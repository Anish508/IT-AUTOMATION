import re 

""" capturing groups """
""" Swaping first and last name """
result = re.search(r"(\w*), (\w*)$", "lovelace, ada")
print(result[0])
print(result.groups())
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))


""" Matching exact words using {} """

match = re.search(r"[a-zA-Z]{5}","A Ghost is Real")
print(match)

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))

""" upper and lower bound limit """
print(re.findall(r"\w{5,10}", "I Really like strawbwrries"))
print(re.findall(r"\w{5,}", "I Really like strawbwrries"))


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))