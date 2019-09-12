########################
# Daniel Goldstein
# implement sparse array
# August 10th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
You have a large array, most of
whose elements are zero.
Create a more space-effcient data structure,
SparseArray, that implements the following interface:

-init(arr, size): initialize with the orignal large array and size
-set(i, val): update index at i to be val
-get(i): get the value at index i
'''
class SparseArray:
    def __init__(self, arr, size):
        self._dic = {}
        self.size = size
        for i, e in enumerate(arr):
            if e != 0:
                self._dic[i] = e

    def set(self, i, val):
        if i >= 0 and i < self.size and val != 0:
            self._dic[i] = val
        elif i in self._dic.keys():
            del self._dic[i]
        else:
            raise IndexError('Index not in range')

    def get(self, i):
        if i in self.keys():
            return self._dic[i]
        elif i >= 0 and i < self.size:
            return 0
        else:
            raise IndexError('Index not in range')
