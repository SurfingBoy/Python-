import re
print('result:',re.split(r'[\s\,]+','a,b, c  d'))
print('result2:',re.split(r'\s+', 'a b   c'))