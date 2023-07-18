def list_sum(lst):
    
    total = 0
    
    for x in lst:
       
        total += x
  
    return total
def list_max(lst):
   
    max_elem = None
    
    for x in lst:
        
        if max_elem is None or x > max_elem:
           
            max_elem = x
   
    return max_elem
def list_reverse(lst):
    
    reversed_lst = []
    
    for i in range(len(lst) - 1, -1, -1):
        
        reversed_lst.append(lst[i])
    
    return reversed_lst
def bubble_sort(lst):
    
    n = len(lst)
   
    for i in range(n-1):
       
        for j in range(0, n-i-1):
           
            if lst[j] > lst[j+1]:
               
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    return lst
def list_stats(lst):
    
    total = 0
    
    freq = {}
    
    mode = None
    
    max_freq = 0
   
    for x in lst:
        
        total += x
        
        freq[x] = freq.get(x, 0) + 1
       
        if freq[x] > max_freq:
            
            mode = x
            max_freq = freq[x]
   
    mean = total / len(lst)

    return (mean, mode)


print(list_sum([1,2,3,4]))
print(list_max([1,2,3,4]))
print(list_reverse([1,2,3,4]))
print(bubble_sort([1,2,3,4]))
print(list_stats([1,2,3,4]))


numbers = list(map(int, input("Enter a sequence of numbers separated by spaces: ").split()))

k = int(input("Enter another integer k: "))


indices = []

for i in range(k):
    
    indices.append(list(map(int, input(f"Enter two numbers start and end for {i+1}th query separated by spaces: ").split())))


sums = []

for start, end in indices:
 
    sub_sum = 0
   
    for j in range(start, end + 1):
       
        sub_sum += numbers[j]
   
    sums.append(sub_sum)

print(f"The result is: {sums}")