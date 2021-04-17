
import parallel_park
import K_turn
import picarx_improved
import time

def maneuver_func(val):
    if val == 'Park':
       parallel_park.parallel_park('right')
    elif val == 'Turn':
       K_turn.k_turn('left')

if __name__ =='__main__':
    while True:
       val = input("Enter the type of Maneuver(Park or Turn): ")
       if val == 'Park' or val == 'Turn':
          maneuver_func(val)
       else:
          break
