from sensing import Sensor
import time
import random
import numpy as np
import picarx_improved

class Interpreter:
    def __init__(self, adc_sensor_data, sensitivity = 300, polarity='dark'):
        self.adc_sensor_data = adc_sensor_data
        self.scaled_data = list([0,0,0])
        self.sensitivity = sensitivity
        self.polarity = polarity

    
    def scaling(self):
        max_index = self.adc_sensor_data.index(max(self.adc_sensor_data))
        min_index = self.adc_sensor_data.index(min(self.adc_sensor_data))
        list1 = [-1, 0, 1]
        list1 = list1.remove(max_index)
        list1 = list1.remove(min_index)
        third_index = list1[0]
        if self.polarity == 'light':
            self.scaled_data[max_index] = 1
            if (self.adc_sensor_data[third_index] - self.adc_sensor_data[min_index]) > self.sensitivity:
                self.scaled_data[third_index] = 0
                self.scaled_data[min_index] = -1
            else:
                self.scaled_data[third_index] = 0
                self.scaled_data[min_index] = 0
        elif self.polarity == 'dark':
            self.scaled_data[max_index] = -1
            if (self.adc_sensor_data[third_index] - self.adc_sensor_data[min_index]) > self.sensitivity:
                self.scaled_data[third_index] = 0
                self.scaled_data[min_index] = 1
            else:
                self.scaled_data[third_index] = 0
                self.scaled_data[min_index] = 0
        return self.scaled_data
        
    def sensor_processing(self, scaled_data):
        scaled_data = self.scaling(scaled_data)
        if (scaled_data[0] == 0 and scaled_data[1] == 0 and scaled_data[2] == 0): # No line found
            self.move_left()
        

        # Robot is towards right so move left
        elif (scaled_data[0] == 1 and scaled_data[1] == 0 and scaled_data[2] == 0): 
            picarx_improved.set_dir_servo_angle(-20)
            time.sleep(0.6)
            picarx_improved.forward(40)
            time.sleep(0.2)
            picarx_improved.stop()

        # Robot is centered
        elif (scaled_data[0] == 0 and scaled_data[1] == 1 and scaled_data[2] == 0):
            picarx_improved.set_dir_servo_angle(0)
            time.sleep(0.6)
            picarx_improved.forward(40)
            time.sleep(0.2)
            picarx_improved.stop()

        # Robot is towards left so move right
        elif (scaled_data[0] == 0 and scaled_data[1] == 0 and scaled_data[2] == 1):
            picarx_improved.set_dir_servo_angle(20)
            time.sleep(0.6)
            picarx_improved.forward(40)
            time.sleep(0.2)
            picarx_improved.stop()

        # Robot is towards slightly right so move left
        elif (scaled_data[0] == 1 and scaled_data[1] == 1 and scaled_data[2] == 0):
            picarx_improved.set_dir_servo_angle(-10)
            time.sleep(0.6)
            picarx_improved.forward(20)
            time.sleep(0.2)
            picarx_improved.stop()

        # No line found
        elif (scaled_data[0] == 1 and scaled_data[1] == 0 and scaled_data[2] == 1):
            self.find_line()

        
        # Robot is towards slightly left so move right
        elif (scaled_data[0] == 0 and scaled_data[1] == 1 and scaled_data[2] == 1):
            picarx_improved.set_dir_servo_angle(10)
            time.sleep(0.6)
            picarx_improved.forward(20)
            time.sleep(0.2)
            picarx_improved.stop()
            
        else:
            self.find_line()

    
    def move_left(self):
        num1 = random.rand
        if num1 < 0.5:
            picarx_improved.set_dir_servo_angle(20)
            time.sleep(0.6)
            picarx_improved.forward(40)
            time.sleep(0.2)
            picarx_improved.stop()
        else:
            picarx_improved.set_dir_servo_angle(-20)
            time.sleep(0.6)
            picarx_improved.forward(40)
            time.sleep(0.2)
            picarx_improved.stop()



if __name__ == '__main__':
    adc_data = Sensor
    adc_sensor_data = adc_data.sensor_reading()
    processor = Interpreter
    discrete_data = processor.sensor_processing(adc_sensor_data)