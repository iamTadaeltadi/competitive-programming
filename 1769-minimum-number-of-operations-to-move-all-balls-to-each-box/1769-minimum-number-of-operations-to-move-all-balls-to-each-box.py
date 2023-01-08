class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        d={}
        listt=[]
        for i in range(len(boxes)):
            if boxes[i] =="1":
                d[i]=int(i)
        c_b=0
        c_a=len(d)
        tot_b=sum(d.values())
        tot_a=0
        for i in range(len(boxes)):
            if boxes[i]=="1":
                c_a-=1
                tot_b-=i
            listt.append((tot_b-c_a*i) + (i*c_b-tot_a))
            if boxes[i]=="1":
                c_b+=1
                tot_a+=i
            
        return listt