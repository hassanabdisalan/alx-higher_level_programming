#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weighted_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_sum += score * weight
        total_weight += weight

    return total_weighted_sum / total_weight if total_weight != 0 else 0
