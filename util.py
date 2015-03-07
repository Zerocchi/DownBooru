__author__ = 'zerocchi'


import os
import datetime as dt

def makefile(path=None):

    if path is not None:
        location = os.path.realpath(path)
    else:
        location = "{}".format(dt.datetime.now().strftime('%Y%m%d%H%M%S'))

    if not os.path.exists(location):
        os.makedirs(location)

    os.chdir(location)
    print(os.path.join(os.path.dirname(__file__)))


def dochelp():
    """Usage: python main.py <tags> <limit> <booru>
<tags> should be enclosed in quotation mark if tag is more than single word"""