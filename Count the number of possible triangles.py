class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # Step 1: Sort the array to use two-pointer technique
        arr.sort()
        n = len(arr)
        count = 0

        # Fix the third side (largest in the triplet)
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1

            # Use two pointers to find all valid (left, right) pairs
            while left < right:
                # Agar do chhoti sides ka sum > third side hai, toh triangle banega
                if arr[left] + arr[right] > arr[i]:
                    # Sab elements between left and right are valid
                    count += (right - left)
                    right -= 1
                else:
                    left += 1

        return count
