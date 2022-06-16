# Write code snippet to extract the operating system and version from the provided string

ua = 'Mozilla/5.0 (Windows NT 10.0)' #the provided string
find_opening_bracket = ua.find('(')
find_closing_bracket = ua.find(')')

os_ver = ua[find_opening_bracket + 1: find_closing_bracket]

print(os_ver)
