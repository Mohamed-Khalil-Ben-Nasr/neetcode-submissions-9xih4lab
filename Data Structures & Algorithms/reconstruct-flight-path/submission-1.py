class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort the edges lexicographically
        # => dfs will always start with smaller lexical order
        tickets.sort()
        # create adjacency list
        nodeToNeis = defaultdict(list)
        nodeToUsed = {}
        for s, d in tickets:
            nodeToNeis[s].append(d)
            if s not in nodeToUsed:
                nodeToUsed[s] = defaultdict(int)
            nodeToUsed[s][d] += 1

        res = ["JFK"]
        def dfs(source):
            # we visited every node
            # => valid itinerary => success
            if len(res) == len(tickets)+1:
                return True
            # if dfs gets stuck and we still didnt visit every node
            # => failure
            if source not in nodeToNeis:
                return False

            for nei in nodeToNeis[source]:
                if nodeToUsed[source][nei] > 0:
                    res.append(nei)
                    nodeToUsed[source][nei] -= 1
                    if dfs(nei):
                        return True
                    # invalid itinerary => backtrack
                    res.pop()
                    nodeToUsed[source][nei] += 1
            return False          
        
        dfs("JFK")
        return res