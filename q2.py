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

def symmetric_differenece(s1,s2):
    return symmetric_differenece(s2)

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

