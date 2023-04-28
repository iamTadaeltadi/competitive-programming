class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        self.visted = set()
        
        for i in range(n-1):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        steps, boolean = self.dfs(0, graph, self.visted, hasApple)
        if steps!=0:
            return steps-2
        else:
            return steps
    def dfs(self, node, graph, visited, hasApple):


        found_apple_in_this_sub_tree = hasApple[node]
        cur_steps = 0

        if node in self.visted:
            return 0, False
        
        
        self.visted.add(node)

        for neigh in graph[node]:
            steps_for_this_neigh, boolean_for_this_neigh = self.dfs(neigh, graph, visited, hasApple)

            cur_steps +=steps_for_this_neigh
            found_apple_in_this_sub_tree = found_apple_in_this_sub_tree or boolean_for_this_neigh
        
        if found_apple_in_this_sub_tree:
            cur_steps += 2


        
        return cur_steps, found_apple_in_this_sub_tree