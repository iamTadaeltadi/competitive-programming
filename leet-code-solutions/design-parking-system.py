class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        
        self.park=[big,medium,small]
    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType==1 and self.park[0]>0:
            self.park[0]-=1
            return True
        elif carType==2 and self.park[1]>0:
            self.park[1]-=1
            return True
        elif carType==3 and self.park[2]>0:
            self.park[2]-=1
            return True
        else:
            return False
            
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)