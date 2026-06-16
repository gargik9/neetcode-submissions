class Solution:

    def monotone_stack(self, arr):
        next_smallest = [len(arr) for _ in range(len(arr))]
        st = []
        for idx, elem in enumerate(arr):
            while len(st) > 0 and elem < st[-1][1]:
                pop_idx, _ = st.pop()
                next_smallest[pop_idx] = idx
            st.append((idx, elem))
        return next_smallest
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        nl_right = self.monotone_stack(heights)
        nl_left = self.monotone_stack(heights[::-1])[::-1]
        nl_left = [(len(heights) - 1 - i) for i in nl_left]

        ans = 0
        for i in range(len(heights)):
            ans = max(ans, heights[i] * (nl_right[i] - nl_left[i] - 1))
        
        return ans