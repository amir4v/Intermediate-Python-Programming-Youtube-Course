# Logging

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs
'''
app.log
app.log.1
app.log.2
app.log.3
app.log.4
app.log.5
'''
# this will log into app.log and if it's size is over 2KB then logs into app.log.1 , app.log.2 , app.log.3 , app.log.4 , app.log.5
# and if app.log.5 size goes over 2KB logger will go for app.log file and log into it and if it's size is over 2KB then logs into app.log.1 , app.log.2 , app.log.3 , app.log.4 , app.log.5
# rotate

handler = RotatingFileHandler("app.log", maxBytes=2048, backupCount=5)
logger.addHandler(handler)

for _ in range(1000):
    logger.info(f"Hello World! -{_}")
