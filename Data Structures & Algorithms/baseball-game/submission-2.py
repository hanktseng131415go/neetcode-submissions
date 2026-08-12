class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out = []
        for o in operations:
            if o == "+":
                out.append(sum(out[-2:]))
            elif o == "D":
                out.append(2*out[-1])
            elif o == "C":
                out.pop()
            else:
                out.append(int(o))
        
        return sum(out)