"""List Filtering
Problem:
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Sample tests:
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

def filter_list(l):
    nonneg = []
    for x in l:
        if type(x) == int:
            if x >= 0:
                nonneg.append(x);
    return nonneg;
    
#   'return a new list with the strings filtered out'