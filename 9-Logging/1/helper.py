import logging

logger = logging.getLogger(__name__) # Return a logger with the specified name # __name__: name of this file: helper
# logger = logging.getLogger("my_logger")

# logger.propagate # by default it's True - when you import this file in another file like 9-Logging.py this logger will get the configs from that another file (like 9-Logging.py)
# logger.propagate = False

logger.info("hello from helper")
