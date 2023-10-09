class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        deq = collections.deque([(root, 1)])
        max_w = 0
        
        while deq:
		    # update max_width if there are more then one element on the current level
            if deq[0][1] != deq[-1][1]:
                max_w = max(max_w, (1 + deq[-1][1] - deq[0][1]))
            for i in range(len(deq)):
                node, cur = deq.popleft() # pop current node and current position on the level of a tree 
                if node.left: 
                    deq.append((node.left, cur * 2 - 1))   # left node always odd
                if node.right: 
                    deq.append((node.right, cur * 2))   # right node always even
                    
        return max(1, max_w)