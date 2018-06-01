###
# Stack
# Time Complexity: O(n) + O(aloga)
# Space Complexity: O(a)
###
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stk = []
        curmap = collections.Counter()
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stk.append(curmap)
                curmap = collections.Counter()
            elif formula[i] == ')':
                i += 1
                s = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                num = int(formula[s:i] or 1)
                i -= 1
                tmp = stk.pop()
                for name, cnt in curmap.iteritems():
                    tmp[name] += cnt * num
                curmap = tmp
            else:
                s = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                name = formula[s:i]
                s = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                num = int(formula[s:i] or 1)
                i -= 1
                curmap[name] += num
            i += 1
        re = ""
        for name, cnt in sorted(curmap.iteritems()):
            re += name
            if cnt > 1:
                re += str(cnt)
        return re
                    
                                        
                            
                    