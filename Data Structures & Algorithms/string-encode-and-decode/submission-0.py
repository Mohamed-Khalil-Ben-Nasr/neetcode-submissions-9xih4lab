class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""

        for s in strs:
            encoding += str(len(s)) + "#" + s

        return encoding 

    def decode(self, s: str) -> List[str]:
        decoding = []
        print(s)
        i = 0
        while i < len(s):
            j = i
            # find the delimiter # thats right after the length of the str
            while s[j] != "#":
                j += 1
            # once we found the delimiter
            length = int(s[i:j])
            # we move past the delimiter #
            i = j + 1
            # slice out the str from s 
            decoding.append(s[i:i+length])
            # update i so that the loop starts reading from the first digit of the length of the next str
            i += length

        return decoding

