class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for i in range(len(strs)):
            new_str = ','.join([str(ord(c)) for c in strs[i]])
            res = res + ":" + new_str

        return res

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if len(s) == 0:
            return []
        if s == ":":
            return [""]

        enc_strs = s.split(':')
        res = []
        for i in range(1, len(enc_strs)):
            if len(enc_strs[i]) == 0:
                res.append("")
                continue

            res_str = ''.join(
                [chr(int(ord_num)) for ord_num in enc_strs[i].split(',')])
            res.append(res_str)

        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
codec = Codec()
print("*** [] ***")
enc_str = codec.encode("[]")
dec_strs = codec.decode(enc_str)
print(enc_str, dec_strs)

# Sample test case:
#   Input:
#       See the site
#   Output:
#       See the site

# Performance Result:
#   Coding Time: 00:24:45
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 328 ms, faster than 7.78% of Python3
#       online submissions for Encode and Decode Strings.
#   Memory Usage: 13.9 MB, less than 100.00% of Python3
#       online submissions for Encode and Decode Strings.
