from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited, processed = set(), set()

        CtoP = defaultdict(list)
        for pre in prerequisites:
            CtoP[pre[0]].append(pre[1])
        
        def dfs(c):
            # base case
            # this course was already processed 
            # and can be completed successfully without cycles
            if c in processed:
                return True
            # we went back to a visited course that we didnt prove we can complete yet
            # => cycle detected
            if c in visited:
                return False
            
            visited.add(c)
            for pre in CtoP[c]:
                if not dfs(pre):
                    return False
            # this course has been processed
            processed.add(c)
            return True

        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        
        return True

