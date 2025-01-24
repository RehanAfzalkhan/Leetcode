class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
    
    # Iterate through the array
        for num in nums:
             # Find the index corresponding to the current number
            idx = abs(num) - 1 
            # Subtract 1 because array indices start from 0
             # abs(num) ensures the value is always positive because the array gets modified

        # Check if the value at the calculated index is negative
        
            if nums[idx] < 0:
                output.append(abs(num))  # Duplicate found, add to output
            else:
                nums[idx] = -nums[idx]  # Mark the element as seen
    
        return output