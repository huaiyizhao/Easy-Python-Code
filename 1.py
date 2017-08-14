#螺旋矩阵
class Solution:
    """
    @param: : a matrix of m x n elements
    @return: an integer list
    """

    def spiralOrder(self, matrix):
        # write your code here
        if matrix == []:
            return []
        m = len(matrix)
        n = len(matrix[0])
        I = []
        leg = 0
        reg = n - 1
        aeg = 0
        beg = m - 1
        while (leg < reg) and (aeg < beg):
            for i in range(leg, reg):
                I.append(matrix[aeg][i])
            for i in range(aeg, beg):
                I.append(matrix[i][reg])
            for i in range(reg, leg, -1):
                I.append(matrix[beg][i])
            for i in range(beg, aeg, -1):
                I.append(matrix[i][leg])
            leg = leg + 1
            reg = reg - 1
            aeg = aeg + 1
            beg = beg - 1
        if leg == reg:
            for i in range(aeg, beg + 1):
                I.append(matrix[i][leg])
        elif aeg == beg:
            for i in range(leg, reg + 1):
                I.append(matrix[aeg][i])
        return I
            