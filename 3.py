#判断一个字符串是否是另一个字符串的置换
class Solution(object):
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        if(len(A) != len(B)):
            return False
        for i in range(len(A)):
            if B.find(A[i]) >= 0:
                B = B[:B.find(A[i])] + B[(B.find(A[i]) + 1) :]
            else:
                return False
        return True
        
        # write your code here