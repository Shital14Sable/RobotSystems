import picarx_improved

def parallel_park(park_dir):
    picarx_improved.set_dir_servo_angle(0) 
    for i in range(5000):
            picarx_improved.forward(50)
           

    if park_dir == 'left':
        picarx_improved.set_dir_servo_angle(-45)
    else:
        picarx_improved.set_dir_servo_angle(45)

    for i in range(5000):
          picarx_improved.backward(50)

    if park_dir == 'left':
        picarx_improved.set_dir_servo_angle(45)
    else:
        picarx_improved.set_dir_servo_angle(-45)

    for i in range(5000):
        picarx_improved.backward(30)

    picarx_improved.set_dir_servo_angle(0) 

    for i in range(3000):
        picarx_improved.forward(30)

    picarx_improved.stop()

if __name__ == "__main__":
    parallel_park('left')
