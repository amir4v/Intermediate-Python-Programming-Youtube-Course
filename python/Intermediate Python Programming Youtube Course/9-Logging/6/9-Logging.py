# Logging

import logging
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s(second), m(minute), h(hour), d(), midnight, w0(monday)
handler = TimedRotatingFileHandler("timed.log", when='s', interval=1, backupCount=5)
logger.addHandler(handler)
# just like section 5 but this will rotate after 1 second

for _ in range(10):
    logger.info(f"Hello World! -{_}")
    time.sleep(1)
