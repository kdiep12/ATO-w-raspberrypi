from gpiozero import InputDevice
from time import sleep

#Pin configuration
SENSOR_PIN = 17
water_sensor = InputDevice(SENSOR_PIN, pull_up=True) # pull-up resistor disabled

try:
    while True:
        if water_sensor.value == 1:
            print("Water level LOW")
            sleep(0.5)
        else:
            print("Water level OK")
            sleep(0.5)
        sleep(1)
except KeyboardInterrupt:
    print("Exiting program")