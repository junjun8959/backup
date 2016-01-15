#-*- coding:utf-8 -*-
import time
 
SECONDS_PER_DAY = 24 * 60 * 60
 
def doFunc():
    print "do Function..."
 
def doFirst():
    from datetime import datetime, timedelta
    # 现在的时间
    curTime = datetime.now()
    # 目标时间
    desTime = curTime.replace(hour=16, minute=00, second=0, microsecond=0)
    if desTime > curTime:
        skipSeconds = (desTime - curTime).total_seconds()
    else:
        delta = curTime - desTime
        print delta
        skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
    print "Must sleep %d seconds" % skipSeconds
    return skipSeconds
doFirst()