from sklearn import datasets, linear_model
import numpy as np

# Iris 데이터셋 로드
iris = datasets.load_iris()
X = iris.data
y = iris.target

# setosa 클래스에 해당하는 인덱스 추출
setosa_indices = np.where(y == 0)[0]

# setosa 클래스에 해당하는 데이터 추출
setosa_data = X[setosa_indices]

# setosa 클래스에 해당하는 데이터를 sepal length (cm) 기준으로 정렬
setosa_data_sorted = setosa_data[setosa_data[:, 0].argsort()]

# 상위 30개 샘플 선택
top_30_setosa_data = setosa_data_sorted[:30]

# 선형 회귀 모델 생성
regr = linear_model.LinearRegression()

# Sepal Length를 독립변수(X)로, Sepal Width를 종속변수(y)로 설정하여 회귀 모델 학습
regr.fit(top_30_setosa_data[:, 0].reshape(-1, 1), top_30_setosa_data[:, 1])

# 회귀선의 기울기와 y절편 출력
print("회귀선의 기울기:", regr.coef_[0])
print("회귀선의 y절편:", regr.intercept_)
