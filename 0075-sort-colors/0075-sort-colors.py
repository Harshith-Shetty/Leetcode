class Solution(object):
    
    
        # merge sort
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        # Loop until subarrays are exhausted
        while left <= mid and right <= high:
            # Compare left and right elements
            if arr[left] <= arr[right]:
                # Add left element to temp
                temp.append(arr[left])
                # Move left pointer
                left += 1
            else:
                # Add right element to temp
                temp.append(arr[right])
                # Move right pointer
                right += 1

        # Adding the remaining elements of left half
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Adding the remaining elements of right half
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Transferring the sorted elements to arr
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    # Helper function to perform merge sort from low to high
    def mergeSortHelper(self, arr, low, high):
        # Base case: if the array has only one element
        if low >= high:
            return
        
        # Find the middle index
        mid = (low + high) // 2
        # Recursively sort the left half
        self.mergeSortHelper(arr, low, mid)
        # Recursively sort the right half
        self.mergeSortHelper(arr, mid + 1, high)
        # Merge the sorted halves
        self.merge(arr, low, mid, high)

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # merge sort
        n = len(nums) # Size of array
        
        # Perform Merge sort on the whole array
        self.mergeSortHelper(nums, 0, n - 1)
        
        # Return the sorted array
        return nums