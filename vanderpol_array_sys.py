#################################################################################
#################################################################################
## function definition

def forward_difference_solver(t_initial, t_final, dt, A, mu, state_number, init_cond_1, init_cond_2):

    length_of_loop = int((t_final - t_initial)/dt)
    
    tru = np.arange(length_of_loop*state_number, dtype=float).reshape(length_of_loop, state_number)

    # initial condition assignment
    tru[0,0] = init_cond_1
    tru[0,1] = init_cond_2

    for i in range(0, length_of_loop - 1):
        # A matrix definition
        A[0,0] = 1
        A[0,1] = dt
        A[1,0] = -dt
        A[1,1] = dt*mu*(1 - tru[i,0]*tru[i,0]) + 1
        tru[i+1,:] = A.dot(np.transpose(tru[i,:])).flatten()
        
    return tru;

#################################################################################
#################################################################################
## main code

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# define sampling period
dt = 0.001

t_initial = 0.0
t_final = 20.0

length_of_loop = int((t_final - t_initial)/dt)

# time parameter
t = np.arange(t_initial, t_final, dt, dtype=float)

# initial condition
z1_0 = 2
z2_0 = 0

# define input variable
u = np.arange(t_initial,t_final,dt,dtype=float)

for i in range(0, length_of_loop):
    u[i] = 10

# define specific size for system matrices
row_a = 2
column_a = 2

A = np.arange(row_a*column_a,dtype=float).reshape(row_a,column_a)

# system parameters
mu = 0.1

# system variables
state_number = column_a

tru_forward = forward_difference_solver(t_initial, t_final, dt, A, mu, state_number, z1_0, z2_0)

plt.figure()

plt.plot(t,tru_forward[:,0],'r')
plt.plot(t,tru_forward[:,1],'b')
plt.ylabel('Position/Velocity')
plt.xlabel('Time (Sec)')
plt.grid(True)
plt.title('Vanderpol System')

plt.show()











