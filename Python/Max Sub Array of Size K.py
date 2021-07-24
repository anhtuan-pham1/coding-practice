# Given an array of positive numbers and a positive number ‘ k, ’
# find the maximum sum of any contiguous subarray of size ‘k’.

def max_sub_array_of_size_k(k, arr):
    global_max = 0
    for i in range (len(arr) - k + 1):
        local_sum = 0
        for j in range (i,i + k ):
            local_sum += arr[j]
        if (local_sum > global_max):
            global_max = local_sum
    return global_max


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()

