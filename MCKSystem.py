####################################################################################
##include library
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


####################################################################################
## plotting data

def plot_func(tru_centered, t, title_f, ylabel_f, xlabel_f):

    plt.figure()

    # for adding data 
    plt.plot(t, tru_centered, 'r')
    plt.xlabel(xlabel_f)
    plt.ylabel(ylabel_f)
    plt.grid(True)
    plt.title(title_f)

    plt.show()

####################################################################################
## difference solver function

def centered_difference_solver(t_initial, t_final, dt, f_x_pre, f_x_now, f_x_fut, x_0, x_dot_0):

    length_of_loop = int((t_final - t_initial)/dt)

    tru = np.arange(t_initial, t_final, dt, dtype=float)

    #initial condition assignment
    tru[0] = x_0
    tru[1] = tru[0] + x_dot_0*dt

    for i in range(1, length_of_loop - 1):
         tru[i+1] = (tru[i]*f_x_now + tru[i-1]*f_x_pre)/f_x_fut

    return tru

####################################################################################
## main function

def main():
    # define sampling period
    dt = 0.001

    t_initial = 0.0
    t_final = 10.0

    # initial condition
    x_0 = 10
    x_dot_0 = 5

    length_of_loop = int((t_final - t_initial)/dt)

    t = np.arange(t_initial, t_final, dt, dtype=float)

    # define system parameters
    f_x_fut = (1/(dt*dt) + 3/(2*dt))
    f_x_now = (2/(dt*dt) - 2)
    f_x_pre = (3/(2*dt) - 1/(dt*dt))

    system_setting_parameters = [t_initial, t_final, dt, 
                                f_x_pre, f_x_now, f_x_fut, 
                                x_0, x_dot_0, t]

    return system_setting_parameters

if __name__ == "__main__":
    system_parameters_main = main()
    tru_centered = centered_difference_solver(system_parameters_main[0],
                                              system_parameters_main[1],
                                              system_parameters_main[2],
                                              system_parameters_main[3],
                                              system_parameters_main[4],
                                              system_parameters_main[5],
                                              system_parameters_main[6],
                                              system_parameters_main[7])
                                              
    t = system_parameters_main[8]

    plot_func(tru_centered, t, "MCK Second Order System",
                "Position (m)", "Time (sec)")