###############################################################
#main

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# defining sampling period
dt = 0.001

t_initial = 0.0
t_final = 15.0

# initial condition
x_0 = 0
v_0 = 0

# creating array for variables
t = np.arange(t_initial, t_final, dt)
x_t_f = np.arange(t_initial, t_final, dt)
v_t_f = np.arange(t_initial, t_final, dt)

# define input variable

u = np.arange(t_initial, t_final, dt)

for i in range(0, int((t_final - t_initial)/dt)):
    u[i] = np.sin(2*np.pi*1*t[i])

#system parameters
m = 1
c = 2
k = 1

#implementation of forward difference for MCK

for i in range(0, int((t_final - t_initial)/dt) - 1):
    x_t_f[i+1] = x_t_f[i] + dt*(v_t_f[i])
    v_t_f[i+1] = v_t_f[i] + dt*(-k/m*x_t_f[i] - c/m*v_t_f[i] + u[i]/m)


#showing graph related to MCK system

plt.figure()

plt.subplot(311)
plt.plot(t,x_t_f,'r')
plt.ylabel('Position (m)')
plt.grid(True)
plt.title('MCK System')

plt.subplot(312)
plt.plot(t,v_t_f,'r')
plt.ylabel('Velocity (m/sn)')
plt.grid(True)

plt.subplot(313)
plt.plot(t, u,'r')
plt.ylabel('Input (N)')
plt.grid(True)
plt.xlabel('Time (sec)')

plt.show()
#main
###############################################################