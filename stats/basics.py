from collections import Counter

def mean(numbers):
    mean_value = sum(numbers) / len(numbers)
    return round(mean_value, 1)

def median(numbers):
    sorted_numbers = sorted(numbers)
    num_length = len(sorted_numbers)

    median = 0
    midpoint = int(num_length / 2)
        
    if num_length % 2 == 0:
        median = ( sorted_numbers[midpoint - 1] + sorted_numbers[midpoint] ) / 2
    else:
        median = sorted_numbers[midpoint]
    
    return round(median, 1)

def mode(numbers):
    num_counter = Counter(numbers)
    print(num_counter)
    most_common_list = []

    most_recent_count = 0
    for i in iter(num_counter):
        if len(most_common_list) == 0:
            most_common_list.append(i)
            most_recent_count = num_counter[i]
        else:
            if num_counter[i] == most_recent_count:
                most_common_list.append(i)
    
    most_common_list.sort()
    return most_common_list[0]

def weighted_mean(data_points, weights):
    weighted_mean_val = 0
    for data_point, weight in zip(data_points, weights):
        weighted_mean_val += (data_point * weight)
    
    weighted_mean_val = weighted_mean_val / sum(weights)
    return weighted_mean_val

def compute_quartiles(number_list):
    second_quartile = median(number_list)
    print(f'second quartile is {second_quartile}')
    sorted_num_list = sorted(number_list)
    print(sorted_num_list)
    
    half_point = int(len(sorted_num_list) / 2)
        
    if second_quartile in sorted_num_list:
        del sorted_num_list[half_point]
        
    first_half = sorted_num_list[0:half_point]
    second_half = sorted_num_list[half_point:]

    first_quartile = median(first_half)
    third_quartile = median(second_half)
    print(first_half)
    print(second_half)
    print(f'first quartile - {int(first_quartile)}')
    print(f'third quartile - {int(third_quartile)}')


if __name__ == '__main__':

    #n = int(input())
    #x = list(map(int, input().split(' ')))
    x = list(map(int, '3 7 8 5 12 14 21 13 18'.split(' ')))
    compute_quartiles(x)
