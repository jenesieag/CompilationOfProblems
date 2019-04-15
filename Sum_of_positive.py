""" SUM OF POSITIVE
Problem: You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0."""

def sumOfPostive():
    sampleInt = [1,-4,7,12];
    positiveInt =[];
    for x in sampleInt:
        if x > 0:
            positiveInt.append(x);
        elif x = 0:
            return 0;
    if len(positiveInt) == 0:
        return 0;
    return sum(positiveInt);        
    

if __name__ == "__main__":
    sumOfPostive();
    