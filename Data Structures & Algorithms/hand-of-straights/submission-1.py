class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        numGroupsNeeded = len(hand) // groupSize

        cardToCount = defaultdict(int)
        minHeap = []
        heapq.heapify(minHeap)
        for i, card in enumerate(hand):
            cardToCount[card] += 1
            heapq.heappush(minHeap, card)
        
        validGroupsFormed = 0
        print("num needed ", numGroupsNeeded)
        print("cardToCount ", cardToCount)
        while validGroupsFormed < numGroupsNeeded:
            # always pick the minimum available card to start the group 
            # => this is the greedy insight
            # pop the min from heap 
            # => only pop once from minHeap to get the start of each group
            
            curStart = heapq.heappop(minHeap)

            # this was already used while building another group
            if cardToCount[curStart] == 0:
                continue
            cardToCount[curStart] -= 1
            curGroupSize = 1
            curGroup = [curStart]
            while curGroupSize < groupSize:
                # we cant form the current group
                if (curStart+1 not in cardToCount or 
                cardToCount[curStart+1]  == 0):
                    print("invalid curGroup ", curGroup)
                    print("curStart ", curStart)
                    print("curStart+1 cant be used/found => return false")
                    return False
                curStart += 1
                curGroup.append(curStart)
                cardToCount[curStart] -= 1
                curGroupSize += 1
            print("valid curGroup ", curGroup)
            validGroupsFormed += 1
        
        return True


