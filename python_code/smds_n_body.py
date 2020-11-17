#Name: Henry Chung
#Date: 10-15-2020
#Class: CS 4350-5350 ST:HPC on Embedded Systems
#Instructor: Gil Gallegos, gil.gallegos@gmail.com
#TA: Christopher Torres, ctorre25@live.nmhu.edu

#Assignment: Simulate spring, mass, damper system

#Main()

# Python program to show time by process_time()
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter
from time import process_time

# Spring Mass Damper System Class
class smds():
    def __init__(self, x,M = 1,k = 0.2 ,c = 0.01):
        self.x_old = x # Initial Position
        self.c = c # Damping Coefficient, (N*s/m)
        self.k = k # Spring Constant, (N/m)
        self.M = M # Mass, (kg)
        # Constants
        self.x_dot_old=0
        self.f = 0
        self.x_new = 0
        self.x_dot_new = 0
        self.dt = 0.001 # Time Slice in Seconds, (s)
        self.N = 2000 # Iterations
        self.c_time = 0
        self.time = [0]
    #Populate Constants
    def repeats(self, value, size):
        temp = []
        for i in range(size): # Keep Similar Size Values
            temp.append(value) # Apply Constants to Array
        return temp


    def run(self, name="smds_1", colors=['red']):
        l = len(self.c)
        fig,ax = plt.subplots(3)
        plt.subplots_adjust( hspace=1)
        ax[0].set_title("Time vs. x_old")
        ax[1].set_title("x_old vs. x_dot_old")
        ax[2].set_title("Time vs. x_dot_old")
        ax[0].set_xlabel("Time (s)")
        ax[1].set_xlabel("x_old")
        ax[2].set_xlabel("Time (s)")
        ax[0].set_ylabel("x_old")
        ax[1].set_ylabel("x_dot_old")
        ax[2].set_ylabel("x_dot_old")
        for i in range(self.N):
            self.f[0] = -1/self.M[0]*(self.c[0]*self.x_dot_old[0] + self.k[0]*self.x_old[0][0])
            if (len(self.k) > 1):
                self.f[0] = 1/self.M[0]*\
                      (self.k[1]*(self.x_old[i][1]-self.x_old[i][0])+self.c[1]*(self.x_dot_old[1]-self.x_dot_old[0])-\
                      self.k[0]*self.x_old[i][0]-self.c[0]*self.x_dot_old[0])
                if (len(self.k) > 2):
                    for j in range(len(self.x_dot_new)-2): # Just Needs to Run Size 
                        self.f[j+1] = 1/self.M[j+1]*\
                                 (self.k[j+2]*(self.x_old[i][j+2]-self.x_old[i][j+1])+self.c[j+2]*(self.x_dot_old[j+2]-self.x_dot_old[j+1])-\
                                 self.k[j+1]*(self.x_old[i][j+1]-self.x_old[i][j])-self.c[j+1]*(self.x_dot_old[j+1]-self.x_dot_old[j]))
                self.f[l-1] = 1/self.M[l-1]*\
                         (-self.k[l-1]*(self.x_old[i][l-1]-self.x_old[i][l-2])-\
                         self.c[l-1]*(self.x_dot_old[l-1]-self.x_dot_old[l-2]))
            #Calculate new velocity, x_dot_new
            for j in range(l):
                self.x_dot_new[j] = self.x_dot_old[j] + self.dt * self.f[j] # New Velocity, x_dot_new
                self.x_new[j] = self.x_old[i][j] + self.dt * self.x_dot_new[j] # New Position, x_new
                self.x_dot_old[j] = self.x_dot_new[j] # Replace Value
                self.x_old[i+1][j] = self.x_new[j] # Record Position on Next Row
                
            # Increment Time
            self.c_time = self.c_time + self.dt
            self.time[i+1] = self.c_time # Don't replace initial value, 0
            if i%100 == 0:
                for j in range(l):
                    ax[0].scatter(self.c_time,self.x_new[j], color=colors[j%len(colors)])
                    ax[1].scatter(self.x_new[j],self.x_dot_new[j], color=colors[j%len(colors)])
                    ax[2].scatter(self.c_time,self.x_dot_new[j], color=colors[j%len(colors)])
        plt.savefig(name)
    def setup(self, time=2000, timestep=0.001):
        self.dt = timestep # Time Slice in Seconds, (s)
        self.N = time # Iterations
        try:
            size = len(self.x_old)
        except:
            size=1
        self.x_dot_old=self.repeats(self.x_dot_old,size)
        self.f = self.repeats(self.f,size)
        self.x_new = self.repeats(self.x_new,size)
        self.x_dot_new = self.repeats(self.x_dot_new,size)
        self.time = self.repeats(self.time,self.N+1)
        self.x_old = self.repeats(self.x_old,self.N+1)
        if (type(self.c) != list):
             self.c = self.repeats(self.c,size)
        if (type(self.k) != list):
             self.k = self.repeats(self.k,size)
        if (type(self.M) != list):
             self.M = self.repeats(self.M,size)

