import picarx_improved
import time

def parallel_park(park_dir):
    picarx_improved.set_dir_servo_angle(0)
#    for i in range(500):
#            picarx_improved.forward(30)
#    time.sleep(2)

    if park_dir == 'left':
        picarx_improved.set_dir_servo_angle(-30)
    else:
        picarx_improved.set_dir_servo_angle(30)

    time.sleep(2)
    for i in range(500):
          picarx_improved.forward(30)

#    if park_dir == 'left':
#        picarx_improved.set_dir_servo_angle(30)
#    else:
#        picarx_improved.set_dir_servo_angle(-30)

#    for i in range(500):
#        picarx_improved.backward(30)

#    picarx_improved.set_dir_servo_angle(0) 

#    for i in range(500):
#        picarx_improved.forward(30)

    picarx_improved.stop()

if __name__ == "__main__":
    parallel_park('left')
