def add_element(s,element):
    s.add(element)

def remove_element(s,element):
    s.discard(element)

def union_and_intersection(s1,s2):
    union_set = s1.union(s2)
    intersection_set = s1.intersection(s2)
    return union_set,intersection_set

def difference(s1,s2):
    return s1.difference(s2)

def is_subset(s1,s2):
    return s1.issubset(s2)

def set_length(s):
    count = 0
    for _ in s:
        count+=1
    return count
def symmetric_difference(s1, s2):
    return s1.symmetric_difference(s2)

def power_set(s):
      from itertools import chain, combinations
      s_list = list(s)
      power_set = set(chain.from_iterable(combinations(s_list, r) for r in range(len(s_list) + 1)))
      return power_set

def unique_subsets(s):
    """Get all unique subsets of a given set."""
    from itertools import chain, combinations
    s_list = list(s)
    unique_subsets = set(chain.from_iterable(combinations(s_list, r) for r in range(len(s_list) + 1)))
    return unique_subsets


# Demonstration of the module functionality
if __name__ == "__main__":
    # Create sets
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    # Demonstrate adding and removing elements
    add_element(set1, 5)
    print(f"Set1 after adding 5: {set1}")

    remove_element(set1, 2)
    print(f"Set1 after removing 2: {set1}")

    # Demonstrate union and intersection
    union_set, intersection_set = union_and_intersection(set1, set2)
    print(f"Union of set1 and set2: {union_set}")
    print(f"Intersection of set1 and set2: {intersection_set}")

    # Demonstrate difference
    diff_set = difference(set1, set2)
    print(f"Difference of set1 and set2: {diff_set}")

    # Check subset
    print(f"Is set1 a subset of set2? {is_subset(set1, set2)}")

    # Set length
    print(f"Length of set1: {set_length(set1)}")

    # Symmetric difference
    sym_diff = symmetric_difference(set1, set2)
    print(f"Symmetric difference of set1 and set2: {sym_diff}")

    # Power set
    power_set_example = power_set(set1)
    print(f"Power set of set1: {power_set_example}")

    # Unique subsets
    unique_subsets_example = unique_subsets(set1)

