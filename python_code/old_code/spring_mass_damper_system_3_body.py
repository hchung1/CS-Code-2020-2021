#Name: Henry Chung
#Date: 10-15-2020
#Class: CS 4350-5350 ST:HPC on Embedded Systems
#Instructor: Gil Gallegos, gil.gallegos@gmail.com
#TA: Christopher Torres, ctorre25@live.nmhu.edu

#Assignment: Simulate spring, mass, damper system

#Main()

# Python program to show time by process_time()
import numpy as np
import matplotlib.pyplot as mp
from time import perf_counter
from time import process_time

def repeats(value,size):
    temp = []
    for i in range(size):
        temp.append(value)
    return temp

## Constants
# Time Slice in Seconds (s), 0.1 = 0.1 of a second
dt = 0.001 # Step Size
time = 0.0 # Start Time
iteration = 15000 # Iteration

## Variables
# Individual Damping Coefficient, (N*s/m) [0,1,2,3,...,N]
c = [0.01, 0.01, 0.01, 0.01, 0.01]
# Individual Spring Constant, (N/m) [0,1,2,3,...,N]
k = [0.2, 0.175, 0.150, 0.125, 0.1]
# Object Mass, Kilograms (kg)
M = [1.0, 0.75, 0.5, 0.25, 0.01]

##Initial Conditions
# Location/Displacement, Meters (m)
x_initial = [0.0, 0.0, 0.1, 0.3, 0.5]

#Initial Position
x_old = [0,1,2,5,10]

# Initial Speed, Meters/Seconds (m/s)
x_dot_old = [0.0,0.0,0.0,0.0,0.0]

# Initial Memory
f = [0,0,0,0,0]
x_dot_new = [0,0,0,0,0]
x_new = [0,0,0,0,0]

# Length of Array
l = len(c) # Size of 5
for i in range(iteration):
    #define f(x,x_dot) = -1/M*(c*x_dot + k*x) --> acceleration, a_x
    f[0] = 1/M[0]*(k[1]*(x_old[1]-x_old[0])+c[1]*(x_dot_old[1]-x_dot_old[0])-k[0]*x_old[0]-c[0]*x_dot_old[0])
    for j in range(l-2):
        f[j+1] = 1/M[j+1]*(k[j+2]*(x_old[j+2]-x_old[j+1])+c[j+2]*(x_dot_old[j+2]-x_dot_old[j+1])-k[j+1]*(x_old[j+1]-x_old[j])-c[j+1]*(x_dot_old[j+1]-x_dot_old[j]))
    f[l-1] = 1/M[l-1]*(-k[l-1]*(x_old[i][l-1]-x_old[i][l-2])-c[l-1]*(x_dot_old[l-1]-x_dot_old[l-2]))
    #Calculate new velocity, x_dot_new
    for j in range(l):
        x_dot_new[j] = x_dot_old[j] + dt * f[j] # New Velocity, x_dot_new
        x_new[j] = x_old[j] + dt * x_dot_new[j] # New Position, x_new
        x_dot_old[j] = x_dot_new[j] # Replace Value
        x_old[i][j] = x_new[j] # Record Position
    
    # Increment Time
    time  = time + dt
    time_out.append(time)
    if i%100 ==0:
        #mp.scatter(x1_old,x1_dot_old)
        #mp.scatter(x2_old,x2_dot_old)
        #mp.scatter(x3_old,x3_dot_old)
        mp.scatter(time,x_old[0], color="red")
        mp.scatter(time,x_old[1], color="green")
        mp.scatter(time,x_old[2], color="blue")
        mp.scatter(time,x_old[3], color="black")
        mp.scatter(time,x_old[4], color="purple")
mp.show()
