class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        car = [0] * 26
        t = 1
        for i in range(len(tasks)):
            car[ord(tasks[i]) - 65] += 1
        car.sort()
        max = car[25]
        max_idle = n * (max - 1)
        for z in range(24,-1,-1):
            if max_idle==0 or car[z]==0:
                break
            max_idle -= min(max -1, car[z])
        if max_idle > 0:
            return max_idle + len(tasks)
        else:
            return len(tasks)
