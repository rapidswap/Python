# import numpy as np

# class Perceptron:
#     def __init__(self, input_size, lr=1, epochs=100):
#         self.W = np.zeros(input_size+1)
#         self.epochs = epochs
#         self.lr = lr
    
#     def activation_fn(self, x):
#         return 1 if x >= 0 else 0
    
#     def predict(self, x):
#         x = np.insert(x, 0, 1) # Adding bias
#         z = self.W.T.dot(x)
#         a = self.activation_fn(z)
#         return a
    
#     def train(self, X, labels):
#         for _ in range(self.epochs):
#             for i in range(len(X)):
#                 x = np.insert(X[i], 0, 1) # Adding bias
#                 y_pred = self.predict(X[i])
#                 e = labels[i] - y_pred
#                 self.W = self.W + self.lr * e * x

# # AND gate
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# AND_labels = np.array([0, 0, 0, 1])

# and_perceptron = Perceptron(input_size=2)
# and_perceptron.train(X, AND_labels)

# print("AND Gate:")
# for i in range(len(X)):
#     print(X[i], ":", and_perceptron.predict(X[i]))


w0=-0.5
x0=1
w1=1
w2=1

def ANDGATE(x1,x2):
    y=w1*x1+w2*x2+x0
    if y>=1:
        y=1
    else:
        y=0
    return y

print(ANDGATE(1,0))
