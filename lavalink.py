from os import getenv
from re import sub

try:
    temp = open('applicate.yml', 'r').read()
    temp = sub('REPLACEPASSWORD', getenv('PASSWORD'), temp)
    open('application.yml', 'w').write(temp)
except:
    pass
