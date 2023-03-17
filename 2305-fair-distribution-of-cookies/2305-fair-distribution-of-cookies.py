class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = inf 
        cookies.sort(reverse = True)
        def faircookies(indx, track):
            nonlocal ans
            if ans <=  max(track):
                return 
            if indx == len(cookies):
                ans = min(ans, max(track))
                return 
            for child in range(k):
                track[child] += cookies[indx]
                faircookies(indx+1, track)
                track[child] -= cookies[indx]
        faircookies(0, [0]*k)
        return ans
        
        