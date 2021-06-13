import picarx_improved
import time
import numpy as np

try :
    from ezblock import *
    from ezblock import __reset_mcu__
    __reset_mcu__()
    time.sleep (0.01)
except ImportError :
    print ("This computer does not appear to be a PiCar -X system \
    (/opt/ezblock is not present). Shadowing hardware calls \
    with substitute functions")
    from sim_ezblock import *

class Sensor:
    def __init__(self, ADC):
        self.S0 = self.ADC('A0')
        self.S1 = self.ADC('A1')
        self.S2 = self.ADC('A2')

    def sensor_reading(self):
        self.adc_op = [self.S0, self.S1, self.S2]
        return self.adc_op

if __name__ == '__main__':
    abc = Sensor
    sensor_values = abc.sensor_reading()
