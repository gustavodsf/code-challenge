import re

class Solution:
    def reverseWords(self, s: str) -> str:
        cleanedTxt: str = re.sub(r'\s+', ' ', s).strip()
        parts: List[str] = cleanedTxt.split()
        parts.reverse()
        return " ".join(parts)


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))