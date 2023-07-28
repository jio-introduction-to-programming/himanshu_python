def list(lst):
    return sum(lst)
def list_max(lst):
    return max(lst)
def list_reverse(lst):
    return lst[::-1]
def bubble_sort(lst):
    n=len(lst)
    for i in range(n):
      for j in range (0, n-i-1 ): 
          if lst[j]>lst[j+1]:
              lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
import statistics
import collections
def list_stats(lst):
    return(statistics.mean(lst),statistics.mode(lst))
print(list([1,2,3,4]))
print(list_max([1,2,3,4]))
print(list_reverse([1,2,3,4]))
print(bubble_sort([1,2,3,4]))
print(list_stats([1,2,3,4]))

numbers = list(map(int, input("Enter a sequence of numbers separated by spaces: ").split()))
k = int(input("Enter another integer k: "))
indices = []
for i in range(k):
    start, end = map(int, input(f"Enter two numbers start and end for {i+1}th query separated by spaces: ").split())
    indices.append((start, end))
sums = [sum(numbers[start:end+1]) for start, end in indices]
print(f"The result is: {sums}")



