import numpy as np
import math
import random
from sklearn.utils.extmath import logsumexp
import scipy.misc
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import warnings
#warnings.filterwarnings("ignore")

def AffineForward(A, W, b):
	Z = np.add(np.matmul(A, W), b)
	Acopy = np.copy(A)
	Wcopy = np.copy(W)
	bcopy = np.copy(b)
	return Z, [Acopy, Wcopy, bcopy]

def ReLUForward(Z):
	A = np.empty_like(Z)
	Zcopy = np.copy(Z)
	for i in range(0, Z.shape[0]):
			A[i] = np.maximum(Z[i], np.zeros(Z[i].shape))
	return A, Zcopy

def AffineBackward(dZ, acache):
	db = np.sum(dZ, axis=0)
	dW = np.matmul(np.transpose(acache[0]), dZ)
	dA = np.matmul(dZ, np.transpose(acache[1]))
	return dA, dW, db

def ReLUBackward(dA, rcache):
	dZ = np.empty_like(dA)
	Z = np.copy(rcache)
	for i in range(0, Z.shape[0]):
		for j in range(0, Z.shape[1]):
			if Z[i][j] < 0: 
				dZ[i][j] = 0
			else:
				dZ[i][j] = dA[i][j]
	return dZ

def softmax(x):
	e_x = np.exp(x - np.max(x))
	return e_x / np.sum(e_x)

def CrossEntropy(F, y):
	#print(F, y)
	sumF = 0
	n = (float)(y.shape[0])
	for i in range((int)(n)):
		logsum = scipy.misc.logsumexp(F[i])
		if(math.isnan(logsum)):
			print(F)
			raise SystemExit
		sumF += F[i][(int)(y[i])] - logsum
	L = -1 * sumF/n
	dF = np.empty_like(F)
	for i in range(F.shape[0]):
		dF[i] = softmax(F[i])
	for i in range(dF.shape[0]):
		dF[i, (int)(y[i])] -= 1
	dF = dF/n
	return L, dF
	

def FourLayerNetwork (X, Ws, bs, y, epoch, test):
	
	Z1, acache1 = AffineForward(X, Ws[0], bs[0])
	A1, rcache1 = ReLUForward(Z1)
	Z2, acache2 = AffineForward(A1, Ws[1], bs[1])
	A2, rcache2 = ReLUForward(Z2)
	Z3, acache3 = AffineForward(A2, Ws[2], bs[2])
	A3, rcache3 = ReLUForward(Z3)
	F, acache4 = AffineForward(A3, Ws[3], bs[3])
	if test:
		F = F.reshape(3,X.shape[0])
		classifications = np.argmax(F)
		#print(classifications)
		return classifications
	loss, dF = CrossEntropy(F, y)
	dA3, dW4, db4 = AffineBackward(dF, acache4)
	dZ3 = ReLUBackward(dA3, rcache3)
	dA2, dW3, db3 = AffineBackward(dZ3, acache3)
	dZ2 = ReLUBackward(dA2, rcache2)
	dA1, dW2, db2 = AffineBackward(dZ2, acache2)
	dZ1 = ReLUBackward(dA1, rcache1)
	dX, dW1, db1 = AffineBackward(dZ1, acache1)
	
	# Update parameters using GD
	learning_rate = 0.1
	Ws[3] = np.add(Ws[3], - (dW4 * learning_rate))
	Ws[2] = np.add(Ws[2], - (dW3 * learning_rate))
	Ws[1] = np.add(Ws[1], - (dW2 * learning_rate))
	Ws[0] = np.add(Ws[0], - (dW1 * learning_rate))
	bs[3] = np.add(bs[3], - (db4 * learning_rate))
	bs[2] = np.add(bs[2], - (db3 * learning_rate))
	bs[1] = np.add(bs[1], - (db2 * learning_rate))
	bs[0] = np.add(bs[0], - (db1 * learning_rate))
	return loss, np.copy(Ws), np.copy(bs)

def MinibatchGD(data, epoch):
	scale_factor = 0.2
	W = []
	W.append(scale_factor * (np.random.rand(5,256) - 0.5))
	W.append(scale_factor * (np.random.rand(256,256) - 0.5))
	W.append(scale_factor * (np.random.rand(256,256) - 0.5))
	W.append(scale_factor * (np.random.rand(256,3) - 0.5))
	b = []
	b.append(np.zeros(256))
	b.append(np.zeros(256))
	b.append(np.zeros(256))
	b.append(np.zeros(3))
	N = data.shape[0]
	n = 128
	batch_num = (int)(N/n)
	loss = []
	for e in range(epoch):
		last_loss = 0
		data = shuffle(data)
		for i in range(batch_num):
			if i == batch_num-1:
				X = data[i*n:, :-1]
				y = data[i*n:, -1]
				ll, W, b = FourLayerNetwork(X, W, b, y, e, False)
				#print(ll)
				last_loss += ll
				#print(loss)
			else:
				X = data[i*n:(i+1)*n, :-1]
				y = data[i*n:(i+1)*n, -1]
				ll, W, b = FourLayerNetwork(X, W, b, y, e, False)
				#print(ll)
				last_loss += ll
				#print(loss)

		last_loss = last_loss / batch_num
		loss.append(last_loss)
		
		print("epoch %i: %f"%(e, last_loss))
	#print(loss)
	#plt.plot(range(epoch), loss)
	#plt.show()
	
	return W, b






