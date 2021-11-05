class Transform:

    def above_below(self, numArr, int):
        res = dict()
        try:
            indx = numArr.index(int)
        except ValueError:
            return "integer not found"

        res["above"] = (len(numArr) - 1) - indx
        res['below'] = indx
        return res

    def string


new_dict = Transform()
print(new_dict.above_below([1, 2, 3, 4, 5, 6], 3))
print(new_dict.above_below([1, 2, 3, 4, 5, 6], 1))
print(new_dict.above_below([1, 2, 3, 4, 5, 6], 6))
print(new_dict.above_below([1, 2, 3, 4, 5, 6], -1))
