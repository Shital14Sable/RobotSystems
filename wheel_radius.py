
def radius_calculator(theta, speed):
    B = 11.7  # cm
    L = 9.4  # cm
    R = L* (1/tan(theta))
    V_in = speed*(R-(B/2))
    V_out = speed*(R+(B/2))
    return V_in, V_out



