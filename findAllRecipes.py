class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
      
        supplies = set(supplies)
        dependency = {}
        indegrees =  {}
        for i,recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    indegrees[recipe] = indegrees.get(recipe,0) + 1
                    dependency[ingredient] = dependency.get(ingredient,[]) + [recipe]
                    
        queue = deque()
        for recipe in recipes:
            if recipe not in indegrees:
                queue.append(recipe)
        res = []
        while queue:
            recipe = queue.popleft()
            res.append(recipe)
            deps = dependency.get(recipe,[])
            for dep in deps:
                indegrees[dep] -= 1 
                if indegrees[dep] == 0:
                    queue.append(dep)
        return res
            
