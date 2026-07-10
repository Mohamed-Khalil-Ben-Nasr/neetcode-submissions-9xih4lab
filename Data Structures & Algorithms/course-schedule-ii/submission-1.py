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
            # if node was visited and we came back to it and 
            # its still not processed
            # => cycle
            # => impossible to finish all courses
            if i in visited and i not in processed:
                return False
            # mark current node as visited
            visited.add(i)
            # explore its children
            for pre in courseToPre[i]:
                if pre not in processed:
                    if not dfs(pre):
                        return False
            # once we finish exploring children
            # => we finished processing this node
            # => add it to the stack which will hold prereqs in order
            processed.add(i)
            stack.append(i)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        return stack
