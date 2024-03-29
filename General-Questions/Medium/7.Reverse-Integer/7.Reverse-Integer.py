class Solution:
    def reverse(self, x: int) -> int:

        temp = str(x)
        hasMinus = False
        newValue = ''

        if '-' in temp:
            temp = temp.replace('-','')
            hasMinus = True
            
        list1 = [int(num) for num in temp]

        list1.reverse()

        newValue = ''.join(map(str, list1))

        if(hasMinus):
            newValue = '-' + newValue
        
        newValue = int(newValue)

        if newValue > ((2 ** 31) - 1) or newValue < -(2 ** 31):
            return 0

        return newValue




        return newValue