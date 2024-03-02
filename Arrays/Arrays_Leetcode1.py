class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:   

        #answer[0] in num1 but not num2
        #answer[1] in num2 but not num1
        #loop thru array 1
        #check if element in array two
        #if yes add to answer[0] list
        #loop thru array 2
        #check if elementin array 1
        #if yes add to answer[1] list

        answer1 = []
        answer2 = []
        final_ans = []

        for num in nums1:
            if (num not in nums2) and (num not in answer1):
                answer1.append(num)

        for num in nums2:
            if (num not in nums1) and (num not in answer2):
                answer2.append(num)

        final_ans.append(answer1)
        final_ans.append(answer2)

        return final_ans
