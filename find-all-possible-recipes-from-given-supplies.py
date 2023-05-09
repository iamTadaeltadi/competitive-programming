class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        incoming=[0]*len(recipes)
        supply=set(supplies)
        r=set(recipes)
        queue=deque()
        result=[]
        idx_recipe={}
        graph=defaultdict(list)

        for i,v in enumerate(recipes):
            canICreate=True
            idx_recipe[v]=i

            for ingr in ingredients[i]:
                
                if ingr  not in supply:
                    incoming[i]+=1
                    canICreate=False

            if canICreate:
                queue.append(v)
       
        
        for idx,rec in enumerate(recipes):

            for ingr in ingredients[idx]:

                if ingr in r:
                    graph[ingr].append(rec)
        
        while queue:

            curr=queue.popleft()
            result.append(curr)

            for neg in graph[curr]:

                incoming[idx_recipe[neg]]-=1

                if incoming[idx_recipe[neg]]==0:
                    queue.append(neg)

        return result