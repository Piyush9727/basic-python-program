import time
def Countdown_Timer(t):
    if t < 0:
        print("Invalid input, please enter valid time")
    while t > 0:
        min,secs = divmod(t,60)

        timer = "{:02d}:{:02d}" .format( min , secs) # {:02d}:{:02d} = there is twodigit number and with leading number of zeros

        print(timer,end="\r")

        time.sleep(1)
        t-=1
    print("Time Complited!!!")

try:
    t=int(input("Enter time in second = > "))
    Countdown_Timer(t)
except ValueError:
    print("Invalid input")


