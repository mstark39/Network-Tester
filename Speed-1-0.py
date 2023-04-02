import speedtest
import time

def get_speed():
    st = speedtest.Speedtest()
    return st.download() / 1000000

def check_speed():
    speed = get_speed()
    if speed < 5:
        print("Yellow - Slow speed")
    elif speed >= 5:
        print("Green - Fast speed")
    
def check_internet():
    try:
        response = urllib.request.urlopen('https://www.google.com')
        return True
    except:
        return False

if __name__ == '__main__':
    while True:
        internet_on = check_internet()
        if internet_on:
            check_speed()
        else:
            print("Red - Internet down")
        time.sleep(60)  # wait 10 minutes before checking again
