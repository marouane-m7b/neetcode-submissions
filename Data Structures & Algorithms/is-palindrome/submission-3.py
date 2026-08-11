class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringArray = list(s.lower().replace(" ", ""))

        for st in stringArray:
            if not st.isalnum():
                stringArray.remove(st)
                
        print(stringArray)
        print(stringArray[::-1])
        return stringArray == stringArray[::-1]