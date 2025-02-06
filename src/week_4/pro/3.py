import json
import copy


def analyze_salaries(filename):
    with open(filename, encoding='utf-8') as f:
        file_data = json.load(f)
        result = {}
        for data in file_data:
            if data['city'] not in result.keys():
                result[data['city']] = {}
        count_workers = copy.deepcopy(result)

        for data in file_data:
            if data['profession'] not in count_workers[data['city']]:
                count_workers[data['city']][data['profession']] = 1

            else:
                count_workers[data['city']][data['profession']] += 1

        for data in file_data:
            if data['profession'] not in result[data['city']]:
                result[data['city']][data['profession']] = data['salary'] / 1

            else:
                result[data['city']][data['profession']] = (result[data['city']][data['profession']] + data['salary'])

        for key, value in result.items():
            for key_p, value_s in value.items():
                count  = count_workers[key][key_p]
                result[key][key_p] = round(value_s / count,2)
        return result


print(analyze_salaries('example.jsonl'))
