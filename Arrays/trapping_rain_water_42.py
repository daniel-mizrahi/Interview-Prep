class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        max_height = max(height)
        max_index = height.index(max(height))
        left, right = 0, len(height) - 1
        total = 0
        while left != max_index:
            h = height[left]
            left += 1
            while h >= height[left] and left != max_index:
                total += h - height[left]
                left += 1
        while right != max_index:
            h = height[right]
            right -= 1
            while h >= height[right] and right != max_index:
                total += h - height[right]
                right -= 1
        return total
