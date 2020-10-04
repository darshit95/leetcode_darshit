class Solution(object):
    def isValid(self, br_str):
        class Stack():
            def __init__(self):
                self.items = []
                
            def isEmpty(self):
                return self.items == []
            
            def push(self, item):
                self.items.append(item)
                
            def pop(self):
                return self.items.pop()
            
            def peek(self):
                return self.items[len(self.items)-1]
            
            def size(self):
                return len(self.items)
            
        s = Stack()
        for braces in br_str : 
            if braces == "(" or braces == "{" or braces == "[" :
                s.push(braces)
        
            elif braces == ")":
                if s.isEmpty(): 
                    return False
                brc = s.pop()
                if brc != "(" :
                    return False
            elif braces == "}":
                if s.isEmpty(): 
                    return False
                brc = s.pop()
                if brc != "{" :
                    return False
            elif braces == "]":
                if s.isEmpty(): 
                    return False
                brc = s.pop()
                if brc != "[" :
                    return False
        
        if s.isEmpty(): 
            return True
        else :
            return False
                    
                          
                          
                
        """
        :type s: str
        :rtype: bool
        """
        