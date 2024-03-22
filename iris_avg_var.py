import pandas as pd
import numpy
import sys


tmp_list=[]
all_avg_list=[]
all_var_list=[]
setosa_avg_list=[]
setosa_var_list=[]
versicolor_avg_list=[]
versicolor_var_list=[]
virginica_avg_list=[]
virginica_var_list=[]
sum=0.0
# URL에서 데이터 다운로드
iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)

# 열 이름 설정
iris_data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "iris_class"]

# NumPy 배열로 변환
iris_matrix = iris_data.values

# 결과 출력

for i in range(len(iris_matrix[0])-1):
    for j in range(len(iris_matrix)):
        sum += float(iris_matrix[j][i])
        tmp_list.append(iris_matrix[j][i])
    all_avg_list.append(round(sum/150,2))
    all_var_list.append(round(numpy.var(tmp_list)))
    sum=0.0
    tmp_list=[]

for i in range(len(iris_matrix[0])-1):
    for j in range(0,49):
        sum += float(iris_matrix[j][i])
        setosa_var_list.append(iris_matrix[j][i])
    setosa_avg_list.append(round(sum/50,2))
    sum=0.0

for i in range(len(iris_matrix[0])-1):
    for j in range(50,99):
        sum += float(iris_matrix[j][i])
        versicolor_var_list.append(iris_matrix[j][i])
    versicolor_avg_list.append(round(sum/50,2))
    sum=0.0

for i in range(len(iris_matrix[0])-1):
    for j in range(100,149):
        sum += float(iris_matrix[j][i])
        virginica_var_list.append(iris_matrix[j][i])
    virginica_avg_list.append(round(sum/50,2))
    sum=0.0
    
print("Iris 데이터 행렬:")
print(iris_matrix)
print("평균: ",all_avg_list)
print("분산: ", round(numpy.var(all_var_list),2))
print("setosa avg: ",setosa_avg_list)
print("setosa var: ", round(numpy.var(setosa_var_list),2))
print("versicolor avg: ",versicolor_avg_list)
print("versicolor var: ",round(numpy.var(versicolor_var_list),2))
print("virginica avg: ",virginica_avg_list)
print("virginica var:", round(numpy.var(virginica_var_list),2))
