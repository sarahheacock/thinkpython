import time

# take the seconds since 1970
def getTime():
    s = int(time.time())
    days = s/(24 * 60 * 60)

    hours = (s%(24 * 60 * 60)) / (60 * 60)
    minutes = (s%(60 * 60)) / 60
    seconds = s%60

    return str(days) + " days " + str(hours) + ":" + str(minutes) + ":" + str(seconds)

print(getTime())
