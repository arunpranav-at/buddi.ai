# program to classify using regression
# importing the required libraries
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from matplotlib.lines import Line2D

def indicator(lst):
    elements = list(set(lst))
    ans = []
    for i in lst:
        ans.append(elements.index(i))
    return ans

def dataset():
    # creating datasets
    x = [1, 2, 3, 4, 5, -3, -4, -5, -6] # x values
    yreal = ['B','B','B','B','B','G','G','G','G'] # y values
    y = indicator(yreal)
    x = np.array(x, dtype=np.float32).reshape(-1, 1)
    y = np.array(y, dtype=np.float32).reshape(-1, 1)
    return x, y

#Model y=sigmoid(X*W + b)
# same as the linear regression just sigmoid wrapped around the linear equation
def output(x, W, b, a): 
    return tf.nn.sigmoid(a*(tf.matmul(x, W) + b))

#Loss function : sum of squares
def loss_function(y_pred, y_true):
    return tf.reduce_sum(tf.square(y_pred - y_true))

x_train, y_train = dataset()

#Initialize Weights
W = tf.Variable(tf.random.uniform(shape=(1, 1), dtype=tf.float32))
b = tf.Variable(tf.zeros(shape=(1,), dtype=tf.float32))
a = tf.Variable(tf.zeros(shape=(1,), dtype=tf.float32))

## Optimization
learning_rate = 0.1
steps = 300 #epochs
x_plot = np.arange(-7, 6, 0.001, dtype=np.float32).reshape(-1, 1)
for i in range(steps):
    with tf.GradientTape() as tape:
        predictions = output(x_train, W, b, a)
        loss = loss_function(predictions, y_train)
    dloss_dw, dloss_db, dloss_da = tape.gradient(loss, [W, b, a])
    W.assign_sub(learning_rate * dloss_dw)
    b.assign_sub(learning_rate * dloss_db)
    a.assign_sub(learning_rate * dloss_da)
    print(f"epoch : {i}, loss  {loss.numpy()},  W : {W.numpy()}, b  {b.numpy()}, a  {a.numpy()}")
    
yplot = output(x_plot, W, b, a)
plt.title("Classification Using Sigmoid Function")
plt.xlabel("X Coordinates")
plt.ylabel("Y Coordinates")
plt.figtext(0.5, 0.01, "More the number of epochs, more the accuracy of the model. " + f"epoch : {i}, loss  {loss.numpy()},  W : {W.numpy()}, b  {b.numpy()}, a  {a.numpy()}", wrap=True, horizontalalignment='center', fontsize=12)
plt.plot(x_train, y_train, 'bo', label='Actual Data')
plt.plot(x_plot, yplot, 'r-', markersize='1', label='Sigmoid Line')
plt.legend(handles=[Line2D([0], [0], color='blue', lw=2, label='Actual Data'),
                    Line2D([0], [0], color='red', lw=2, label='Sigmoid Line')])
plt.show()