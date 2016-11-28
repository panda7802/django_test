# coding=utf-8
import functools

print "比较"
def cmp_ignore_case(s1, s2):
    x = s1.lower()
    y = s2.lower()
    if x > y:
        return 1
    if x < y:
        return -1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


sorted_ignore_case = functools.partial(sorted,cmp = lambda s0,s1 : cmp(s0.lower(),s1.lower()))
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])
