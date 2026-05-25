class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        res = 0
        for op in operations:
            if op == "C":
                records.pop()
            elif op == "D":
                records.append(records[-1]*2)
            elif op == "+":
                records.append(records[-1] + records[-2])
            else:
                records.append(int(op))

        return sum(records)

