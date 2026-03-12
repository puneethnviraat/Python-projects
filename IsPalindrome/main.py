import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]', '', s)
        new_List = list(s.lower())
        left,right=0,len(new_List)-1
        palind=True
        while right>left:
            if new_List[left]==new_List[right]:
                left+=1
                right-=1
                palind=True
            else:
               palind=False
               break
        print(palind)
        return palind
Solution.isPalindrome(Solution, "A man, a pn, a canal: Panama"  )