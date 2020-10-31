# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.
import pytest

from tasks.exercise004 import pig_it

def test_pig_latin_returns_string():
    assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
    assert pig_it("This is my string") == "hisTay siay ymay tringsay"

def test_pig_latin_punctuation():
    assert pig_it("Pig latin is cool!!") == "igPay atinlay siay oolcay!!"


# considerations/ additional tests:
    # what if the word is a single letter without punctuation
    # what if the word is a contraction (e.g. 'til)
    # removing punctuation as first step and returning it at the end only works if it is a single sentence with no other punctuation.
        # need to think about how to manage commas/semi-colons/colons/special character and/or strings of more than one sentence.