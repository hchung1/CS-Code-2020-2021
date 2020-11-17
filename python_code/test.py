from smds_n_body import smds

#One Object SMDS
#Constants
x = [0.1] # Position
c = 0.00 # damping coefficient (N*s/m)
k = 0.1 # spring constant (N/m)
M = 0.1 # kilograms (kg)
# Run Functions
b = smds(x,M = M,k = k ,c = c)
b.setup()
b.run(name = "output/smds1")

#Two Object SMDS
#Constants
x = [0.0,0.1] # Position
c = 0.1 # damping coefficient (N*s/m)
k = [0.1,0.2] # spring constant (N/m)
M = 0.1 # kilograms (kg)
# Run Functions
b = smds(x,M = M,k = k ,c = c)
b.setup()
b.run(name = "output/smds2", colors = ['red', 'green'])

#Three Object SMDS
#Constants
x = [0.0,0.0,0.1] # Position
c = 0.1 # damping coefficient (N*s/m)
k = [0.1,0.2,0.3] # spring constant (N/m)
M = 0.1 # kilograms (kg)
# Run Functions
b = smds(x,M = M,k = k ,c = c)
b.setup()
b.run(name = "output/smds3", colors = ['red', 'green', 'blue'])

