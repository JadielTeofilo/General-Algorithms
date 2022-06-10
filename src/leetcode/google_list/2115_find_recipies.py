"""
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

recipies: List[str]

ingredients: List[List[str]]

supplies: List[str]



a: b c
b: 1
c: 2
d: a f
f: d


we can create a recipe if there is no cycle dependency in its ingredients

create a graph from recipies 

graph: Dict[str, Set[str]]

keep a set of supplies

supplies: Set[str]

keep a visited and global_visited

iterate on the recipies for each of them try to find a cycle
if no cycle, add to result


O(R*I) time complexity
O(S + R*I) space complexity where I is the max num of ingredients for a given recipe


"""
import collections
from typing import Dict, Set


Graph = Dict[str, Set[str]]


def build_graph(recipies: List[str], ingredients: List[str]) -> Graph:
    graph: Graph = collections.defaultdict(set)
    for recipe, curr_ingredients in zip(recipies, ingredients):
        for ingredient in curr_ingredients:
            graph[recipe].add(ingredient)
    return graph


class Solution:
    def findAllRecipes(self, recipes: List[str], 
                       ingredients: List[List[str]], 
                       supplies: List[str]) -> List[str]:
        graph: Graph = build_graph(recipes, ingredients)
        supplies_cache: Set[str] = set(supplies)
        global_visited: Dict[str, bool] = dict()
        result: List[str] = []
        for recipe in recipes:
            visited: Set[str] = set()
            if not self.has_cycle(graph, recipe, visited, 
                                  global_visited, supplies_cache):  
                result.append(recipe)
        return result

    def has_cycle(self, graph: Graph, recipe: str, visited: Set[str], 
                  global_visited: Dict[str, bool], supplies_cache: Set[str]) -> bool:
        if recipe in visited:
            return True
        if recipe in global_visited: 
            return global_visited[recipe]
        if recipe in supplies_cache:
            return False
        visited.add(recipe)
        for ingredient in graph[recipe]:
            if self.has_cycle(graph, ingredient, visited, 
                              global_visited, supplies_cache):
                global_visited[recipe] = True
                return True
        global_visited[recipe] = False 
        visited.remove(recipe)
        return False

