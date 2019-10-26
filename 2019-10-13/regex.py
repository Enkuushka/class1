import re
longString = "RD11223344"
key = "^[A-Z][A-Z][0-9]{8}$"
matches = re.search(key, longString)
print(matches)
