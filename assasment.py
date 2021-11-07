
class Transform:

    def above_below(self, num_list, int):
        res = dict()
        try:
            indx = num_list.index(int)
        except ValueError:
            return "integer not found"

        res["above"] = (len(num_list) - 1) - indx
        res['below'] = indx
        return res

    def string_rotation(self, str, num):
        if num > len(str):
            return f'Enter a number less than {len(str)}'

        str_list = list(str)
        res = list()

        for i in range(len(str_list) - num):
            char = str_list[i]
            res.append(char)

        remaining = str_list[len(str_list)-num: len(str_list)]
        combined = remaining + res

        return (''.join(combined))


new_dict = Transform()

print(new_dict.above_below([1, 2, 3, 4, 5, 6], 3))
print(new_dict.string_rotation("MyString", 2))
