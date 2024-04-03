import numpy as np
import numpy
import sys
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

tmp_list=[]
setosa_avg_list=[]
setosa_tmp=[]
versicolor_avg_list=[]
versicolor_tmp=[]
virginica_avg_list=[]
virginica_tmp=[]

# URL에서 데이터 다운로드
iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)

# 열 이름 설정
iris_data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "iris_class"]

# NumPy 배열로 변환
iris_matrix = iris_data.values


for i in range(len(iris_matrix[0])-1):
    for j in range(0,50):
        sum += float(iris_matrix[j][i])
        setosa_tmp.append(iris_matrix[j][i])
    setosa_avg_list.append(round(sum/50,2))
    setosa_var_list.append(round(numpy.var(setosa_tmp),2))
    setosa_tmp=[]
    sum=0.0


for i in range(len(iris_matrix[0])-1):
    for j in range(50,100):
        sum += float(iris_matrix[j][i])
        versicolor_tmp.append(iris_matrix[j][i])
    versicolor_avg_list.append(round(sum/50,2))
    versicolor_var_list.append(round(numpy.var(versicolor_tmp),2))
    sum=0.0
    versicolor_tmp=[]

for i in range(len(iris_matrix[0])-1):
    for j in range(100,150):
        sum += float(iris_matrix[j][i])
        virginica_tmp.append(iris_matrix[j][i])
    virginica_avg_list.append(round(sum/50,2))
    virginica_var_list.append(round(numpy.var(virginica_tmp),2))
    sum=0.0
    virginica_tmp=[]

# Iris 데이터셋 로드
iris = load_iris()
X = iris.data
y = iris.target

# 3-means
kmeans_3 = KMeans(n_clusters=3, n_init=10)
kmeans_3.fit(X)
centroids_3 = kmeans_3.cluster_centers_
labels_3 = kmeans_3.labels_

# 2-means
kmeans_2 = KMeans(n_clusters=2, n_init=10)
kmeans_2.fit(X)
centroids_2 = kmeans_2.cluster_centers_
labels_2 = kmeans_2.labels_

# 시각화
fig, ax = plt.subplots(2, 2, figsize=(12, 12))

# 3-means 시각화
for i in range(3):
    ax[0, 0].scatter(X[y == i, 0], X[y == i, 1], label=f'Iris {i}', c=f'C{i}')
ax[0, 0].set_title('Actual Iris Species')
ax[0, 0].set_xlabel('Sepal Length')
ax[0, 0].set_ylabel('Sepal Width')
ax[0, 0].legend()

for i in range(3):
    ax[0, 1].scatter(X[labels_3 == i, 0], X[labels_3 == i, 1], label=f'Cluster {i}', c=f'C{i}', marker='x')
ax[0, 1].scatter(centroids_3[:, 0], centroids_3[:, 1], marker='o', s=200, c='red', label='Centroids')
ax[0, 1].set_title('3-Means Clustering')
ax[0, 1].set_xlabel('Sepal Length')
ax[0, 1].set_ylabel('Sepal Width')
ax[0, 1].legend()

# 2-means 시각화
for i in range(3):
    ax[1, 0].scatter(X[y == i, 0], X[y == i, 1], label=f'Iris {i}', c=f'C{i}')
ax[1, 0].set_title('Actual Iris Species')
ax[1, 0].set_xlabel('Sepal Length')
ax[1, 0].set_ylabel('Sepal Width')
ax[1, 0].legend()

for i in range(2):
    ax[1, 1].scatter(X[labels_2 == i, 0], X[labels_2 == i, 1], label=f'Cluster {i}', c=f'C{i}', marker='x')
ax[1, 1].scatter(centroids_2[:, 0], centroids_2[:, 1], marker='o', s=200, c='red', label='Centroids')
ax[1, 1].set_title('2-Means Clustering')
ax[1, 1].set_xlabel('Sepal Length')
ax[1, 1].set_ylabel('Sepal Width')
ax[1, 1].legend()

plt.tight_layout()
plt.show()

print("Centroids for 3-Means:")
for i, centroid in enumerate(centroids_3):
    rounded_centroid = [round(coord, 2) for coord in centroid]
    print(f"Cluster {i}: {rounded_centroid}")

print("setosa avg: ",setosa_avg_list)
print("versicolor avg: ",versicolor_avg_list)
print("virginica avg: ",virginica_avg_list)


setosameans = []
versicolormeans = []
virginicameans = []


for i in range(4):
    setosameans.append(round(abs(setosa_avg_list[i] - centroids_3[0][i]),2))
    versicolormeans.append(round(abs(versicolor_avg_list[i] - centroids_3[1][i]),2))
    virginicameans.append(round(abs(virginica_avg_list[i] - centroids_3[2][i]),2))


print("Setosa means:", setosameans)
print("Versicolor means:", versicolormeans)
print("Virginica means:", virginicameans)


closest_centroids = []


for data_point in X:
    distances = [np.linalg.norm(data_point - centroid) for centroid in centroids_3]
    closest_centroid_index = np.argmin(distances)
    closest_centroids.append(closest_centroid_index)


for i in range(0, len(closest_centroids), 50):
    print(f"Closest {i+1} to {i+50}: {closest_centroids[i:i+50]}")



