import random 
while True:
    t=random.randint(25,100)
    h=random.randint(40,100)
    print("-------------------------------------")
    if t>30: 
        print("High temperature detetcted")
        print("Buzzer on,alarm sound is high")
    elif t==30: 
        print("Temprature reached maximum thershold of 30 degrees celsius") 
    else: 
        print("Temperature is good") 
#for Humidity 
    if h>65 : 
        print("High humidity detetcted")
        print("Buzzer on,alarm sound is high")    
    elif t == 65: 
        print("Humidity reached maximum thershold of 65 percent") 
    else: 
        print("Humidity is good")
