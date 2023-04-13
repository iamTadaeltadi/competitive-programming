"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d=defaultdict(int)
        graph=defaultdict(list)
        for employee in employees:
            print(employee.id)
            d[employee.id]=employee.importance
            graph[employee.id]=employee.subordinates
        stack=[id]
        val=0
        while stack:
            curr=stack.pop()
            val+=d[curr]
            for neg in graph[curr]:
                stack.append(neg)
        return val