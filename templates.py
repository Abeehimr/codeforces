n = 10

#2d prefix sum
def prefixSum2D(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(1,n):
        mat[i][0] += mat[i-1][0]
    for j in range(1,m):
        mat[0][j] += mat[0][j-1]
    for i in range(1,n):
        for j in range(1,m):
            mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
    return mat

#range sum query
def rangeSum(mat, r1, c1, r2, c2):
    sm = mat[r2][c2]
    if r1 > 0:
        sm -= mat[r1-1][c2]
    if c1 > 0:
        sm -= mat[r2][c1-1]
    if r1 > 0 and c1 > 0:
        sm += mat[r1-1][c1-1]
    return sm
    
def nextPermutation(nums):
    i = len(nums) - 2
    while(nums[i] >= nums[i+1] and i > -1):
        i -= 1
    if i == -1:
        nums.reverse()
        return    
    j = len(nums) - 1
    while (nums[i] >= nums[j] and i < j):
        j-= 1
    nums[i],nums[j] = nums[j],nums[i]
    nums[i+1:] = nums[i+1:][::-1]



    



