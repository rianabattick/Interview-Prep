class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #split list at k+1
        #reverse first half

        first_half = nums[0:k+1]
        second_half = nums[k+1:]

        second_half[::-1]
        return second_half + first_half





        

        
