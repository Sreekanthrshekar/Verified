''' This document displays the ability of json module to pretty-print
 dictionaries '''
import json

# standad representation
my_dict = {'a':23,'b':43,'c':0x0eeff}
print(my_dict)

# json module representation of dictionary
print(json.dumps(my_dict, indent=4,sort_keys=True))
