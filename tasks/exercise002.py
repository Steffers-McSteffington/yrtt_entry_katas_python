# The clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make the 'past' function return the time converted to milliseconds.
# More examples in the test cases below.

def past(h, m, s):

    # need to know how many milliseconds are in a hour/minute/second
    # convert hh into milliseconds
    hours_in_ms = h * 3600000
    # convert mm into milliseconds
    minutes_in_ms = m * 60000
    # convert ss into milliseconds
    seconds_in_ms = s * 1000
    # add hh, mm, ss millisecond values together
    # print output in milliseconds

    return hours_in_ms + minutes_in_ms + seconds_in_ms
