def age_assignment(*args, **kwargs):
    result = {}

    for name in args:
        for letter, age in kwargs.items():
            if name[0] == letter:
                result[name] = age

    sorted_result = sorted(result.items(), key=lambda x: x[0])

    final_list = ""

    for name, age in sorted_result:
        final_list += f"{name} is {age} years old." + "\n"

    return final_list


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))