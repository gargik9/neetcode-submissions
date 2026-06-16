class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        thresh = n/3

        map1 = defaultdict(int)
        seen  = set()
        for num in nums:

            map1[num]+=1

            if map1[num]>thresh:

                seen.add(num)

        return list(seen)


