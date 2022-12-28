class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        sumof=sum(salary)
        max_val=(max(salary))
        min_val=min(salary)
        result =float(sumof-(max_val+min_val))/(len(salary)-2)
        return result