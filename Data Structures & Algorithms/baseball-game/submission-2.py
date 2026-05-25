class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops_wo_c = []
        res = 0
        for op in operations:
            if op == "C":
                ops_wo_c.pop()
            else:
                ops_wo_c.append(op)
        
        records = []
        for i in range(len(ops_wo_c)):
            if ops_wo_c[i] == "D":
                records.append(int(records[i-1])*2)
            elif ops_wo_c[i] == "+":
                records.append(int(records[i-1]) + int(records[i-2]))
            else:
                records.append(int(ops_wo_c[i]))

        for rec in records:
            res += rec
        return res

