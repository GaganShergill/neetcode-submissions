class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        res = 0
        for op in operations:
            if op == "C":
                res -= records.pop()
            elif op == "D":
                records.append(records[-1]*2)
                res += records[-1]
            elif op == "+":
                records.append(records[-1] + records[-2])
                res += records[-1]
            else:
                records.append(int(op))
                res += records[-1]

        return res

