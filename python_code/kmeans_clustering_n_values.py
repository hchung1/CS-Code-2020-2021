#Name: Henry Chung
#Class: CS 4740-5740 Machine Learning Algorithms
#Instructor: Gil Gallegos, gil.gallegos@gmail.com
#TA: Patrik Boloz, pboloz@live.nmhu.edu

#Assignment: K-means Clustering (2-D)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Main()
class K_Means_Cluster():
    def __init__(self, iteration, data, centroids):
        self.iteration = iteration # Iteration
        self.data = data # x&y
        self.centroids = centroids # Centroids
        try:
            self.c_distance = np.zeros((data.shape[0],2,centroids.shape[0])) #X&Y Distance Between Two Centroids, R(10,2,2) -> (sample, x&y, number of centroids)
            self.o_distance = np.zeros((data.shape[0],centroids.shape[0])) # Distance between Coordinates
        except:
            print ("Error in K_Means_Cluster(iteration,data,centroids)")
            print ("data and centroids needs to be a numpy array.")
        self.sorting = []
        for i in range(centroids.shape[0]):
            self.sorting.append([]) # Create Memory for Each Centroids
    def euclidean_distance(self, i, j): #Use Triangle Formula to find Distance
        #Find Difference of Coordinates
        self.c_distance[i,0,j] = self.centroids[j,0]-self.data[i,0] # Centroid X-Axis minus Sample X-Axis
        self.c_distance[i,1,j] = self.centroids[j,0]-self.data[i,0] # Centroid Y-Axis minus Sample Y-Axis
        #Find Distance Between Points, r = (x**2 + y**2)**0.5
        self.o_distance[i,j] = np.sqrt((self.c_distance[i,0,j]**2)+(self.c_distance[i,1,j]**2))
    def plot_relations(self, i, k, name = ""):
        try:
            data = np.array(self.sorting[i])
            plt.scatter(data[:,0],data[:,1],color='red', label="Samples"); # Points
        except:
            print ("This " + str(i) + " does not have any related data added to it.")
        centroid = self.centroids[i]
        plt.scatter(centroid[0], centroid[1],color='green', label="Centroid_"+str(i)); # Centroids
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title("Related Sample Plots of Centroid " + str(i))
        if name == "":
            plt.savefig("image/" + str(k) + "_Kmeans_Cluster_Centroid_" + str(i))
        else:
            plt.savefig(name)
        plt.close()
    def plot_all(self, i, k, name = ""):
        for i in range(len(self.sorting)):
            try:
                temp = np.array(self.sorting[i])
                plt.scatter(temp[:,0],temp[:,1],color='red', label="Samples"); # Points
            except:
                print ("This " + str(i) + " does not have any related data added to it.")
        plt.scatter(self.centroids[:,0], self.centroids[:,1],color='green', label="Centroids"); # Centroids
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title("All Sample Plots and Centroids")
        if name == "":
            plt.savefig("image/All_KMeans_Cluster_" + str(k))
        else:
            plt.savefig(name)
        plt.close()
    def run(self):
        for k in range(self.iteration):
            counts = np.zeros(self.centroids.shape[0]) # Counter, R(1,2)
            for i in range(self.data.shape[0]):
                for j in range(self.centroids.shape[0]):
                    self.euclidean_distance(i,j)
            # Find the Minimum Index
            index = np.argmin(self.o_distance, axis=1) # Find the Location of the Minimal Value in Each Row, R(10,1)
            #print (index)
            # List the Coordinates for the Closest Centroids
            for i in range(self.data.shape[0]):
                self.sorting[index[i]].append(list(self.data[i])) # Place Sample Coordinates in Closest Centroids Coordinates
                
            # Change the Location of the Existing Centroids 
            for i in range(self.centroids.shape[0]): # Number of Centroids
                try:
                    self.centroids[i,0] = np.sum(np.array(self.sorting[i])[:,0])/len(self.sorting[i]) # Average Distance of Sample Data X-Axis
                    self.centroids[i,1] = np.sum(np.array(self.sorting[i])[:,1])/len(self.sorting[i]) # Average Distance of Sample Data Y-Axis
                except:
                    pass # self.sorting is empty
            for i in range(self.centroids.shape[0]):
                self.plot_relations(i, k) # (data, centroid, centroid number, iteration)
            self.plot_all(i, k) # (data, centroid, centroid number, iteration)

