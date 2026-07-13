class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        b1=int(a,2)
        b2=int(b,2)
        c=b1+b2
        return bin(c)[2:]
        