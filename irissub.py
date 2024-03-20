mport pandas as pd

# URL에서 데이터 다운로드
iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)

# 열 이름 설정
iris_data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "iris_class"]

# 데이터 출력
print(iris_data.to_string())
