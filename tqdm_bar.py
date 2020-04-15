"""
tqdm
A Fast, Extensible Progress Bar for Python and CLI
"""

import time
from tqdm import tqdm

mylist = range(8)
for i in tqdm(mylist):
    time.sleep(1)