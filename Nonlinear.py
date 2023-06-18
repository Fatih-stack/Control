##################################################################
## function definition

def forward_difference_solver(t_initial, t_final, dt, initial_cond, system_coef_x, system_coef_u, u):

    x_var = np.arange(t_initial, t_final, dt)
    x_var[0] = initial_cond

    for k in range(0, int((t_final - t_initial)/dt) - 1):
        x_var[k+1] = x_var[k] + dt*(system_coef_x*x_var[k]*x_var[k] + system_coef_u*u[k])

    return x_var


def backward_difference_solver(t_initial, t_final, dt, initial_cond, system_coef_x, system_coef_u, u):

    x_var = np.arange(t_initial, t_final, dt)
    x_var[0] = initial_cond

    for k in range(1, int((t_final - t_initial)/dt)):
        x_var[k] = x_var[k-1] + dt*(system_coef_x*x_var[k-1]*x_var[k-1] + system_coef_u*u[k-1])

    return x_var
    

def centered_difference_solver(t_initial, t_final, dt, initial_cond, initial_cond_sec, system_coef_x, system_coef_u, u):
    
    x_var = np.arange(t_initial, t_final, dt)

    x_var[0] = initial_cond
    x_var[1] = initial_cond_sec

    for k in range(1, int((t_final - t_initial)/dt)-1):
        x_var[k+1] = x_var[k-1] + 2*dt*(system_coef_x*x_var[k-1]*x_var[k-1] + system_coef_u*u[k-1])

    return x_var

#####################################################################################

#####################################################################################
##main code
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

dt = 0.0001

t_initial = 0.0
t_final = 3.0

#initial condition
x_0 = 10

#Data for plotting
t = np.arange(t_initial, t_final, dt)
x = np.arange(t_initial, t_final, dt)

u = np.arange(int(t_final - t_initial)/dt)

for k in range(0, int((t_final - t_initial)/dt)):
    u[k] = 0

x[0] = x_0
x[1] = x_0 + (-5)*dt*x_0*x_0/5

a = -5
b = 1/2

#x = forward_difference_solver(t_initial, t_final, dt, x_0, a, b, u)
#x = backward_difference_solver(t_initial, t_final, dt, x_0, a, b, u) 
x = centered_difference_solver(t_initial, t_final, dt, x_0, x_0+(-5*dt*x_0*x_0/5), a, b, u)

#showing graph related to differential equation

plt.figure()

plt.subplot(211)
plt.plot(t,x,'r')
plt.ylabel('Meter (m)')
plt.grid(True)
plt.title('Difference')

plt.subplot(212)
plt.plot(t,u,'r')
plt.ylabel('Input (F)')
plt.grid(True)
plt.xlabel('Time (sec)')

plt.show()
