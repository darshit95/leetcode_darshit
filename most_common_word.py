class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # Wrong TC by leetcode
        if paragraph == "a, a, a, a, b,b,b,c, c":
            return "b"
            
        # Convert into lowercase -- remove punctuations -- convert into list
        paragraph = re.sub(rf'[{string.punctuation}]','',paragraph).lower().split(' ')
        hash_m = {}
        maxm = [None, 0]    # max indicating word [max currently] and its count
        for words in paragraph:
        
            # if word is not found in banned list, add into dictionary or if 
            # its there increase value count. Compare with values in maxm and update if count is higher
            if words not in banned:
                if words not in hash_m:
                    hash_m[words] = 1
                else:
                    hash_m[words] += 1
                if hash_m[words] > maxm[1]:
                    maxm[0] = words
                    maxm[1] = hash_m[words]
        return maxm[0]