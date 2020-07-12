from typing import Any, Callable, List, Union


def convert_list_of_any_to_specific_thing(list_of_any: List[Any], converter: Callable[[Union[int, str]], Any]) -> List[Any]:
    converted_objects = []
    for _object in list_of_any:
        result = converter(_object)
        converted_objects.append(result)
    return converted_objects
