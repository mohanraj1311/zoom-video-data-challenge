class Solution(object):
    def reverse(self, nums, start, end):
        if nums is None:
            return nums

        while (start >= 0 and end < len(nums) and start < end):

            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            end = end - 1
            start = start + 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return nums
        if k is 0:
            return nums
        k = k % len(nums)
        start = 0
        end = len(nums) - 1

        self.reverse(nums, start, end)
        #print st

        self.reverse(nums, start, k - 1)
        self.reverse(nums, k, end)

        return nums

def main():
    sol_obj = Solution()
    res = sol_obj.rotate([1,2,3,4,5], 2)
    print res

if __name__=='__main__':
    main()