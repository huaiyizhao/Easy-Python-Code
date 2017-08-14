#螺旋矩阵II
class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        # Write your code here
        I = [i for i in range (1,n ** 2 + 1)]
        leg = 0
        reg = n - 1 
        aeg = 0
        beg = n - 1
        M = [[0 for i in range(n)] for i in range(n)]
        count = 0
        while (leg < reg) and (aeg < beg):
            for i in range(leg,reg):
                M[aeg][i] = I[count]
                count = count + 1
            for i in range(aeg,beg):
                M[i][reg] = I[count]
                count = count + 1
            for i in range(reg,leg,-1):
                M[beg][i] = I[count]
                count = count + 1
            for i in range(beg,aeg,-1):
                M[i][leg] = I[count]
                count = count + 1
            leg = leg + 1
            reg = reg - 1
            aeg = aeg + 1
            beg = beg - 1
        if leg == reg:
            for i in range(aeg,beg + 1):
                M[i][leg] = I[count]
        if aeg == beg:
            for i in range(leg,reg + 1):
                M[aeg][i] = I[count]
        return M
        