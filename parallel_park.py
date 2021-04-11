import picarx_improved
import picarx_improved.py

def parallel_park(park_dir):
    picarx_improved.set_dir_servo_angle(0) 
    for i in range(2000):
            picarx_improved.forward(30)

    if park_dir == 'left':
        picarx_improved.set_dir_servo_angle(-45)
    else:
        picarx_improved.set_dir_servo_angle(45)

    for i in range(2000):
          picarx_improved.backward(30)

    if park_dir == 'left':
        picarx_improved.set_dir_servo_angle(45)
    else:
        picarx_improved.set_dir_servo_angle(-45)

    for i in range(2000):
        picarx_improved.backward(30)

    picarx_improved.set_dir_servo_angle(0) 

    for i in range(1000):
        picarx_improved.forward(30)

    picarx_improved.stop()