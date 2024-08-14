class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        
        def count_pairs(mid):
            count, left = 0, 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        low, high = 0, nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low

# # Exemplos de uso
# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.smallestDistancePair([1, 3, 1], 1))
#     print(solution.smallestDistancePair([1, 1, 1], 2))
#     print(solution.smallestDistancePair([1, 6, 1], 3))
