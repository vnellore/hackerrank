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

if __name__ == '__main__':

    #n = int(input())
    #x = list(map(int, input().split(' ')))
    x = list(map(int, '10 40 30 50 20'.split(' ')))
    y = list(map(int, '1 2 3 4 5'.split(' ')))

    print('Mean is ' + str(mean(x)))    
    print('Median is ' + str(median(x)))
    print('Weighted mean is ' + str(weighted_mean(x, y)))
    #print('Mode is ' + str(mode(x)))