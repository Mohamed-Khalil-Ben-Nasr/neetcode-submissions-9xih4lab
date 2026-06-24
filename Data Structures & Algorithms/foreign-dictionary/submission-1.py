from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        nodeToChildren = defaultdict(set)
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            # catch invalid orderings
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            # the strings in words are sorted lexicographically 
            for i in range(minLen):
                # if the characters dont match
                if w1[i] != w2[i]:
                    nodeToChildren[w1[i]].add(w2[i])
                    break
        res = []
        visited = set()
        processed = set()
        def dfs(node):
            # add cycle detection just in case
            # if we came back to a node that we previously visited
            # but hasnt been finished/processed yet
            # that means there is a cycle
            if node in processed:
                return True
            if node in visited:
                return False
            # mark the current node as visited
            visited.add(node)
            # explore its children
            for child in nodeToChildren[node]:
                if not dfs(child):
                    return False
            # we finished exploring the current node's children
            # => this node is processed
            processed.add(node)
            res.append(node)
            return True
        
        allChars = "".join(words)
        for c in allChars:
            if c not in visited:
                if not dfs(c):
                    return ""
        
        return "".join(reversed(res))
