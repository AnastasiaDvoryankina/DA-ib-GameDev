import numpy as np
import matplotlib.pyplot as plt
import gspread
import numpy.random

import numpy as np
import matplotlib.pyplot as plt
import gspread
import numpy.random

x = [3,21,22,34,54,34,55,67,89,99]
x = np.array(x)
y = [2,22,24,65,79,82,55,130,150,199]
y = np.array(y)
gc = gspread.service_account(filename='unitysound-b3b9dd2033d6.json')
sh = gc.open("UnitySound")
plt.scatter(x,y)
plt.show()
def model(a, b, x):
    return a*x + b

def loss_function(a, b, x, y):
    num = len(x)
    prediction=model(a,b,x)
    return (0.5/num) * (np.square(prediction-y)).sum()

def optimize(a,b,x,y):
    num = len(x)
    prediction = model(a,b,x)
    da = (1.0/num) * ((prediction -y)*x).sum()
    db = (1.0/num) * ((prediction -y).sum())
    a = a - Lr*da
    b = b - Lr*db
    return a, b

def iterate(a,b,x,y,times):
    for i in range(times):
        a,b = optimize(a,b,x,y)
    return a,b
a = np.random.rand(1)
print(a)
b = np.random.rand(1)
print(b)
Lr = 0.000001
for j in range(1,6):
    if j == 1:
        print("j = ", j)
        a, b = iterate(a, b, x, y, 1)
        prediction = model(a, b, x)
        loss = loss_function(a, b, x, y)
        print(a, b, loss)
        plt.scatter(x, y)
        plt.plot(x, prediction)
        plt.show()
        _loss = str(loss)
        _loss = _loss.replace('.', ',')
        sh.sheet1.update(('A' + str(j)), str(j))
        sh.sheet1.update(('B' + str(j)), str(_loss))
    if j == 2:
        print("j = ", j)
        a, b = iterate(a, b, x, y, 100)
        prediction = model(a, b, x)
        loss = loss_function(a, b, x, y)
        print(a, b, loss)
        plt.scatter(x, y)
        plt.plot(x, prediction)
        plt.show()
        _loss = str(loss)
        _loss = _loss.replace('.', ',')
        sh.sheet1.update(('A' + str(j)), str(j))
        sh.sheet1.update(('B' + str(j)), str(_loss))
    if j == 3:
        print("j = ", j)
        a, b = iterate(a, b, x, y, 250)
        prediction = model(a, b, x)
        loss = loss_function(a, b, x, y)
        print(a, b, loss)
        plt.scatter(x, y)
        plt.plot(x, prediction)
        plt.show()
        _loss = str(loss)
        _loss = _loss.replace('.', ',')
        sh.sheet1.update(('A' + str(j)), str(j))
        sh.sheet1.update(('B' + str(j)), str(_loss))
    if j == 4:
        print("j = ", j)
        a, b = iterate(a, b, x, y, 300)
        prediction = model(a, b, x)
        loss = loss_function(a, b, x, y)
        print(a, b, loss)
        plt.scatter(x, y)
        plt.plot(x, prediction)
        plt.show()
        _loss = str(loss)
        _loss = _loss.replace('.', ',')
        sh.sheet1.update(('A' + str(j)), str(j))
        sh.sheet1.update(('B' + str(j)), str(_loss))
    if j == 5:
        print("j = ", j)
        a, b = iterate(a, b, x, y, 15000)
        prediction = model(a, b, x)
        loss = loss_function(a, b, x, y)
        print(a, b, loss)
        plt.scatter(x, y)
        plt.plot(x, prediction)
        plt.show()
        _loss = str(loss)
        _loss = _loss.replace('.', ',')
        sh.sheet1.update(('A' + str(j)), str(j))
        sh.sheet1.update(('B' + str(j)), str(_loss))

