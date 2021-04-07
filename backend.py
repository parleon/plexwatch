from time import sleep
import notifier
import refreshtime

while True:
    notifier.checkNotify()
    sleep(30)
    refreshtime.timeRefresher()
    sleep(30)
