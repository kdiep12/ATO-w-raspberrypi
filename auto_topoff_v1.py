from gpiozero import DigitalInputDevice, DigitalOutputDevice
from time import sleep, time
import logging

#Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

#Pin configuration
SENSOR_PIN = 17
RELAY_PIN = 27

#Safe limits
MAX_PUMP_DURATION = 300
CHECK_INTERVAL = 1

sensor = DigitalInputDevice(SENSOR_PIN, pull_up=True) # pull-up resistor disabled
pump = DigitalOutputDevice(RELAY_PIN, initial_value=False)

def control_water_level():
    pump_start_time = None

    try:
        while True:
            water_detected = (sensor.value == 0)
            
            if water_detected:
                if pump.value:
                    logging.info("Water detected - Stopping pump")
                    pump.off()
                pump_start_time = None
            else:
                if not pump.value:
                    logging.info("Water level low - Starting pump")
                    pump.on()
                    pump_start_time = time()
                else:
                    if pump_start_time and time() - pump_start_time > MAX_PUMP_DURATION:
                            logging.warning("Pump running too long - Stopping pump")
                            pump.off()
                            pump_start_time = None
                    
            # Debugging
            logging.info(f"Raw sensor value: {sensor.value}")
            logging.info(f"Water detected: {water_detected}")
            logging.info(f"Pump status: {'ON' if pump.value else 'OFF'}")
            
            sleep(CHECK_INTERVAL)
        
    except KeyboardInterrupt:
        logging.info("\nShutting down...")
        pump.off()
    except Exception as e:
        logging.error(f"Error occured: {e}")
        pump.off()
    
if __name__ == "__main__":
    logging.info("Starting water level control system...")
    logging.info("Press CTRL+C to exit")
    control_water_level()
        

        