# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
         left = 1
         right = n
         while left <= right:

             mid = left + (right - left) // 2

             if isBadVersion(mid) == False: #== if a version is not bad, answer will definitely lie after m
                 left = mid + 1 

             else: #== if a version is bad 

                 #we will check (m-1)th number - if it is bad, we will do right = m - 1
                 #if it is good, we will return answer
                 if mid == 1:
                     return mid

                 if isBadVersion(mid-1):
                     right = mid - 1

                 else:
                     return mid
        