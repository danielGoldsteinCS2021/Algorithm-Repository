########################
# Daniel Goldstein
# max stock profit
# July 13th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################


'''
Given a array of numbers representing the stock
prices of a company in chronological order,
write a function that calculates the maximum profit you could have made
from buying and selling that stock once. You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.

'''


def maxStockProfit(ls):
    lenLs = len(ls)
    if lenLs > 1:
        rslt = ls[1] - ls[0]
        indexVal = ls[0]
    else:
        return None
    for i in range(0, lenLs-1):
        for j in range(i+1, lenLs):
            if ls[j]-ls[i] > rslt:
                rslt = ls[j]-ls[i]
                indexVal = ls[i]
    return indexVal

# TESTING ##############################
arr0 = [9, 11, 8, 5, 7, 10] # -> 5
arr1 = [] # -> None
arr2 = [1] # -> None
arr3 = [1, 2] # -> 1
arr4 = [2, 1] # -> 2
arr5 = [5, 4, 1] # -> 5
arr6 = [6, 5, 4, 10, 3, 4, 1] # -> 4
arr7 = [1, 4, 5] # -> 1
arr8 = [1, 100, 20, 50] # -> 1
arr9 = [100, 100, 100] # -> 100
arr10 = [170, 180, 200, 50, 26, 70, 80, 90, 100, 20, 40, 88, 110, 40, 25, 1] # -> 20


print("Testing with arrray ", arr0, "\nmaxStockProfit returns: ", maxStockProfit(arr0))
print("Testing with arrray ", arr1, "\nmaxStockProfit returns: ", maxStockProfit(arr1))
print("Testing with arrray ", arr2, "\nmaxStockProfit returns: ", maxStockProfit(arr2))
print("Testing with arrray ", arr3, "\nmaxStockProfit returns: ", maxStockProfit(arr3))
print("Testing with arrray ", arr4, "\nmaxStockProfit returns: ", maxStockProfit(arr4))
print("Testing with arrray ", arr5, "\nmaxStockProfit returns: ", maxStockProfit(arr5))
print("Testing with arrray ", arr6, "\nmaxStockProfit returns: ", maxStockProfit(arr6))
print("Testing with arrray ", arr7, "\nmaxStockProfit returns: ", maxStockProfit(arr7))
print("Testing with arrray ", arr8, "\nmaxStockProfit returns: ", maxStockProfit(arr8))
print("Testing with arrray ", arr9, "\nmaxStockProfit returns: ", maxStockProfit(arr9))
print("Testing with arrray ", arr10, "\nmaxStockProfit returns: ", maxStockProfit(arr10))
