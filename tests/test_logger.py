# import logging
# import unittest  
# from unittest.mock import patch

# import sys,os

# sys.path.insert(0, '../scripts/')
# sys.path.append(os.path.abspath(os.path.join('scripts')))

# from log_helper import AppLog


import sys
import unittest
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG

class TestCase(unittest.TestCase):
    def testSimpleMsg(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        try:
            print("AA")
            logging.getLogger().info("BB")
        finally:
            logger.removeHandler(stream_handler)