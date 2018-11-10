'Parses cron objects and returns true if the current time is in the given range'

import datetime

def is_now(cron_input):
    'Checks cron range array against current time'
    # QQ:SMG day light savings
    now = datetime.datetime.now()
    cron_ranges_bool_array = []
    for cron in _get_multiple_ranges(cron_input):
        if _input_not_in_any_ranges(cron[0], now.year):
            cron_ranges_bool_array.append(False)
            continue
        if _input_not_in_any_ranges(cron[1], now.month):
            cron_ranges_bool_array.append(False)
            continue
        if _input_not_in_any_ranges(cron[2], now.day):
            cron_ranges_bool_array.append(False)
            continue
        if _input_not_in_any_ranges(cron[3], now.hour):
            cron_ranges_bool_array.append(False)
            continue
        if _input_not_in_any_ranges(cron[4], now.minute):
            cron_ranges_bool_array.append(False)
            continue
        if _input_not_in_any_ranges(cron[5], now.second):
            cron_ranges_bool_array.append(False)
            continue
        cron_ranges_bool_array.append(True)
    return any(cron_ranges_bool_array)

def _get_multiple_ranges(cron_input):
    # Set up initial conditions
    should_continue = False
    index = 0
    new_cron_range = []

    while True:
        # Execute loop
        for cron_string in cron_input:
            cron_ranges = cron_string.split(" & ")
            if index < len(cron_ranges):
                should_continue = True
                new_cron_range.append(cron_ranges[index])
            else:
                # Use last range
                new_cron_range.append(cron_ranges[-1])

        # Stop if done
        if not should_continue:
            raise StopIteration

        # Return constructed cron range
        yield new_cron_range

        # Else reset initial conditions
        new_cron_range = []
        index += 1
        should_continue = False


def _input_not_in_any_ranges(cron_ranges, input_datetime):
    return not _input_in_one_of_ranges(cron_ranges, input_datetime)

def _input_in_one_of_ranges(cron_ranges, input_datetime):
    ranges = cron_ranges.split(",")
    for cron_range in ranges:
        if _input_in_range(cron_range, input_datetime):
            return True
    return False

def _input_in_range(cron_range, input_datetime):
    if cron_range == '*':
        return True
    parsed_range = cron_range.split("-")
    start_range = int(parsed_range[0])

    if len(parsed_range) == 1:
        return int(start_range) == input_datetime

    end_range = int(parsed_range[1])
    return start_range <= input_datetime and input_datetime < end_range
