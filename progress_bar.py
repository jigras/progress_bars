"""
progress
Easy progress reporting for Python
"""

import time
from progress.bar import IncrementalBar, ChargingBar, FillingSquaresBar, Bar, PixelBar, ShadyBar

MAX = 8
MYLIST = range(MAX)


def iterbar(bar, mylist):
    for i in mylist:
        bar.next()
        time.sleep(1)
    bar.finish()


if __name__ == '__main__':
    bar = Bar('Bar', max=MAX)
    filling_squares_bar = FillingSquaresBar('FillingSquaresBar', max=MAX)
    charging_bar = ChargingBar('ChargingBar', max=MAX)
    incremental_bar = IncrementalBar('IncrementalBar', max=MAX)
    pixel_bar = PixelBar('PixelBar', max=MAX)
    shady_bar = ShadyBar('ShadyBar', max=MAX)

    iterbar(bar, MYLIST)
    iterbar(charging_bar, MYLIST)
    iterbar(incremental_bar,MYLIST)