class Solution:
    def numUniqueEmails(self, emails):
        mail_address_map = {}
        for orig_address in emails:
            cleaned_address = []
            plus_flg = False
            domain_flg = False
            for c in orig_address:
                if c != '.' and c != '+' and c != '@':
                    if not plus_flg:
                        cleaned_address.append(c)
                elif c == '.' and domain_flg:
                    cleaned_address.append(c)
                elif c == '+':
                    plus_flg = True
                elif c == '@':
                    plus_flg = False
                    domain_flg = True
                    cleaned_address.append(c)

            mail_address_map[''.join(cleaned_address)] = True

        return len(mail_address_map.keys())


s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com",
                         "test.e.mail+bob.cathy@leetcode.com",
                         "testemail+david@lee.tcode.com"]))

# Sample test case:
#   Input:
#       ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:11:54
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 100 ms, faster than 7.26% of Python3
#       online submissions for Unique Email Addresses.
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Unique Email Addresses.
