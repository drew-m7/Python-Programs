import time
# simple timer in python!
def mycountdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Timer completed!')

t = input('Enter the time to count down in seconds: ')

mycountdown(int(t))
