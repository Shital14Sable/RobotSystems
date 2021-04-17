
from picarx_improved import picarx_improved
import time
import numpy as np

class Sensor():
    def __init__(self, ADC):
        self.S0 = self.ADC('A0')
        self.S1 = self.ADC('A1')
        self.S2 = self.ADC('A2')

    def sensor_reading(self):
        self.adc_op = [self.S0, self.S1, self.S2]
        return self.adc_op

if __name__ == '__main__':
     abc = Sensor
     abc.sensor_reading()
