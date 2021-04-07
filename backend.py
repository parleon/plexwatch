from time import sleep
import notifier
import refreshtime

while True:
    notifier.checkNotify()
    sleep(5)
    refreshtime.timeRefresher()
    sleep(55)
