from gendiff.modules.parser import parser_json

def generate_diff(filepath1, filepath2):
    result_diff="{ \n"
    dict1 = parser_json(filepath1)
    dict2 = parser_json(filepath2)
    for key in sorted(set(dict1.keys()) | set(dict2.keys())):
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result_diff += f"  {key}: {dict1[key]}\n"
            else:
                result_diff += f"- {key}: {dict1[key]}\n"
                result_diff += f"+ {key}: {dict2[key]}\n"
        elif key in dict1:
            result_diff += f"- {key}: {dict1[key]}\n"
        elif key in dict2:
            result_diff += f"+ {key}: {dict2[key]}\n"
    result_diff += "} \n"
    return result_diff

diff = generate_diff(filepath1, filepath2)
print(diff)






