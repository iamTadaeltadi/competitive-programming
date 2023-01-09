class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        d={}
        num1=num1.split("+")
        num2=num2.split("+")
        num1+=num2
        
        for i in range(len(num1)):
            if i==1 or i==3:
                d[i]=int(num1[i][:-1])
            else:
                d[i]=int(num1[i])
        print(d)
        res=str(d[0]*d[2]+ d[1]*d[3]*-1)+ "+" + str(d[0]*d[3]+d[1]*d[2])+"i"
        return res
        
            
            