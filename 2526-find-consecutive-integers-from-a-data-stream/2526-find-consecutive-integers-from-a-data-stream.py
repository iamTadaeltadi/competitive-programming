class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.k=k
        self.value=value
        self.count=0

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==self.value:
            self.count+=1
        else:
            self.count=0
        if self.count>=self.k:
            return True
        return False
       

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)