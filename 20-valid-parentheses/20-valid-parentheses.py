class Solution:
    def isValid(self, s: str) -> bool:
        munch = []

        if len(s) % 2 == 0 and ((s.count("(") + s.count("[") + s.count("{")) == (s.count(")") + s.count("]") + s.count("}"))):
            for i in s:
                if i == "(" or i == "[" or i == "{":
                    munch.append(i)
                if len(munch) != 0:
                    if i == ")" and munch[-1] == "(":
                        munch.pop()
                    elif i == "]" and munch[-1] == "[":
                        munch.pop()
                    elif i == "}" and munch[-1] == "{":
                        munch.pop()
            if len(munch) == 0:
                return True
            else:
                return False

        else:
            return False