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

def get_sum_sequence():
    try:
        numbers = list(map(int, input("Enter a sequence of numbers (space-separated): ").split()))
        k = int(input("Enter the value of k: "))
        result = []
        for _ in range(k):
            start, end = map(int, input("Enter start and end indices (space-separated): ").split())
            result.append(sum(numbers[start:end + 1]))
        return result1
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        return []

k_sized_list = get_sum_sequence()
print(k_sized_list)


