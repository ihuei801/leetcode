###
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        unit = "Thousand Million Billion".split()
        i = 0
        words = []
        while num:
            word = self.gen_num(num%1000) 
            if word:
                word += " " + unit[i-1] if i else "" 
                words.append(word)
            num /= 1000
            i += 1
            
        return ' '.join(words[::-1])
        
    def gen_num(self, num) :
        s_19 = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        s_tens = "N N Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        re = ""
        if num > 99:
            re += s_19[num/100] + " Hundred "
            num %= 100
        if num > 19:
            re += s_tens[num/10] + " "
            num %= 10
        if num:
            re += s_19[num]
        return re.strip()
        