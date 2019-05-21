"""Find the capitals
Problem: Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

Example:
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
"""
def capitals(word):
    #your code here
    print (word);
    capsArr = [];
    for x in range(0,len(word)):
        if word[x].isupper():
            capsArr.append(x);
    print (capsArr);
    return capsArr;