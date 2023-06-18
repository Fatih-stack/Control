####################################################################
## main code
import ctypes
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time



######################################################################
# function definition

## plot definition
def plot_func(tru_centered, x_reference, t, title_f, ylabel_f, xlabel_f):

    user32 = ctypes.windll.user32

    screen_s_width = user32.GetSystemMetrics(0)
    screen_s_height = user32.GetSystemMetrics(1)

    plt.figure(figsize=(int(screen_s_width)/200, int(screen_s_height)/200))

    # for adding data
    plt.plot(t, tru_centered, 'r')
    plt.plot(t, x_reference, 'b')
    plt.ylabel(ylabel_f)
    plt.xlabel(xlabel_f)
    plt.grid(True)
    plt.title(title_f)

    plt.show()

## solver definition
def centered_difference_solver(t_initial, t_final, dt, f_x_pre, f_x_now, f_x_fut, x_0, x_dot_0, x_ref):

    length_of_loop = int((t_final - t_initial)/dt)

    tru = np.arange(t_initial, t_final, dt, dtype=float)
    F = np.arange(t_initial, t_final, dt, dtype=float)
    e = np.arange(t_initial, t_final, dt, dtype=float)

    #initial condition assignment
    tru[0] = x_0
    tru[1] = tru[0] + x_dot_0*dt
    
    Ae = 0.5

    for i in range(1, length_of_loop - 1):
        #controller design
        e[i] = x_ref[i] - tru[i]
        C1 = x_ref[i+1] - (tru[i]*f_x_now + tru[i-1]*f_x_pre)/f_x_fut
        F[i] = f_x_fut*(C1 - Ae*e[i])
        tru[i+1] = (tru[i]*f_x_now + tru[i-1]*f_x_pre + F[i])/f_x_fut

    return tru
# function definition
######################################################################



######################################################################
## main

def main():
    #defining sampling period
    dt = 0.001

    t_initial = 0.0
    t_final = 10.0

    length_of_loop = int((t_final - t_initial)/dt)

    # time array
    t = np.arange(t_initial, t_final, dt,dtype=float)

    #initial condition
    x_0 = 2
    x_dot_0 = 0

    #define input variable
    f = 0.1
    x_ref = 5 + np.sin(2*np.pi*f*t)

    #system parameter constants
    f_x_pre = (3/(2*dt) - 1/(dt*dt))
    f_x_now = (2/(dt*dt) - 2)
    f_x_fut = (1/(dt*dt) + 3/(2*dt))

    system_settings_parameters = [t_initial, t_final, dt, 
                                f_x_pre, f_x_now, f_x_fut, 
                                x_0, x_dot_0, x_ref, t]

    return system_settings_parameters

## main
######################################################################


if __name__ == "__main__":
    system_parameters_main = main()
    tru_centered = centered_difference_solver(system_parameters_main[0],system_parameters_main[1],
                                            system_parameters_main[2],system_parameters_main[3],
                                            system_parameters_main[4],system_parameters_main[5],
                                            system_parameters_main[6],system_parameters_main[7],
                                            system_parameters_main[8])

    t = system_parameters_main[9]
    x_reference = system_parameters_main[8]

    plot_func(tru_centered, x_reference, t, "MCK Controller Response", "Position (m)", "Time (sec)")