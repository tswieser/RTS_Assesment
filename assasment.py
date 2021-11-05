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
        list_to_str = ' '.join(combined)
        return list_to_str


new_dict = Transform()
# print(new_dict.above_below([1, 2, 3, 4, 5, 6], 3))
# print(new_dict.above_below([1, 2, 3, 4, 5, 6], 1))
# print(new_dict.above_below([1, 2, 3, 4, 5, 6], 6))
# print(new_dict.above_below([1, 2, 3, 4, 5, 6], -1))

# new_list = [1, 2, 3, 4, 5, 6]
# test = new_list[1: len(new_list) - 1]

# print(test)

print(new_dict.string_rotation("MyString", 0))
print(new_dict.string_rotation("MyString", 1))
print(new_dict.string_rotation("MyString", 2))
print(new_dict.string_rotation("MyString", 3))
print(new_dict.string_rotation("MyString", 4))
print(new_dict.string_rotation("MyString", 5))
print(new_dict.string_rotation("MyString", 6))
print(new_dict.string_rotation("MyString", 7))
