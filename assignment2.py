def removeDuplicates(nums):
    # Create an empty list to store unique values
    unique_nums = []
    
    # Iterate through the input list and add elements to unique_nums if they are not already present
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    
    # return the list containing no duplicates
    return unique_nums

def split_removeDups_and_sort(nums):
    # check if input list length is less than or equal to 20
    if len(nums) > 20:
        return "Error: Input list should not contain more than 20 integers."

    # check if 0 is in the input list
    if 0 in nums:
        return "Error: The number 0 is not a valid input."

    # filter odd and even numbers into two separate lists
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]

    # remove duplicates
    odd_nums = removeDuplicates(odd_nums)
    even_nums = removeDuplicates(even_nums)

    # sort in ascending order
    odd_nums = sorted(odd_nums)
    even_nums = sorted(even_nums)

    return odd_nums, even_nums

nums = [10, 10, 7, 5, 4, 4, 2, 1]
odd_nums, even_nums = split_removeDups_and_sort(nums)

print("Odd numbers:", odd_nums)
print("Even numbers:", even_nums)