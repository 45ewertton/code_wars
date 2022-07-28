def custom_key(elems):
    return -len(elems), elems.lower()

def mix(s1, s2):
    s1 = sorted(s1.replace(' ', ''))
    s2 = sorted(s2.replace(' ', ''))
    list1 = set(s1)
    list2 = set(s2)
    list_sum = set.union(list1, list2)
    list_result = list()

    for i in list_sum:
        if i.islower():
            if s1.count(i) > 1 or s2.count(i) > 1:
                if s1.count(i) > s2.count(i):
                    list_result.append('1:'+str(i*s1.count(i)))
                elif s1.count(i) < s2.count(i):
                    list_result.append('2:'+str(i*s2.count(i)))
                elif s1.count(i) == s2.count(i):
                    list_result.append('=:'+str(i*s1.count(i)))

    list_result = sorted(list_result, key=custom_key)
    return '/'.join(list_result)