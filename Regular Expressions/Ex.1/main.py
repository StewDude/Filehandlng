
import re

pattern = re.compile(r"")
string = input("Enter string: ")
pattern = re.compile(r"[0-9]+")
result = pattern.sub("_", string)
print(result)