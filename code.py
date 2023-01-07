class Solution:
    def reverseBits(self, n):
        return int(format(n,'032b')[::-1], 2) #Binary values start with "0b" the 2 gets rid of that.



