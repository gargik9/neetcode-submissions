class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = Counter(hand)

        for c in sorted(count):

            m = count[c]

            if m==0:
                continue

            for j in range(c,groupSize+c):
                count[j]-=m
                if count[j]<0:
                    return False

        return True
        