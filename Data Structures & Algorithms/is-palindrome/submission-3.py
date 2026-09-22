class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip characters that are not letters or numbers
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1

            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1

            # Compare the characters
            if s[left].lower() != s[right].lower():
                return False

            # Move toward the middle
            left += 1
            right -= 1

        return True

    def isAlphaNumeric(self, c):
        return (
            ('A' <= c <= 'Z') or
            ('a' <= c <= 'z') or
            ('0' <= c <= '9')
        )