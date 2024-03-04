from sklearn.metrics.pairwise import euclidean_distances
import numpy as np 
#[Height,Age,Weight]
x = np.array([[5,45,77],[5.11,26,47],[5.6,30,55],[5.9,34,59],[4.8,40,72],[5.8,36,60],[5.3,19,40],[5.8,28,60],[5.5,23,45],[5.6,32,58]])

# distance between X and the point
distance = euclidean_distances(x, [[5.5,38,55]])
print("S")
print(distance)
min=distance[0]
for i in distance:
    if i<min:
        min=i
print(min)
