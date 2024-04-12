import pandas as pd
import numpy
import sys
import numpy as np

up=0.0
down=0.0
#iris data의 분류를 위한 리스트 선언
tmp_list=[]
all_avg_list=[]
all_var_list=[]
setosa_avg_list=[]
setosa_tmp=[]
setosa_var_list=[]
versicolor_avg_list=[]
versicolor_tmp=[]
versicolor_var_list=[]
virginica_avg_list=[]
virginica_tmp=[]
virginica_var_list=[]
#iris data의 분류를 하되 30개씩 분류해서 정리한 리스트
setosa30_avg_list=[]
setosa30_var_list=[]
versicolor30_avg_list=[]
versicolor30_var_list=[]
virginica30_avg_list=[]
virginica30_var_list=[]
sum=0.0

# URL에서 데이터 다운로드
iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)

# 열 이름 설정
iris_data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "iris_class"]

# NumPy 배열로 변환
iris_matrix = iris_data.values


#iris data의 모든 데이터 평균 분산 구하는 for문
for i in range(len(iris_matrix[0])-1):
    for j in range(len(iris_matrix)):
        sum += float(iris_matrix[j][i])
        tmp_list.append(iris_matrix[j][i])
    all_avg_list.append(round(sum/150,2))
    all_var_list.append(round(numpy.var(tmp_list),2))
    sum=0.0
    tmp_list=[]
#setosa에 대한 평균 분산
for i in range(len(iris_matrix[0])-1):
    for j in range(0,50):
        sum += float(iris_matrix[j][i])
        setosa_tmp.append(iris_matrix[j][i])
    setosa_avg_list.append(round(sum/50,2))
    setosa_var_list.append(round(numpy.var(setosa_tmp),2))
    setosa_tmp=[]
    sum=0.0
#setosa 30개의 평균 분산
for i in range(len(iris_matrix[0])-1):
    for j in range(0,30):
        sum += float(iris_matrix[j][i])
        setosa_tmp.append(iris_matrix[j][i])
    setosa30_avg_list.append(round(sum/30,2))
    setosa30_var_list.append(round(numpy.var(setosa_tmp),2))
    setosa_tmp=[]
    sum=0.0
#versicolor에 대한 평균 분산
for i in range(len(iris_matrix[0])-1):
    for j in range(50,100):
        sum += float(iris_matrix[j][i])
        versicolor_tmp.append(iris_matrix[j][i])
    versicolor_avg_list.append(round(sum/50,2))
    versicolor_var_list.append(round(numpy.var(versicolor_tmp),2))
    sum=0.0
    versicolor_tmp=[]
#versicolor 30개의 평균 분산
for i in range(len(iris_matrix[0])-1):
    for j in range(50,80):
        sum += float(iris_matrix[j][i])
        versicolor_tmp.append(iris_matrix[j][i])
    versicolor30_avg_list.append(round(sum/30,2))
    versicolor30_var_list.append(round(numpy.var(versicolor_tmp),2))
    sum=0.0
    versicolor_tmp=[]
#virginica에 대한 평균 분산
for i in range(len(iris_matrix[0])-1):
    for j in range(100,150):
        sum += float(iris_matrix[j][i])
        virginica_tmp.append(iris_matrix[j][i])
    virginica_avg_list.append(round(sum/50,2))
    virginica_var_list.append(round(numpy.var(virginica_tmp),2))
    sum=0.0
    virginica_tmp=[]
#virginica 30개의 평균 분산
for i in range(len(iris_matrix[0])-1):
    for j in range(100,130):
        sum += float(iris_matrix[j][i])
        virginica_tmp.append(iris_matrix[j][i])
    virginica30_avg_list.append(round(sum/30,2))
    virginica30_var_list.append(round(numpy.var(virginica_tmp),2))
    sum=0.0
    virginica_tmp=[]

print("Iris 데이터 행렬:")
print(iris_matrix)
print("평균: ",all_avg_list)
print("분산: ", all_var_list)
print("setosa avg: ",setosa_avg_list)
print("setosa var: ", setosa_var_list)
print("versicolor avg: ",versicolor_avg_list)
print("versicolor var: ",versicolor_var_list)
print("virginica avg: ",virginica_avg_list)
print("virginica var:", virginica_var_list)

print("setosa30 avg: ",setosa30_avg_list)
print("setosa30 var: ", setosa30_var_list)
print("versicolor30 avg: ", versicolor30_avg_list)
print("versicolor30 var: ", versicolor30_var_list)
print("virginica30 avg: ",virginica_avg_list)
print("virginca30 var: ", virginica_var_list)


print(setosa30_avg_list[1])
up = 0.0
down = 0.0
setosa_top_30 = iris_matrix[:30, :2]  # setosa 클래스의 상위 30개 데이터의 첫 번째와 두 번째 속성만 추출
setosa30_avg_list = setosa_avg_list[:2]  # 속성 값만 사용

for i in range(30):
    up += (float(setosa_top_30[i][0]) - float(setosa30_avg_list[0])) * (float(setosa_top_30[i][1]) - float(setosa30_avg_list[1]))
    down += np.power((float(setosa_top_30[i][0]) - float(setosa30_avg_list[0])), 2)

beta1 = up / down
beta0 = float(setosa30_avg_list[1]) - (beta1 * float(setosa30_avg_list[0]))

print("기울기 (β₁):", beta1)
print("y절편 (β₀):", beta0)