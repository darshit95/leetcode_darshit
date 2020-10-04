class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # create hash_map with key:value as {alphabet : index}
        
        hash_m = {c:i for i,c in enumerate(order)}
        
        for x in range(1,len(words)):
            
            # compare words[i] and words[i-1]
            first = words[x-1]
            second = words[x]
            i, j = 0, 0
            while i < len(first) and j < len(second):
                
                # if letter in first word > same index letter in second word, they are not in
                # order
                if hash_m[first[i]] > hash_m[second[j]]:
                    return False
                
                # if corresponding index chars are same, move on to next indexes
                # and compare again
                elif hash_m[first[i]] == hash_m[second[j]]:
                    i += 1
                    j += 1
                
                # if letter in first word < same index letter in second word, they are in 
                # order 
                else:
                    break
            if i < len(first) and j >= len(second):
                return False
        return True