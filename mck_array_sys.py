####################################################################
## main code

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#defining sampling period
dt = 0.001

t_initial = 0.0
t_final = 20.0

length_of_loop = int((t_final - t_initial)/dt)

# time array
t = np.arange(t_initial, t_final, dt,dtype=float)

#initial condition
x_0 = 0
v_0 = 0

#define input variable
u = np.arange(t_initial, t_final, dt, dtype=float)

for i in range(0,length_of_loop):
    u[i] = 10

# define specific size for system matrices

row_a = 2
column_a = 2

row_b = 2
column_b = 1

A = np.arange(row_a*column_a, dtype=float).reshape(row_a, column_a)
B = np.arange(row_b*column_b, dtype=float).reshape(row_b, column_b)

# system matrices - assigning data m,c,k
m = 1
c = 2
k = 1

# create A matrix
A[0,0] = 1
A[0,1] = dt
A[1,0] = -k*dt/m
A[1,1] = (1 - c*dt/m)

# create B matrix
B[0,0] = 0
B[1,0] = dt/m

# system variables

state_number = 2 #column_a

tru = np.arange(length_of_loop*state_number,dtype=float).reshape(length_of_loop,state_number)

#initial condition
tru[0,0] = x_0
tru[0,1] = v_0

##################forward difference ########################################################

for i in range(0, length_of_loop - 1):
    tru[i+1,:] = A.dot(np.transpose(tru[i,:])).flatten() + B.dot(u[i]).flatten()

# showing graph...
plt.figure()

plt.plot(t, tru[:,0], 'r')
plt.plot(t, tru[:,1], 'b')
plt.ylabel('States')
plt.grid(True)
plt.title('MCK System with Array')

plt.show()

## main code
######################################################################