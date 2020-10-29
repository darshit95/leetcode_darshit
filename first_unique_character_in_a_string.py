class Solution:
    def firstUniqChar(self, s: str) -> int:
	
#	Solution 1: Only dict
#        d = {}
        
#        for i in range(len(s)):
#            if s[i] in d:
#                d[s[i]][1] += 1
#            else:
#                d[s[i]] = [i, 1]
#        for ch in s:
#            if d[ch][1] == 1:
#                return d[ch][0]
#        return -1


# Solution 2: Dict and set          
        my_set = set()
        d = {}

        for idx, ch in enumerate(s):
            if ch not in my_set:
                my_set.add(ch)
                d[ch] = idx
            else:
                if ch not in d:
                    continue
                else:
                    del d[ch]
        return min(d.values()) if d else -1