import time
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

import atexit
import numpy as np 
import time
import logging
from logdecorator import log_on_start , log_on_end , log_on_error

logging_format = "%(asctime)s:%(message)s"
logging.basicConfig(format=logging_format, level = logging.INFO, datefmt ="% H:%M:%S")
logging.getLogger().setLevel(logging.DEBUG)


class picarx_improved:

    def __init__(self):
        self.PERIOD = 4095
        self.PRESCALER = 10
        self.TIMEOUT = 0.02

        self.dir_servo_pin = Servo(PWM('P2'))
        self.camera_servo_pin1 = Servo(PWM('P0'))
        self.camera_servo_pin2 = Servo(PWM('P1'))
        self.left_rear_pwm_pin = PWM("P13")
        self.right_rear_pwm_pin = PWM("P12")
        self.left_rear_dir_pin = Pin("D4")
        self.right_rear_dir_pin = Pin("D5")

        self.S0 = ADC('A0')
        self.S1 = ADC('A1')
        self.S2 = ADC('A2')

        self.str_angle = 0
        self.Servo_dir_flag = 1
        self.dir_cal_value = 0
        self.cam_cal_value_1 = 0
        self.cam_cal_value_2 = 0
        self.motor_direction_pins = [left_rear_dir_pin, right_rear_dir_pin]
        self.motor_speed_pins = [left_rear_pwm_pin, right_rear_pwm_pin]
        self.cali_dir_value = [1, -1]
        self.cali_speed_value = [0, 0]
        #初始化PWM引脚
        for pin in motor_speed_pins:
            pin.period(PERIOD)
            pin.prescaler(PRESCALER)


    def set_motor_speed(self, motor, speed):
        global cali_speed_value,cali_dir_value
        motor -= 1
        
        if speed >= 0:
            direction = 1 * cali_dir_value[motor]
        elif speed < 0:
            direction = -1 * cali_dir_value[motor]
        speed = abs(speed)
        # if speed != 0:
        #     speed = int(speed /2 ) + 50
        # speed = speed - cali_speed_value[motor]
        if direction < 0:
            motor_direction_pins[motor].high()
            motor_speed_pins[motor].pulse_width_percent(speed)
        else:
            motor_direction_pins[motor].low()
            motor_speed_pins[motor].pulse_width_percent(speed)

    def motor_speed_calibration(self, value):
        global cali_speed_value,cali_dir_value
        cali_speed_value = value
        if value < 0:
            cali_speed_value[0] = 0
            cali_speed_value[1] = abs(cali_speed_value)
        else:
            cali_speed_value[0] = abs(cali_speed_value)
            cali_speed_value[1] = 0

    def motor_direction_calibration(self, motor, value):
        # 0: positive direction
        # 1:negative direction
        global cali_dir_value
        motor -= 1
        if value == 1:
            cali_dir_value[motor] = -1*cali_dir_value[motor]


    def dir_servo_angle_calibration(self, value):
        global dir_cal_value
        dir_cal_value = value
        set_dir_servo_angle(dir_cal_value)
        # dir_servo_pin.angle(dir_cal_value)

    def set_dir_servo_angle(self, value):
        global str_angle
        global dir_cal_value
        dir_servo_pin.angle(value+dir_cal_value)
        str_angle = value

    def camera_servo1_angle_calibration(self, value):
        global cam_cal_value_1
        cam_cal_value_1 = value
        set_camera_servo1_angle(cam_cal_value_1)
        # camera_servo_pin1.angle(cam_cal_value)

    def camera_servo2_angle_calibration(self, value):
        global cam_cal_value_2
        cam_cal_value_2 = value
        set_camera_servo2_angle(cam_cal_value_2)
        # camera_servo_pin2.angle(cam_cal_value)

    def set_camera_servo1_angle(self, value):
        global cam_cal_value_1
        camera_servo_pin1.angle(-1 *(value+cam_cal_value_1))

    def set_camera_servo2_angle(self, value):
        global cam_cal_value_2
        camera_servo_pin2.angle(-1 * (value+cam_cal_value_2))

    def get_adc_value(self):
        adc_value_list = []
        adc_value_list.append(S0.read())
        adc_value_list.append(S1.read())
        adc_value_list.append(S2.read())
        return adc_value_list

    def radius_calculator(self, theta, speed):
        B = 11.7*0.3  # cm
        L = 9.4*0.3  # cm
        if theta == 0:
            V_in = speed
            V_out = speed
        else:
            R = L*(1/np.tan(theta))
            V_in = speed*(R-(B/2))
            V_out = speed*(R+(B/2))

        if abs(V_in) < 15:
            V_in = 15
        if abs(V_out) < 15 :
            V_out =  15
        
        
        if abs(V_in) > 100:
            V_in = 100
        if abs(V_out) > 100 :
            V_out =  100


        return abs(V_in), abs(V_out)

    def set_power(self, speed):
        global str_angle
        theta = str_angle
        V_in, V_out = radius_calculator(theta, speed)
        if theta >= 0:
            set_motor_speed(1, V_in)
            set_motor_speed(2, V_out)
        else:
            set_motor_speed(1, V_out)
            set_motor_speed(2, V_in)

    def backward(self, speed):
        global str_angle
        theta = str_angle
        V_in, V_out = radius_calculator(theta, speed)
        if theta >= 0:
            set_motor_speed(1, V_in)
            set_motor_speed(2, V_out)
        else:
            set_motor_speed(1, V_out)
            set_motor_speed(2, V_in)
    #    set_motor_speed(1, speed)
    #    set_motor_speed(2, speed)

    def forward(self, speed):
        global str_angle
        theta = str_angle
        V_in, V_out = radius_calculator(theta, speed)
        if theta <= 0:
            set_motor_speed(1, -V_in)
            set_motor_speed(2, -V_out)
        else:
            set_motor_speed(1, -V_out)
            set_motor_speed(2, -V_in)
    
    #    set_motor_speed(1, -1*speed)
    #    set_motor_speed(2, -1*speed)


    def stop(self):
        set_motor_speed(1, 0)
        set_motor_speed(2, 0)


    def Get_distance(self):
        timeout=0.01
        trig = Pin('D8')
        echo = Pin('D9')

        trig.low()
        time.sleep(0.01)
        trig.high()
        time.sleep(0.000015)
        trig.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while echo.value()==0:
            pulse_start = time.time()
            if pulse_start - timeout_start > timeout:
                return -1
        while echo.value()==1:
            pulse_end = time.time()
            if pulse_end - timeout_start > timeout:
                return -2
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        #print(cm)
        return cm
        
    def test(self):
        # dir_servo_angle_calibration(-10) 
        set_dir_servo_angle(-40)
        # time.sleep(1)
        # set_dir_servo_angle(0)
        # time.sleep(1)
        # set_motor_speed(1, 1)
        # set_motor_speed(2, 1)
        # camera_servo_pin.angle(0)

    atexit.register(stop)
    # if __name__ == "__main__":
    #     try:
    #         # dir_servo_angle_calibration(-10) 
    #         while 1:
    #             test()
    #     finally: 
    #         stop()
