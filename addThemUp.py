#
# input("Enter numbers separated by space: ").split() takes a string of numbers separated by spaces from the user and splits it into a list of strings.
# map(int, ...) converts each string in the list to an integer.
# list(...) converts the map object to a list.
# sum(numbers) calculates the sum of the numbers in the list.

a, b = list(map(int,input().split(" ")))
print(a+b)