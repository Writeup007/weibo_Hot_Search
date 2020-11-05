import os
import time
from scrapy import cmdline


def hot():
    """
    Create a hot - hot.

    Args:
    """
    os.system('scrapy crawl hot')


while True:
    hot()
    time.sleep(60)
