# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans=[]
        seen=set()
        graph=defaultdict(list)

        def preorder(root):
            if not root:
                return 
            left=preorder(root.left)
            right=preorder(root.right)
            if left:
                graph[root.val].append(left)
                graph[left].append(root.val)
            if right:
                graph[root.val].append(right)
                graph[right].append(root.val)
            return root.val
        preorder(root)
        print(graph)










        queue=deque([(target.val,0)])
        while queue:
            for i in range(len(queue)):
                curr,path=queue.popleft()
                
                if path==k:
                    ans.append(curr)
                seen.add(curr)
                for neg in graph[curr]:
                    if neg not in seen:
                        queue.append((neg,path+1))
               
        return ans