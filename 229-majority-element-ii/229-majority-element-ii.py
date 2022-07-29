class Solution:
    def majorityElement(self, num: List[int]) -> List[int]:
        num1 = -1
        num2 = -2
        count1 = 0
        count2 = 0
        length = len(num)
        for x in range(length):
            if(num[x] == num1):
                count1+=1
            elif(num[x] == num2):
                count2+=1
            elif(count1 == 0):
                num1 = num[x]
                count1 = 1
            elif(count2 == 0):
                num2 = num[x]
                count2 = 1
            else:
                count1-=1
                count2-=1
        array_list = []
        count1 = 0
        count2 = 0
        for y in range(length):
            if(num[y] == num1):
                count1+=1
            elif(num[y] == num2):
                count2+=1
        if(count1 > length/3):
            array_list.append(num1)
        if(count2 > length/3):
            array_list.append(num2)
        return array_list