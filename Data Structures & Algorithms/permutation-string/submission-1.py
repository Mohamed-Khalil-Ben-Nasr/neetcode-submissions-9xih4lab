from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # optimization: when im moving the sliding window, i can keep the same 
        # substring dictionary but only remove the character thats no longer in the window
        # and add the new character that joined the window
        d1 = defaultdict(int)
        for c in s1:
            d1[c] += 1
        d2 = defaultdict(int)
        for i in range(0, len(s2)-len(s1)+1):
            # initialize the substring charToFreq dictionary
            if i == 0:
                for c in s2[i:i+len(s1)]:
                    d2[c] += 1
            else:
                # add the current new char
                # since we are gonna expand the window from the right
                d2[s2[i + len(s1)-1]] += 1
            # check if match
            match = True
            for c in d2:
                if d2[c] != d1[c]:
                    match = False
            if match:
                return True
            # no match => so remove current s2[i] since 
            # its gonna be out of the substring window in the next iteration
            # since we are gonna shrink the window from the left
            d2[s2[i]] -= 1
        return False

