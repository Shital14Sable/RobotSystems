from sensing import Sensor
import time
import random
import numpy as np
import picarx_improved

class Controller:
    def __init__(self, adc_sensor_data, sensitivity = 300, polarity='dark'):
        self.left_sensor = adc_sensor_data[0]
        self.mid_sensor = adc_sensor_data[1]
        self.right_sensor = adc_sensor_data[2]
        self.scaled_data = list([0,0,0])
