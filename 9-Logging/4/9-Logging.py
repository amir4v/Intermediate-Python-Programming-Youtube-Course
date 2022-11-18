# Logging

import logging

try:
    1 / 0
except Exception as e:
    logging.error(e, exc_info=True) # log (e message) + (Traceback info)
print("Ok!")
'''
ERROR:root:division by zero
Traceback (most recent call last):
  File "/mnt/d/dev/simple-dev-notes/python/Intermediate Python Programming Youtube Course/9-Logging/4/9-Logging.py", line 6, in <module>
    1 / 0
ZeroDivisionError: division by zero
Ok!
'''

import traceback
try:
    1 / 0
except:
    logging.error("Error is %s" , traceback.format_exc())
'''
ERROR:root:Error is Traceback (most recent call last):
  File "/mnt/d/dev/simple-dev-notes/python/Intermediate Python Programming Youtube Course/9-Logging/4/9-Logging.py", line 20, in <module>
    1 / 0
ZeroDivisionError: division by zero
'''
