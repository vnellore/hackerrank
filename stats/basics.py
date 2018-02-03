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
    sorted_num_list = sorted(number_list)
    
    half_point = int(len(sorted_num_list) / 2)
        
    if second_quartile in sorted_num_list:
        del sorted_num_list[half_point]
        
    first_half = sorted_num_list[0:half_point]
    second_half = sorted_num_list[half_point:]

    first_quartile = median(first_half)
    third_quartile = median(second_half)
    
    return first_quartile, second_quartile, third_quartile

def compute_interquartile_range(input_list):
    first_q, second_q, third_q = compute_quartiles(input_list)
    return third_q - first_q

def process_freq_datasets(x, f):
    print(f'x - {x}')
    print(f'f - {f}')
    
    s = [i[0] for i in zip(x,f) for j in range(i[1]) ]
                
    return sorted(s)

if __name__ == '__main__':

    #n = int(input())
    #x = list(map(int, input().split(' ')))
    x = list(map(int, '10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10'.split(' ')))
    f = list(map(int, '1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20'.split(' ') ))
    s = process_freq_datasets(x, f)
    print(s)
    intquartile_range = compute_interquartile_range(s)

    print(float(intquartile_range))