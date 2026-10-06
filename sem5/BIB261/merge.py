# Реализовать процедуру merge двух списков в виде функции
def merge(l1, l2):
    r = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            r.append(l1[i])
            i += 1
        else:
            r.append(l2[j])
            j += 1
        
    r.extend(l1[i:])
    r.extend(l2[j:])
    return r