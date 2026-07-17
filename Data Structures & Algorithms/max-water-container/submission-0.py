class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a_pt = 0
        b_pt = len(heights)-1
        height_a=heights[a_pt]
        height_b=heights[b_pt]
        max_area = 0

        while a_pt < b_pt:
            height_a=heights[a_pt]
            height_b=heights[b_pt]
            area = min(height_a, height_b) * (b_pt-a_pt)
            if area>max_area:
                max_area = area
            if height_a<height_b:
                a_pt+=1
            elif height_a>height_b:
                b_pt-=1
            elif height_b == height_a:
                a_pt+=1
                b_pt-=1
        return max_area