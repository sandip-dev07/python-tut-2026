# 1:
# >>>sandip     # will throw error, as withoout quotes it will be treated as variable & NameError: name 'sandip' is not defined 
#>>> "sandip"

print("sandip")

# 2:
# print('sandip's laptop') # SyntaxError: unterminated string literal (detected at line 1)

print("sandip's laptop") # double quotes works fine
print('sandip\'s laptop') # single quotes works fine , but escape character is needed

# print('c:\users\sandip') # 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
print('c:\\users\\sandip')
