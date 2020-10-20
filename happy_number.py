class Solution:
    def isHappy(self, n: int) -> bool:
        my_set = set()      # set to track all square additions upto current point
        while n != 1:       # loop until n (sum of squares) is one
            summ = 0
            if n in my_set:     # if n (summ) is in set, means sum is already encountered before and there is cycle
                return False
            my_set.add(n)       # if not there in set, add in set
            for num in str(n):
                summ += int(num)**2
            n = summ            # make n as sum to continue the loop
        return True
