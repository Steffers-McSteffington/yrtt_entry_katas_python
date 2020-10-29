# Scenario
# Several people are standing in a row divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

# Task
# Given an array of positive integers (the weights of the people), return a new array of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

# Notes
# Array size is at least 1.
# All numbers will be positive.

# Input >> Output Examples
# rowWeights([13, 27, 49])  ==>  return (62, 27)
# Explanation:
# The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.

# rowWeights([50, 60, 70, 80])  ==>  return (120, 140)
# Explanation:
# The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.

# rowWeights([80])  ==>  return (80, 0)
# Explanation:
# The first element 80 is the total weight of team 1, and the second element 0 is the total weight of team 2.

def row_weights(array):

    # SOLUTION 1
    # create two lists: team_one and team_two
    # iterate over array once -
        # if in even position in array move value to team_one list
        # if in odd position in array move value to team_two list
        # repeat until list empty
    # add all the values in team_one list together and record output
    # add all the values in team_two list together and record output

    # SOLUTION 2
    # iterate over array
        # add all key values for elements in an even position together
        # save the result
        # add all key values for elements in an odd position together
        # save the result

    # SOLUTION 3
    # Like a production line sorting parcels - x goes one way and is grouped together, y goes another/different way and is grouped together
    # return values for the grouped things


    team_one = []
    team_two = []
    for weight in array:
        if weight in array[0::2]:
            team_one.append(weight)
        if weight in array[1::2]:
            team_two.append(weight)

    team_one_total = 0
    for weight in team_one:
        team_one_total = team_one_total + weight

    team_two_total = 0
    for weight in team_two:
        team_two_total = team_two_total + weight

    return [team_one_total, team_two_total]