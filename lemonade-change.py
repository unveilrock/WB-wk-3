class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for cust in bills:
            if cust == 5:
                fives+=1
            elif cust == 10:
                if fives>0:
                    tens+=1
                    fives-=1
                else:
                    return False
            elif cust == 20:
                if fives >=1 and tens >=1:
                    fives-=1
                    tens-=1
                elif fives >=3:
                    fives -=3
                else:
                    return False
        return True
