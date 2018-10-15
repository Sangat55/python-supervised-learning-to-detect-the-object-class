from matplotlib import pyplot as plt
import numpy as np
import win32com.client as wc

data = [[3,1.5,1],
        [2,1,0] ,
        [4,1.5,1 ],
        [2.5,1,0],
        [3.5 , .5, 1],
        [2,0.5 , 0],
        [5.5 , 1 ,1],
        [1,1,0]]
flower = [4.5 , 1.5]
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

def sigmoid(x):
    return 1/(1+ np.exp(-x))
def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))
#plt.axis([0,6,0,6])
#plt.grid()
for i in range(len(data)):
    point = data[i]
    color  = 'r'
    if point[2] == 0 :
        color = 'b'
    #plt.scatter(point[0], point[1] , c = color)
rate = 0.2
costs = []
for i in range(5000):
    ri = np.random.randint(len(data))
    point = data[ri]
    z = point[0] * w1 + point[2] * w2 + b
    pred= sigmoid(z)
    target = point[2]
    cost = np.square(pred-target)
    dcost_pred = 2*(pred-target)
    dpred_dz = sigmoid_p(z)
    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_db = 1
    costs.append(cost)
    dcost_dz = dcost_pred * dpred_dz
    dcost_dw1 = dcost_dz * dz_dw1
    dcost_dw2 = dcost_dz * dz_dw2
    dcost_db = dcost_dz * dz_db
    w1 = w1-rate * dcost_dw1
    w2 = w2-rate * dcost_dw2
    b  = b - rate * dcost_db
    if i % 100 == 0 :
        cost_sum = 0 
        for j in range(len(data)):
            point = data[ri]
            z = point[0] * w1 + point[1] * w2 + b 
            pred = sigmoid(z)
            target = point[2]
            cost_sum += np.square(pred-target)
        costs.append(cost_sum/len(data))
            
plt.plot(costs)
for i in range(len(data)):
    point = data[i]
    print(point)
    z = point[0] * w1 + point[1 ] * w2 + b
    pred = sigmoid(z)
    print(pred)
    
def which_flower(height , width):
    z = height * w1 + width * w2 + b
    pred = sigmoid(z)
    print(pred)
    if pred >= 0.5:
       speak = wc.Dispatch("Sapi.SpVoice")
       speak.Speak("I am Red")
    else:
        speak = wc.Dispatch("Sapi.SpVoice")
        speak.Speak("I am  Blue")

h = float(input("Enter the height of petals:"))
w = float(input("Enter the width of the petals:"))
which_flower(h,w)