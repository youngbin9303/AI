import numpy as np
import math
import copy
import matplotlib.pyplot as plt
# Training
hl_tokens = np.empty((10,2))
hl_tokens_strings = []
temp = []
for i in range(10):
	temp.append("")
for i in range(2):
	hl_tokens_strings.append(copy.deepcopy(temp))
for i in range(10):
	hl_tokens[i][0] = -10000
	hl_tokens[i][1] = 10000
avg_accuracy = np.zeros(100, dtype=float)
class_count = np.zeros(10, dtype=int)
frequencys = np.zeros((10,32,32), dtype=int)
training_data = open("digitdata/optdigits-orig_train.txt", "r")
token = training_data.readlines(33 * 32 + 1)
while token:
	curr_class = int(token[32][1])
	class_count[curr_class] += 1
	for i in range(32):
		for j in range(32):
			frequencys[curr_class][i][j] += int(token[i][j])
	token = training_data.readlines(33 * 32 + 1)
	

likelihoods = np.zeros((10,32,32,2), dtype=float)
laplace_coeff = 5.8
for i in range(10):
	for j in range(32):
		for k in range(32):
			likelihoods[i][j][k][0] = (class_count[i] - frequencys[i][j][k] + laplace_coeff) / (class_count[i] + 2 * laplace_coeff)
			likelihoods[i][j][k][1] = (frequencys[i][j][k] + laplace_coeff) / (class_count[i] + 2 * laplace_coeff)
pclass = np.zeros(10, dtype=float)
total_count = np.sum(class_count)
for i in range(10):
	pclass[i] = class_count[i]/total_count
# Testing
confusion = np.zeros((10,10), dtype = float)
training_data.close()
testing_data = open("digitdata/optdigits-orig_test.txt", "r")

token = testing_data.readlines(33 * 32 + 1)
while token:
	
	true_class = int(token[32][1])
	probabilities = np.zeros(10, dtype=float)
	for i in range(10):
		prob = 0.0
		prob += math.log(pclass[true_class])
		for j in range(32):
			for k in range(32):
				prob += math.log(likelihoods[i][j][k][int(token[j][k])])
		probabilities[i] = prob
	map_class = np.argmax(probabilities)
	confusion[true_class][map_class] += 1
	if true_class == map_class:
		if hl_tokens[true_class][0] < probabilities[map_class]:
			hl_tokens[true_class][0] = probabilities[map_class]
			hl_tokens_strings[0][true_class] = copy.deepcopy(token)
		if hl_tokens[true_class][1] > probabilities[map_class]:
			hl_tokens[true_class][1] = probabilities[map_class]
			hl_tokens_strings[1][true_class] = copy.deepcopy(token)
	token = testing_data.readlines(33 * 32 + 1)
for i in range(10):
	confusion[i] = confusion[i] / (np.sum(confusion[i]))
accuracy = np.zeros(10, dtype=float)
for i in range(10):
	accuracy[i] = confusion[i][i]
testing_data.close()
	
	

new_doc = open("confusion_matrix.txt", "w+")
for i in range(10):
	for j in range(10):
		new_doc.write("%f  " % confusion[i][j])
	new_doc.write("\n")

new_doc.close()
new_doc = open("highlight_tokens.txt", "w+")
for i in range(10):
	new_doc.write("%d: \n" % i)
	new_doc.write("highest posterior probability : %f" % hl_tokens[i][0])
	for j in range(32):
		new_doc.write(hl_tokens_strings[0][i][j])
	new_doc.write("lowest posterior probability : %f" % hl_tokens[i][1])
	for j in range(32):
		new_doc.write(hl_tokens_strings[1][i][j])

new_doc.close()

confusion_pairs = []
pairs = []
for i in range(10):
	for j in range(i+1, 10):
		pairs.append([i,j])
for p in pairs:
	confusion_pairs.append([0, p])
for p in confusion_pairs:
	p[0] = confusion[p[1][0]][p[1][1]] + confusion[p[1][1]][p[1][0]]

temp = np.zeros(45, dtype=float)
c = 0
for p in confusion_pairs:
	temp[c] = p[0]
	c += 1
chosen_pairs = []
for i in range(4):
	chosen_pairs.append(confusion_pairs[np.argmax(temp)])
	temp[np.argmax(temp)] = -1
for p in chosen_pairs:   
	l1 = np.zeros((32,32), dtype=float)
	l1_max = -100
	l1_min = 100
	for i in range(32):
		for j in range(32):
			l1[31-i][j] = math.log(likelihoods[p[1][0]][i][j][1])
			if(l1_max < l1[31-i][j]):
				l1_max = l1[31-i][j]
			if(l1_min > l1[31-i][j]):
				l1_min = l1[31-i][j]
	l2 = np.zeros((32,32), dtype=float)
	l2_max = -100
	l2_min = 100
	for i in range(32):
		for j in range(32):
			l2[31-i][j] = math.log(likelihoods[p[1][1]][i][j][1])
			if(l2_max < l2[31-i][j]):
				l2_max = l2[31-i][j]
			if(l2_min > l2[31-i][j]):
				l2_min = l2[31-i][j]
	l3 = np.zeros((32,32), dtype=float)
	l3_max = -100
	l3_min = 100
	for i in range(32):
		for j in range(32):
			l3[i][j] = math.log(l1[i][j] / l2[i][j])
			if(l3_max < l3[i][j]):
				l3_max = l3[i][j]
			if(l3_min > l3[i][j]):
				l3_min = l3[i][j]
	plt.pcolormesh(l1, cmap="jet", vmax=l1_max, vmin=l1_min)
	plt.colorbar()
	plt.show()
	plt.pcolormesh(l2, cmap="jet", vmax=l2_max, vmin=l2_min)
	plt.colorbar()
	plt.show()
	plt.pcolormesh(l3, cmap="jet", vmax=l3_max, vmin=l3_min)
	plt.colorbar()
	plt.show()





