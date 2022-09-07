# write a code snippet to extract the operating system and version from the string

ua = 'Mozilla/5.0 (Windows NT 10.0)'

# start = ua.startswith('(')
left = ua.find('(')
right = ua.find(')')
os_ver = ua[ua.find("(")+1:ua.find(")")]
print(os_ver)

