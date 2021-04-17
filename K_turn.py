from picarx_improved import picarx_improved
import time

def k_turn(u_turn):
    angle1= 35
    power1 = 20

    if u_turn  == 'left':
        picarx_improved.set_dir_servo_angle(-angle1)
    else:
        picarx_improved.set_dir_servo_angle(angle1)

    picarx_improved.forward(power1)
    time.sleep(1)

    if u_turn  == 'left':
        picarx_improved.set_dir_servo_angle(angle1)
    else:
        picarx_improved.set_dir_servo_angle(-angle1)

    picarx_improved.backward(power1)
    time.sleep(1)

    if u_turn  == 'right':
        picarx_improved.set_dir_servo_angle(angle1-5)
    else:
        picarx_improved.set_dir_servo_angle(-angle1+5)

    picarx_improved.forward(power1+5)
    time.sleep(1)

    picarx_improved.set_dir_servo_angle(0)
    picarx_improved.forward(power1)
    time.sleep(1)
    picarx_improved.stop()

if __name__ == "__main__":
    k_turn('right')
