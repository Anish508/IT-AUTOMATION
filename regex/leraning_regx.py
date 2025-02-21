log = "July 31 07:51:48 mycomputer bad_process[12345]:ERROR Performing packages upgrade"

""" index = log.index("[")
print(log[index+1:index+6]) """

import re
regex = r"\[(\d+)\]"
result = re.search(regex , log)
print(result[1])
 
print(re.search(r"[Pp]ython", "python"))
print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"[^a-zA-Z ]","This is sentence with spaces."))

""" or to match one or other """
print(re.search(r"cat|dog" , "This is dog"))
print(re.search(r"cat|dog" , "This is both cats and dogs"))

print(re.findall(r"cat|dog", "I like both cats and dogs"))

print(re.search(r"Py.*n", "Pygamilon"))

print(re.search(r"Py.*n", "Python programming"))

print(re.search(r"Py[a-z]*n", "Python programming"))

print(re.search(r"Py[a-z ]*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))

print(re.search(r"o+l+", "woolly"))

print(re.search(r"o+l+", "oily"))

print(re.search(r"p?each", "No one each"))
print(re.search(r"p?each", "No one peach"))

"""Matching with .com"""

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "regex.com"))

"""\w* alpha numberic and whitespaces"""
""" \w: Matches any word character, which includes:
Letters (a-z, A-Z)
Digits (0-9)
Underscore (_)
 """
print(re.search(r"\w*", "This is the example"))
print(re.search(r"\w*", "This_is_another_example"))

print(re.search(r"\bcat\b", "A cat sat on the mat."))  # Matches: 'cat' (full word)
print(re.search(r"\bcat", "catalog"))                 # Matches: 'cat' (at the start of 'catalog')
print(re.search(r"cat\b", "black cat"))               # Matches: 'cat' (at the end of 'cat')

print(re.findall(r"\b\w+\b", "Split this sentence!"))  # ['Split', 'this', 'sentence']

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))