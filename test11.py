from picarx_improved import picarx_improved
from time import sleep

picarx_improved.set_dir_servo_angle(0)

picarx_improved.forward(20)
sleep(1)
#        picarx_improved.backward(50)
picarx_improved.stop()
