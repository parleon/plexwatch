from time import sleep
import notifier
import refreshtime

while True:
    notifier.checkNotify()
    sleep(1)
    refreshtime.timeRefresher()
    sleep(59)
