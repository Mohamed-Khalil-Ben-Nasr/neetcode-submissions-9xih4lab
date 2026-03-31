class Solution:

    def encode(self, strs):
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str
    
    def decode(self, encoded_str):
        result = []
        i = 0
        while (i < len(encoded_str)):
            j = i
            # find the delimiter "#" cuz the length might be more than one digit
            while encoded_str[j] != "#":
                j += 1
            # get curr length of the encoded str
            curr_str_length = int(encoded_str[i:j])
            # move to first character of the str
            i = j + 1
            # create curr_str
            curr_str = encoded_str[ i: (i + curr_str_length)]
            result.append(curr_str)
            # move i to first character after end of current string == # if there is one more str
            i += curr_str_length
        return result






    

