class Solution:
    def isValid(self, s: str) -> bool:
        lib = []
        dict = {"}":"{", ")":"(", "]":"["}
        for i in s:
            if i in dict.values():
                lib.append(i)
            elif i in dict.keys():
                if lib == [] or dict[i] != lib.pop():
                    return False
            else:
                return False
        return lib == []