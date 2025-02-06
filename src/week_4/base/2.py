from collections import Counter


def get_popular_name_from_file(filename: str):
    with open(filename, encoding='utf-8') as f:
        lines = [line.strip().split(' ')[0] for line in f.readlines()]
        dict_names_with_count = dict(Counter(lines))

        sorted_dict = sorted(dict_names_with_count.items(), key=lambda x: x[1], reverse=True)

        most_freq = sorted_dict[0][1]
        res_str = ''
        for key, value in sorted_dict:
            if value == most_freq:
                res_str += key + ', '
        return res_str[:-2]


print(get_popular_name_from_file('example.txt'))
