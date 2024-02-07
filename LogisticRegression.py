import numpy as np 

class LogisticRegression():
    def __init__(self, lr = 0.001, i = 100000):
        self.lr = lr
        self.i = i
        self.weight = None
        self.bias = None
    def sigmoid(self,x):
        x = np.clip(x,-500,500)
        return 1 / (1+np.exp(-x))
    def param(self, x):
        self.weight = np.zeros((x.shape[1],1))
        self.bias = 0
    def train(self, x, y):
        self.param(x)
        y = y.reshape(-1, 1)
        for i in range(self.i):
            linear_pred = np.dot(x,self.weight) + self.bias
            y_pred = self.sigmoid(linear_pred)
            dw = (1/len(x)) * np.dot(x.T, (y_pred - y))
            db = (1/len(x)) * np.sum(y_pred - y)
            self.weight -= self.lr * dw 
            self.bias -= self.bias * db
    def predict(self, x):
        linear_pred = np.dot(x, self.weight) + self.bias
        y_pred = self.sigmoid(linear_pred)
        class_pred = [0 if y<=0.5 else 1 for y in y_pred]
        return class_pred

def format_data(path,split = 0.875):
    data = np.genfromtxt(path, delimiter=',')
    nan_rows = np.isnan(data).any(axis=1)
    data = data[~nan_rows]
    x,y = data[:,:data.shape[1]-1], data[:,data.shape[1]-1:]
    x = x[:,~np.all(x == 0, axis = 0)]
    new_min,new_max = -10,10
    old_min = np.min(x, axis=0)
    old_max = np.max(x, axis=0)
    x = new_min + (x - old_min) * (new_max - new_min) / (old_max - old_min)
    x_train,x_test = x[:round(len(x)*split),:], x[round(len(x)*split):,:]
    y_train,y_test = y[:round(len(y)*split),:], y[round(len(y)*split):,:]
    return x_train,y_train,x_test,y_test
    
    


x_train,y_train,x_test,y_test = format_data('C:\\Users\\mubta\\Desktop\\CSE422\\Lab\\framingham.csv')
model_1 = LogisticRegression(lr = 0.001)
model_1.train(x_train,y_train)
predictions = model_1.predict(x_test)
accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy}")

from sklearn.model_selection import train_test_split
from sklearn import datasets
bc = datasets.load_breast_cancer()
x, y = bc.data, bc.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)
model_2 = LogisticRegression(lr = 0.001)
model_2.train(x_train,y_train)
predictions = model_2.predict(x_test)
accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy}")

x_train,y_train,x_test,y_test = format_data('C:\\Users\\mubta\\Desktop\\CSE422\\Lab\\train_and_test2.csv')

model_3 = LogisticRegression(lr = 0.001)
model_3.train(x_train,y_train)
predictions = model_3.predict(x_test)
accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy}")