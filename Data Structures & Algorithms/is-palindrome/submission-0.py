class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringArray = list(s.lower())

        for st in stringArray:
            if not st.isalpha():
                stringArray.remove(st)

        return stringArray == stringArray[::-1]