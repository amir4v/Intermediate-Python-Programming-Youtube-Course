# Logging

import logging

import logging.config

logging.config.fileConfig('logging.conf')
# we have also: logging.config.dictConfig

logger = logging.getLogger("simpleExample")

logger.debug("msg") # 2022-08-22 17:37:16,546 - simpleExample - DEBUG - msg
