class UndergroundSystem:

    def __init__(self):
        

        self.check = defaultdict(list)
        self.average = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.check[id] = [stationName,t]


    def checkOut(self, id: int, stationName: str, t: int) -> None:

        stationName_from, time_first= self.check[id]
        
        self.average[(stationName_from,stationName)].append(t-time_first)
        

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.average[(startStation,endStation)])/len(self.average[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)