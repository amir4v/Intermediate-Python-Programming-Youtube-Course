# Logging

import logging

# logging levels
# logging.debug("msg")
# logging.info("msg")
# logging.warning("msg") # WARNING:root:msg
# logging.error("msg") # ERROR:root:msg
# logging.critical("msg") # CRITICAL:root:msg
# by default, logging level is warning

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y/%m/%d - %H:%M:%S")
# asctime: Himan-readable time when the LogRecord was created
# name:    name of the logger used to log the call

logging.debug("msg") # 2022/08/22 - 16:03:17 - root - DEBUG - msg
# THE DEFAULT LOGGER IS 'root' LOGGER

# you can create YOUR OWN LOGGER

import helper # 2022/08/22 - 16:07:46 - helper - INFO - hello from helper
