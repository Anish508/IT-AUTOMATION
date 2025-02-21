import re
print(re.split(r"[.?!]", "one senetnce. another sentence ? and the last one?"))
print(re.split(r"([.?!])", "one senetnce. another sentence ? and the last one?"))

""" regex = r"[\w.%-]+@[\w.-]+", "[REDACTED]"
text = "Received a e-mail for [REDACTED]" """
result = re.sub(r"[\w.%-]+@[\w.-]+", "[REDACTED]", "Received a e-mail for [REDACTED]")
print(result)

new_result = re.sub(r"^([\w .-]*), ([\w .-]*)$",      r"\2 \1" , "Lovelace, ada")
print(new_result)

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

r"\b\w*[aeiou]{3}\w*\b"

r"(\b\d{3}-\d{3}-\d{4}\b)", r"+1-\1"

r"^\s*#+", r"//"