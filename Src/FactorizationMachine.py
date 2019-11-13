import numpy as np
from Model import Model



class FactorizationMachine(Model):

    def __init__(self, num_features, num_factors):

        self._num_features = num_features
        self._num_factors = num_factors # a.k.a. k
        self.__w = np.zeros(self._num_features, dtype=np.float)    # w vector
        self.__b = 0    # bias
        self.__v = np.zeros((self._num_features, self._num_factors), dtype=np.float)    # second order factor matrix


    def getPrediction(self, x):

        v2 = np.power(self.__v, 2)
        x2 = x.power(2)
        factor_member = np.sum(np.power(x.dot(self.__v), 2) - x2.dot(v2), axis=1) / 2
                
        prediction = self.__b + x.dot(self.__w) + factor_member
        return prediction


    def updateParameters(self, x_batch, z_batch, batch_size, lr=0.01):  # dL / dw ?

        pred_batch = self.getPrediction(x_batch)
        diff_part = -2 * (z_batch - pred_batch) / batch_size
        #batch_range = range(batch_size)

        db = np.sum(diff_part)

        xt = x_batch.transpose()
        dw = xt.dot(diff_part)

        print('DONE')

        # N = batch_size; n = num_features; k = num_factors
        # i, j = {1..n}; f = {1..k}
        x2 = np.repeat(np.power(x_batch_dense, 2)[:, :, np.newaxis], self._num_factors, axis=2)  # construct R^{N x n x k} 
        m = np.dot(x_batch_dense, self.__v) # sum v_{jf} * x_j
        xm = np.dot(x_batch_dense.reshape((batch_size, -1, 1)), m.reshape((batch_size, 1, -1))) # R^{N x n} to R^{N x n x 1} and R^{N x k} to R^{N x 1 x k}
        x2v = np.multiply(self.__v, x2)    # x_i^2 * v_{if}
        dv = -1 * np.tensordot((z_batch - self.getPrediction(x_batch_dense)), (xm - x2v), axes=(0, 0))

        self.__w -= lr * dw
        self.__b -= lr * db
        self.__v -= lr * dv


    def resetWeights(self):

        self.__b = 0.0
        self.__w = np.zeros(self._num_features, dtype=np.float)
        self.__v = np.zeros((self._num_features, self._num_factors), dtype=np.float)

    
    def getWeights(self):

        return self.__b, self.__w, self.__v

