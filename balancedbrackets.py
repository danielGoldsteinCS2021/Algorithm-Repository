########################
# Daniel Goldstein
# balanced brackets
# June 12th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################
'''
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
'''

class Stack:
    def __init__(self):
        self.stk = []
    def push(self, item):
        self.stk.append(item)
    def pop(self):
        return self.stk.pop()
    def peak(self):
        if (self.isEmpty()):
            return None
        return self.stk[len(self.stk)-1]
    def isEmpty(self):
        return len(self.stk)==0
    def __str__(self):
        return str(self.stk)

def isBalanced(brcks):
    s1, s2 = Stack(), Stack()
    for i in brcks:
        s1.push(i)
    for j in brcks:
        x = s1.pop()
        if (x in [']', ')', '}']):
            s2.push(x)
        elif (s2.peak() == ']' and x == '['):
            s2.pop()
        elif (s2.peak() == ')' and x =='('):
            s2.pop()
        elif (s2.peak() == '}' and x =='{'):
            s2.pop()
        else:
            return False
    return s2.isEmpty()

# TEST CASES #
print("Is ([])[]({}) balanced? \n", isBalanced("([])[]({})"))
print("Is [] balanced? \n", isBalanced("[]"))
print("Is {} balanced? \n", isBalanced("{}"))
print("Is () balanced? \n", isBalanced("()"))
print("Is ([{{{{}}}}])()()[]({})([])({{[(())]}}) balanced? \n", isBalanced("([{{{{}}}}])()()[]({})([])({{[(())]}})"))
print("Is ([{} balanced? \n", isBalanced("([{}"))
print("Is ([]){}) balanced? \n", isBalanced(" ([]){})"))
print("Is ([)[] balanced? \n", isBalanced("([)[]"))
print("Is )[])[]({}) balanced? \n", isBalanced(")[])[]({})"))
print("Is ( balanced? \n", isBalanced("("))
print("Is ) balanced? \n", isBalanced(")"))
print("Is ()[ balanced? \n", isBalanced("()["))
print("Is (] balanced? \n", isBalanced("(]"))
print("Is (])] balanced? \n", isBalanced("([)]"))
print("Is ((() balanced? \n", isBalanced("((()"))
