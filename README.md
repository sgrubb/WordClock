Word Clock
===================

# Making a Raspberry Pi Image
## Download and prepare SD Card
Download Raspian Stretch Lite from https://www.raspberrypi.org/downloads/raspbian/
Write image using Win32DiskImager

## Boot and set up Wifi 
https://www.piborg.org/blog/pi-zero-wifi-bluetooth
``sudo nano /etc/wpa_supplicant/wpa_supplicant.conf``
add to bottom of file:

	network={
          	ssid="Network Name"
          	psk="password"
	}

## Enable SPI, SSH, I2C etc.

``sudo raspi-config``

- Go to interfacing -> enable SSH
- Go to interfacing -> enable I2C
- Go to interfacing -> enable SPI
- Change Boot Options -> Desktop/Cli -> Console Autologin

## Get latest updates to the OS

	sudo apt-get update && sudo apt-get -y upgrade
	sudo apt-get -y install git python-smbus i2c-tools python-dev python-pip build-essential scons swig apache2 php libapache2-mod-php bluez-tools

## Bluetooth
See https://raspberrypi.stackexchange.com/questions/29504/how-can-i-set-up-a-bluetooth-pan-connection-with-a-raspberry-pi-and-an-ipod

``sudo vi /etc/systemd/network/pan0.netdev``

    [NetDev]
    Name=pan0
    Kind=bridge

``sudo vi /etc/systemd/network/pan0.network``

    [Match]
    Name=pan0

    [Network]
    Address=10.1.1.1/24
    DHCPServer=yes

``sudo vi /etc/systemd/system/bt-agent.service``

    [Unit]
    Description=Bluetooth Auth Agent

    [Service]
    ExecStart=/usr/bin/bt-agent -c NoInputNoOutput
    Type=simple

    [Install]
    WantedBy=multi-user.target

``sudo vi /etc/systemd/system/bt-network.service``

    [Unit]
    Description=Bluetooth NEP PAN
    After=pan0.network

    [Service]
    ExecStart=/usr/bin/bt-network -s nap pan0
    Type=simple

    [Install]
    WantedBy=multi-user.target

``sudo systemctl enable systemd-networkd``

``sudo systemctl enable bt-agent``

``sudo systemctl enable bt-network``

``sudo systemctl start systemd-networkd``

``sudo systemctl start bt-agent``

``sudo systemctl start bt-network``

``sudo nano /etc/profile`` and add the lines:

    sudo bt-adapter --set Discoverable 1

## File editor web site

``sudo rm /var/www/html/index.html``

``sudo ln -s /home/pi/WordClock/index.php /var/www/html/index.php``

``sudo ln -s /home/pi/WordClock/index.css /var/www/html/index.css``

`` sudo chmod 777 /etc/wpa_supplicant/wpa_supplicant.conf``

## Git key gen

	ssh-keygen -t rsa -C "[email address]" -b 4096
	
Set up Git config	
	
	git config --global user.email "[email address]"
	git config --global user.name "[name]"

Add to Gitlab SSH key list

	cat .ssh/id_rsa.pub

## Get and build code

Dotstar

	cd ~
	git clone git@github.com:adafruit/Adafruit_DotStar_Pi.git
	cd ~/Adafruit_DotStar_Pi
	python setup.py build
    sudo python setup.py install

WS2813

	cd ~
	git clone git@github.com:jgarff/rpi_ws281x.git
	cd ~/rpi_ws281x 
	scons
	cd python
	python ./setup.py build
	sudo python setup.py install

WordClock

	cd ~
	git clone git@github.com:sgrubb/WordClock.git
	cd ~/WordClock

## Autostart clock on reboot

``sudo vi /etc/profile`` and add the lines:

    ps -caf | grep WordClock | grep -v grep | grep -v sudo
    if [ $? -eq 0 ]; then
      echo "Clock is already running"
    else
      echo "Start Clock."
      sudo python /home/pi/WordClock/main.py &
    fi
    cd /home/pi/WordClock;git pull
    

## How to set up Wifi details using Bluetooth

- Reboot - Bluetooth will be discoverable for 3 minutes
- Connect via Bluetooth
- Open https://10.1.1.1 in a browser
- Change the ``wpa_supplicant.conf`` file


## Network Time config:

https://wiki.archlinux.org/index.php/Systemd-timesyncd

``sudo vi /etc/systemd/timesyncd.conf``

	[Time]
	NTP=0.arch.pool.ntp.org 1.arch.pool.ntp.org 2.arch.pool.ntp.org 3.arch.pool.ntp.org
	FallbackNTP=0.pool.ntp.org 1.pool.ntp.org 0.fr.pool.ntp.org
	
## Set timezone

``sudo dpkg-reconfigure tzdata``
	
## Real Time Clock (RTC)

https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-rtc-time

``sudo vi /boot/config.txt``
add to end of file:

	dtoverlay=i2c-rtc,pcf8523

reboot them run ``sudo i2cdetect -y 1`` which should show UU where 0x68 is
disable fake clock:

	sudo apt-get -y remove fake-hwclock
	sudo update-rc.d -f fake-hwclock remove

``sudo vi /lib/udev/hwclock-set`` and comment out:

	#if [ -e /run/systemd/system ] ; then
	# exit 0
	#fi

run ``date`` to verify date

run ``sudo hwclock -w`` to write to RTC

# Misc Notes

## Types of strip
https://github.com/ManiacalLabs/AllPixel/wiki/Connecting-the-LEDs

### WS2812 / WS2812B (Neopixels)

- Use WS2811 Controller strip hence sometimes referred to as "WS2812B strip with WS2811 controller"
- If one LED is broken, rest of strip won't work
- WS2812B has intelligent reverse connect protection and the power supply reverse connection does not damage the IC.
- Strict 800KHz data rate (bottleneck on long strands)
- 400Hz refresh/PWM rate
- Smetimes called APA104 (dont confuse with APA102 aka DotStar)

### WS2813

- same controller as WS2812
- has BIN (Backup In) Pin

### APA102 DotStar

- Built in PWM controller
- AKA LPD8806
- Uses SPI
- 32MHz data rate, 19.2KHz PWM rate


## Debugging Wifi Issues
kill the wpa_supplicant process and run it manually:

    sudo wpa_supplicant -c/etc/wpa_supplicant/wpa_supplicant.conf -iwlan0 -dd
    
## Web administration console (Optional)

See http://www.webmin.com/deb.html

    sudo sh -c 'echo "deb http://download.webmin.com/download/repository sarge contrib" > /etc/apt/sources.list.d/webmin.list'
    wget -qO - http://www.webmin.com/jcameron-key.asc | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install webmin

