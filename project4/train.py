import numpy as np
import math
import random
import part2_1

data = []
with open("expert_policy.txt") as f:
	for line in f:
		state = [float(x) for x in line.split()]
		data.append(state)
data = np.array(data)

data_mean = np.mean(data[:, :-1], axis=0)
data_std = np.std(data[:, :-1], axis=0)
data[:, :-1] = (data[:, :-1] - data_mean) / data_std

W, b = part2_1.MinibatchGD(data, 100)
Xs = data[:, :-1]
ys = data[:, -1]
count = 0
correct = 0
conf_mat = np.zeros((3,3))
for i in range(data.shape[0]):
	count += 1
	res = part2_1.FourLayerNetwork(Xs[i].reshape((1,5)), W, b, ys[i].reshape((1,1)), 0, True)
	print(res, ys[i])
	conf_mat[(int)(ys[i]), (int)(res)] += 1
	if res==ys[i]:
		correct += 1
for i in range(3):
	conf_mat[i] = conf_mat[i]/np.sum(conf_mat[i])
print("accuracy", correct/(count*1.0))
np.savetxt("confusion_matrix2.txt", conf_mat)
np.save("W2.npy", W)
np.save("b2.npy", b)