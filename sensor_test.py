from gpiozero import InputDevice
from time import sleep

#Pin configuration
SENSOR_PIN = 17
water_sensor = InputDevice(SENSOR_PIN, pull_up=True) # pull-up resistor disabled

try:
    while True:
        if water_sensor.value == 0:
            print("Water level LOW - Activating pump")  
        else:
            print("Water level OK - Pump off")            
        sleep(1)
except KeyboardInterrupt:
    print("Exiting program")