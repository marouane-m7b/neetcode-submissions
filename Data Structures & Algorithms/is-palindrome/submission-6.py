class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringArray = list(s.lower())
        check = []

        for st in stringArray:
            if st.isalnum():
                check.append(st)
                
        return check == check[::-1]