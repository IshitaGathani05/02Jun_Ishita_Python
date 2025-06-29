#Write a Python program to sort a list using both sort() and sorted(). 

numbers = [25, 10, 45, 5, 90, 30]

# Using sorted() - returns a new sorted list
sorted_list = sorted(numbers)
print("Original list:", numbers)
print("Sorted list using sorted():", sorted_list)

# Using sort() - modifies the original list
numbers.sort()
print("List after using sort():", numbers)