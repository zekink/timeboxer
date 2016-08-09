"""
A timeboxing/pomodoro script developed for personal use. I use 5min and 25min timeboxes when working on stuff.
This is version v0.01, only works with 5 minutes or whatever you want to type in manually to the code.
"""

import time

n = 5

def timebox(n):
    m = n * 60
    time.sleep(m)
    print 'Your timebox of ' + str(n) + ' minutes is now complete!'

timebox(n)
