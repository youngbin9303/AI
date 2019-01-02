import numpy as np
from copy import deepcopy
import pprint
import matplotlib.pyplot as plt
pp = pprint.PrettyPrinter(indent = 4)
import matplotlib
import matplotlib.pyplot
file = open('optdigits-orig_train.txt')
testing_file = open('optdigits-orig_test.txt')
testing_line = testing_file.readlines()
train_lines = file.readlines()
training_data = []
testing_data = []
i = 0
epoch = 5
learning_rate = 0.2
training_accuracy = []
dict = {}
data = np.array([])
x = np.array([])
y = np.array([])
confusion_matrix = np.zeros((10,10))

def learning_rate_decay(learning_rate, epoch):
    return learning_rate/(epoch+1)

def decision_rule(w, x):
    result = np.array([])
    for a in range(len(w)):
        result = np.append(result, np.dot(w[a], x))
    return np.argmax(result)

def update_rule_c(w, x):
    return w + (learning_rate * x)

def update_rule_cprime(w,x):
    return w - (learning_rate * x)

for line in train_lines:
    line = line.strip()
    if len(line) > 1:
        line = [int(n) for n in line]
    if i == 32:
        nump_data = np.array(data)
        d = np.append([1], nump_data)
        dict['data'] = np.array(d)
        dict['label'] = int(line)
        training_data.append(dict)
        dict = {}
        data = np.array([])
        i = 0
    else:
        arr = list(line)
        data = np.append(data, arr)
        i+=1

for line in testing_line:
    line = line.strip()
    if len(line) > 1:
        line = [int(n) for n in line]
    if i == 32:
        nump_data = np.array(data)
        d = np.append([1], nump_data)
        dict['data'] = np.array(d)
        dict['label'] = int(line)
        testing_data.append(dict)
        dict = {}
        data = np.array([])
        i = 0
    else:
        arr = list(line)
        data = np.append(data, arr)
        i+=1

weights = np.array([np.zeros((1025))]*10)

for epo in range(epoch):
    print('epoch ', epo+1)
    wrong = 0
    right = 0

    for dat in training_data:
        label = dat['label']
        data = dat['data']
        decision = decision_rule(weights, data)
        confusion_matrix[label][decision] += 1        
        if decision != label:
            wrong += 1
            weights[label] = update_rule_c(weights[label], data)        
            weights[decision] = update_rule_cprime(weights[decision], data)
        else:
            right += 1
    acc = right/(right+wrong)
    training_accuracy.append((epo, acc))
    x = np.append(x,epo)
    y = np.append(y,acc)

    print('accuracy = ', acc)
    print('learning rate = ', learning_rate)
    learning_rate = learning_rate_decay(learning_rate, epo)

plt.plot(x,y)
plt.xlabel('epoch')
plt.ylabel('Training accuray')
plt.show()

print('training acc = ', training_accuracy)

percentage_confusion_matrix = np.zeros((10, 10))
for i, row in enumerate(confusion_matrix):
    sum = np.sum(row)
    for j, col in enumerate(row):
        percentage_confusion_matrix[i][j] = round((col/sum), 2)
print('confusion matrix = ')
pp.pprint(percentage_confusion_matrix)
for a in percentage_confusion_matrix:
    print(np.sum(a))
testing_wrong = 0
testing_right = 0
for dat in testing_data:
    label = dat['label']
    data = dat['data']
    decision = decision_rule(weights, data)
    if decision != label:
        testing_wrong += 1
    else:
        testing_right += 1

print('tesing acc = ', testing_right/(testing_right+testing_wrong))

print('Learned perceptron weights ')
idx = 0
for weight in weights:
    weight = weight[:-1]
    reshaped = np.reshape(weight, (32, 32))
    matplotlib.pyplot.imshow(reshaped, cmap='jet', interpolation='nearest')
    matplotlib.pyplot.show()