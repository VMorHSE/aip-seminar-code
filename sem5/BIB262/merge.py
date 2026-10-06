def merge(sorted_l1, sorted_l2): 
    result = []
    i = j = 0
    while i < len(sorted_l1) and j < len(sorted_l2):
        if sorted_l1[i]<=sorted_l2[j]:
            result.append(sorted_l1[i])
            i += 1
        else:
            result.append(sorted_l2[j])
            j += 1
    result.extend(sorted_l1[i:])
    result.extend(sorted_l2[j:])
    return result