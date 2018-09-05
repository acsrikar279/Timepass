import re
pat = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$_!%*?&])[A-Za-z\d$@$!_%*?&]{8,}')
print(bool(re.match(pat, "123@321ASvds")))
print(bool(re.match(pat, "Srikar@123")))
print(bool(re.match(pat, "654_432nkcdaCCS")))
print(bool(re.match(pat, "acsrikar29")))
print(bool(re.match(pat, "acsrikar@279")))
print(bool(re.match(pat, "acsriKAr_321")))
print(bool(re.match(pat, "ACSRIKAR@123")))
