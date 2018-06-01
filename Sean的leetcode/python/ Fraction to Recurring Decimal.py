###
# Math
# Time Complexity: O(n) num of times doing long division
# Space Complexity: O(n)
###
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        re = ""
        if (numerator < 0) ^ (denominator < 0):
            re += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        re += str(numerator / denominator)
        rmd = numerator % denominator
        if rmd == 0:
            return re
        re += "."
        d = dict()
        while rmd:         
            if rmd in d:
                re = re[:d[rmd]] + "(" + re[d[rmd]:]
                re += ")"
                break
            d[rmd] = len(re)
            re += str(rmd * 10 / denominator)
            rmd = rmd * 10 % denominator
        return re
                                        
                            
                    