import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = [".com", ".bg", ".org", ".net"]
name_pattern = r"[\w+\.]+"
domain_pattern = r"\.[a-z]+"

command = input()

while command != "End":
    number_of_at_symbol = command.count("@")

    if number_of_at_symbol < 1:
        raise MustContainAtSymbolError("Email must contain @")

    elif number_of_at_symbol == 1:
        current_command = command.split("@")

        if len(re.findall(name_pattern, current_command[0])[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        elif re.findall(domain_pattern, current_command[1])[0] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

        print("Email is valid")

    command = input()
