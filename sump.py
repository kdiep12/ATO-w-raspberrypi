from gpiozero import DigitalInputDevice, DigitalOutputDevice
from time import sleep
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Pin configuration
SENSOR_PIN = 17
RELAY_PIN = 27

sensor = DigitalInputDevice(SENSOR_PIN, pull_up=True) # pull-up resistor disabled
pump = DigitalOutputDevice(RELAY_PIN, initial_value=False)

def control_water_level():
    try:
        while True:
            water_detected = (sensor.value == 0)
            
            if water_detected:
                if pump.value:
                    logging.info("Water detected - Stopping pump")
                    pump.off()
            else:
                if not pump.value:
                    logging.info("Water level low - Starting pump")
                    pump.on()
                    
            # Debugging
            logging.info(f"Raw sensor value: {sensor.value}")
            logging.info(f"Water detected: {water_detected}")
            logging.info(f"Pump status: {'ON' if pump.value else 'OFF'}")
            sleep(1)
        
    except KeyboardInterrupt:
        logging.info("\nShutting down...")
        pump.off()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        pump.off()
    
if __name__ == "__main__":
    logging.info("Starting water level control system...")
    logging.info("Press CTRL+C to exit")
    control_water_level()
