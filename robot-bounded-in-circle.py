class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        initial_pos = curr_pos = [0, 0]
        directions = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0]
        }
        nesw = ['N', 'E', 'S', 'W']
        dir = 'N'
        for i in range(len(instructions)):
            if instructions[i] == 'G':
                curr_pos = [x + y for x, y in zip(curr_pos, directions[dir])]
            elif instructions[i] == 'L':
                dir = nesw[(nesw.index(dir) - 1) % len(nesw)]
            elif instructions[i] == 'R':
                dir = nesw[(nesw.index(dir) + 1) % len(nesw)]
        return initial_pos == curr_pos or dir != 'N'