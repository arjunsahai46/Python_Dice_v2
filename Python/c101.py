import time
input_secs=int(input("Enter time in secs:"))
while input_secs>0:
    mins=int(input_secs/60)
    s=input_secs%60
    print(mins,":",s)
    input_secs-=1
    time.sleep(1)