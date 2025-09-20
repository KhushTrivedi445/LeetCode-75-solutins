class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n   # Step 1: Result array, initially filled with 1s

        # Step 2: Left product
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
            # print("Left pass:", answer)

        # Step 3: Right product
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
            # print("Right pass:", answer)

        return answer
