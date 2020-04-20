class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)


# Performance Result:
#   Coding Time: 00:13:24
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 53.56%
#   Memory Usage: 13.9 MB, less than 6.25%
