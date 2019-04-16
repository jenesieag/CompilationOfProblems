"""The marketing team is spending way too much time typing in hashtags.
Let's help them with out own Hashtag Generator!
Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Sample tests:
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""

def generate_hashtag(b):
    #your code here
    if b == "":
        return False;
    wordArray = b.split(" ");
    b = "";
    for x in wordArray:
        b += x[:1].upper() + x[1:len(x)].lower();
    b = "#" + b;    
    if len(b) > 140:
        return False;
    return b;