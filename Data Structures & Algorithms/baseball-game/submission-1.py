class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                one = record.pop()
                two = record.pop()
                s = one + two
                record.append(two)
                record.append(one)
                record.append(s)
            elif op == "D":
                new = record[-1] * 2
                record.append(new)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
            print(record)
        res = 0
        for sc in record:
            res += sc
        return res