class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        match_idx = 0
        star_idx = -1

        while s_ptr < len(s):
            # 1. Characters match or pattern has '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == "?"):
                s_ptr += 1
                p_ptr += 1

            # 2. Pattern has '*' -> Record position and try matching 0 characters first
            elif p_ptr < len(p) and p[p_ptr] == "*":
                star_idx = p_ptr
                match_idx = s_ptr
                p_ptr += 1

            # 3. Last pattern pointer was '*', advance string pointer to try matching more
            elif star_idx != -1:
                p_ptr = star_idx + 1
                match_idx += 1
                s_ptr = match_idx

            # 4. No match and no active '*' pointer
            else:
                return False

        # Check for remaining trailing stars in pattern
        while p_ptr < len(p) and p[p_ptr] == "*":
            p_ptr += 1

        return p_ptr == len(p)
