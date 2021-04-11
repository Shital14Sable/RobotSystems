import picarx_improved
# from time import sleep

picarx_improved.set_dir_servo_angle(-45)


for i in range(20000):
        picarx_improved.forward(20)

#        picarx_improved.backward(50)
picarx_improved.stop()
