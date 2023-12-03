class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        answer = [ [1]]

        def generatePascal(row, rowArr):

            if row == numRows:
                return rowArr

            newArr = [1]

            for i in range(1, len(rowArr)):
                newArr.append(rowArr[i] + rowArr[i-1])

            newArr.append(1)
            answer.append(newArr)

            return generatePascal(row+1, newArr)

        generatePascal(1, [1])

        return answer