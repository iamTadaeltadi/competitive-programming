class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return float((sum(salary)-(max(salary)+min(salary))))/(len(salary)-2)