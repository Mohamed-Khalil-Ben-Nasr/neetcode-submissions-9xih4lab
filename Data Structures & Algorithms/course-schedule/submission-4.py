class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect cycle using topological sort

        # adjacency map
        courseToPrereqs = defaultdict(list)
        for a, b in prerequisites:
            courseToPrereqs[a].append(b)
        
        visited = set()
        processed = set()

        def dfs(course):
            if course in processed:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)

            for pre in courseToPrereqs[course]:
                if not dfs(pre):
                    return False
            
            processed.add(course)

            return True


        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        
        return True


