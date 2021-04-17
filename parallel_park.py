import picarx_improved
import time

def parallel_park(park_dir):
#    picarx_improved.set_dir_servo_angle(0)
    picarx_improved.forward(50)
    time.sleep(0.6)
    angle1= 26
    power1 = 18

    if park_dir == 'right':
        picarx_improved.set_dir_servo_angle(angle1-6)
    else:
        picarx_improved.set_dir_servo_angle(-angle1+6)

    picarx_improved.backward(power1)
    time.sleep(1)

    if park_dir == 'right':
        picarx_improved.set_dir_servo_angle(-angle1-6)
    else:
        picarx_improved.set_dir_servo_angle(angle1+6)

    picarx_improved.backward(power1)
    time.sleep(1)

    picarx_improved.set_dir_servo_angle(0)
    picarx_improved.forward(50)
    time.sleep(0.3)
    picarx_improved.stop()

if __name__ == "__main__":
    parallel_park('right')
