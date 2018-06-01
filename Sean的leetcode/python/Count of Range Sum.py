###
# Merge Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(logn) + O(n)
###
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
        return self.merge_sort(sums, 0, len(sums), lower, upper)
    def merge_sort(self, sums, start, end, lower, upper):
        if end - start <= 1:
            return 0
        mid = (start + end) / 2
        cnt = self.merge_sort(sums, start, mid, lower, upper) + self.merge_sort(sums, mid, end, lower, upper)
        l = mid
        r = mid
        for left in sums[start:mid]:
            while l < end and sums[l] - left < lower:
                l += 1
            while r < end and sums[r] - left <= upper:
                r += 1
            cnt += r - l
        sums[start:end] = sorted(sums[start:end]) #use TimSort to sort the already sorted two subarray, O(n)
        return cnt
                                        
                            
                    