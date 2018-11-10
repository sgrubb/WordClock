'Represent a word on the clock face'

import lighter
import cronparser

class Word:
    'Represent a word on the clock face'

    def __init__(self, cron, position_array, colourer):
        self.cron = cron
        self.colourer = colourer

        self.current_state = {x: [0, 0, 0] for x in position_array}
        self.target_state = self.current_state.copy()

        self._update_target_state()

    def update(self):
        'Updates the state of the light on the clock face'
        self._update_target_state()
        if self.current_state != self.target_state:
            self._update_lights()

    def _update_target_state(self):
        if self._light_should_be_on():
            self.colourer.set_colours(self.target_state)
        else:
            self._turn_light_off()

    def _light_should_be_on(self):
        light_should_be_on = cronparser.is_now(self.cron)
        return light_should_be_on

    def _turn_light_off(self):
        for key in self.target_state:
            self.target_state[key] = [0, 0, 0]

    def _update_lights(self):
        'Sets the colours of lights and updates current_state accordingly'
        self.current_state = lighter.fade(self.current_state, self.target_state)
