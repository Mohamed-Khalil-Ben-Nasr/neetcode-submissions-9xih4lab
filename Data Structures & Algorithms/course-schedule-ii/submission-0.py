from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # template to solving topological sort problems
        # create adjacency list
        courseToPre = defaultdict(list)
        for a,b in prerequisites:
            courseToPre[a].append(b)
        
        visited = set()
        processed = set()
        stack = []
        def dfs(i):
            if i in visited and i not in processed:
                return False
            visited.add(i)
            for pre in courseToPre[i]:
                if pre not in processed:
                    if not dfs(pre):
                        return False
            processed.add(i)
            stack.append(i)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        return stack
