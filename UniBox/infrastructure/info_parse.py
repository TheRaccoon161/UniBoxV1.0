from UniBox.Classes.data_dto import DataDto


def parse_data_info(params) -> DataDto:
    return DataDto(
        name=remove_unnecessary_whitespaces(params['name']),
        phone_number=remove_unnecessary_whitespaces(params['phone_number']),
        email=remove_unnecessary_whitespaces(params['email'])
    )


def remove_unnecessary_whitespaces(string: str) -> str:
    result = string
    for char in string:
        if char.isspace():
            result = result.replace(char, '', 1)
        else:
            return result
