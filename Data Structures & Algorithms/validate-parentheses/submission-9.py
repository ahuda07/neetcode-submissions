class Solution:
    def isValid(self, s: str) -> bool:
        # looking at this problem i can tell we are specifically looking pattern matching and managing states of the parenthesis
        # so every open bracket is closed by the same type of close bracket
        # so an exmaple of a flase solution would be )(
        # a base case to sniff out a false solution is to check if the first parenthesis is an open (,{,[
        # idk a brute foce solution
        # an optimized solution would be to use a stack, keeping track of the current element and the top element
        # if they correspond you can pop the element
        # if they dont correspond, then you would return false 
        # this solution is o(n) time and o(n) space because we are going throught the string once of size n and creating
        # a stack of size n
        stack = []
        for char in s:
            if len(s) == 1:
                return False
            if char in "{[(":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:  
                    topElement = stack[-1]
                    if char == "}" and topElement == "{":
                        stack.pop()
                    elif char == "]" and topElement == "[":
                        stack.pop()
                    elif char == ")" and topElement  == "(":
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0