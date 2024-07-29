def merge_dicts(*args):
    """Merge multiple dictionaries into one."""
    merged = {}
    for dictionary in args:
        if not isinstance(dictionary, dict):
            raise ValueError("All arguments must be dictionaries.")
        for key, value in dictionary.items():
            if key in merged:
                if isinstance(merged[key], list):
                    merged[key].append(value)
                else:
                    merged[key] = [merged[key], value]
            else:
                merged[key] = value
    return merged

def find_common_keys(*args):
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    
    common_keys = set(args[0].keys())
    for dictionary in args[1:]:
        if not isinstance(dictionary, dict):
            raise ValueError("All arguments must be dictionaries.")
        common_keys.intersection_update(dictionary.keys())
    
    return common_keys

def sum_values(*args):
    """Sum values for each key across multiple dictionaries."""
    summed = {}
    for dictionary in args:
        if not isinstance(dictionary, dict):
            raise ValueError("All arguments must be dictionaries.")
        for key, value in dictionary.items():
            if not isinstance(value, (int, float)):
                raise ValueError("All values must be integers or floats.")
            if key in summed:
                summed[key] += value
            else:
                summed[key] = value
    return summed

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
dict3 = {'a': 2, 'd': 6}

# Merge dictionaries
merged = merge_dicts(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

# Find common keys
common_keys = find_common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys)

# Sum values for each key
summed_values = sum_values(dict1, dict2, dict3)
print("Summed Values:", summed_values)

#a)
def merging_Dict(*args):
    """Merge multiple dictionaries into one."""
    merged = {}
    for dictionary in args:
        if not isinstance(dictionary, dict):
            raise ValueError("All arguments must be dictionaries.")
        for key, value in dictionary.items():
            if key in merged:
                if isinstance(merged[key], list):
                    merged[key].append(value)
                else:
                    merged[key] = [merged[key], value]
            else:
                merged[key] = value
    return merged

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'a': 5, 'd': 6}

merged = merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

#b)
def find_common_keys(*args):
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    
    common_keys = set(args[0].keys())
    for dictionary in args[1:]:
        if not isinstance(dictionary, dict):
            raise ValueError("All arguments must be dictionaries.")
        common_keys.intersection_update(dictionary.keys())
    
    return common_keys

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'b': 5, 'd': 6}

common_keys = find_common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys)

#c)
def invert_dict(dictionary):
    """Invert a dictionary, swapping keys and values. Group keys with the same value into a list."""
    inverted = {}
    for key, value in dictionary.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 1}

inverted = invert_dict(dict1)
print("Inverted Dictionary:", inverted)

#d)
def find_common_key_value_pairs(*args):
    """Find common key-value pairs across multiple dictionaries."""
    if not args:
        return set()
    
    common_pairs = set(args[0].items())
    for dictionary in args[1:]:
        if not isinstance(dictionary, dict):
            raise ValueError("All arguments must be dictionaries.")
        common_pairs.intersection_update(dictionary.items())
    
    return common_pairs

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'c': 3}
dict3 = {'b': 2, 'd': 4}

common_pairs = find_common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_pairs)


