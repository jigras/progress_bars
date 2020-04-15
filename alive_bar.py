"""
alive-progress
An animated and smart Progress Bar for python!
"""

from alive_progress import alive_bar
import time

mylist = range(8)


with alive_bar(len(mylist)) as bar:
    for i in mylist:
        bar()
        time.sleep(1)