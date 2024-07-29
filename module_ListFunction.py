#1)
#a)
def find_max(l1):
    if not l1:
        return None # empty list
    
    max_value=l1[0]
    for value in l1:
        if value>max_value:
            max_value = value
    return max_value

def find_min(l1):
    if not l1:
        return None # empty list
    
    min_value=l1[0]
    for value in l1:
        if value<min_value:
            min_value = value
    return min_value

def find_sum(l1):
     tsum=0
     for value in l1:
        tsum+=value
     return tsum
    
def find_avg(l1):
    avg=sum(l1)/len(l1)
    return avg

def find_median(l1):
    sorted_list = sorted(l1)
    n=len(sorted_list)

    if(n%2==1):
        median=sorted_list[n//2]
    else:
        mid1=sorted_list[n//2 -1]
        mid2=sorted_list[n//2]
        median = (mid1+mid2)/2
    return median

squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]

print("List of squares:", squares)
print("Maximum value in squares:",find_max(squares))
print("Minimum value in squares:",find_min(squares))
print("Sum of squares:",find_sum(squares))
print("Average of squares:",find_avg(squares))
print("Median of squares:",find_median(squares))

print("\nList of even numbers:", evens)
print("Maximum value in squares:",find_max(evens))
print("Minimum value in squares:",find_min(evens))
print("Sum of squares:",find_sum(evens))
print("Average of squares:",find_avg(evens))
print("Median of squares:",find_median(evens))

