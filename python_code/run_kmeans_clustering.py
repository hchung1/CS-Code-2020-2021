from kmeans_clustering_n_values import K_Means_Cluster
import numpy as np
import matplotlib.pyplot as plt


# Show the Unmodified Graph of the Centroids and Samples
def show_plot(x,x_c, name = "KMeans_Clustering_Initial_Plot"):
    plt.scatter(x[:,0],x[:,1],color='red', label="Samples"); # Points
    plt.scatter(x_c[:,0], x_c[:,1],color='green', label="Centroids"); # Centroids
    plt.title("Plot Display")
    plt.legend()
    plt.savefig(name)
    plt.close()

#### Keep Results Consistent
np.random.seed(3) # Random Seed

#### Important Constants
iteration = 10 # Number of Loops
sample = 30 # Number of Samples
centroids = 7  # Number of Available Centroids

#### Generate Data Randomly
# Generate Sample Data Coordinates, R(10x2) -> (number of samples, x&y)
x = np.vstack((7 * np.random.random(sample) - 5, 8 * np.random.random(sample) - 3)).T
#print(x)

# Generate Centroids Coordinates x_c, R(2,2) -> (number of centroids, x&y)
x_c = np.vstack((7 * np.random.random(centroids) - 5, 8 * np.random.random(centroids) - 3)).T
#print (x_c)

#### Show the Original Plot
show_plot(x,x_c, name = "image/Kmeans_Clustering_Initial")

#### Run Class
temp = K_Means_Cluster(iteration, x, x_c) # Call Class
temp.run() # Run Data
