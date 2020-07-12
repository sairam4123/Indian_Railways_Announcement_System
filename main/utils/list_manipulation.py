from typing import List


def check_a_list_in_another_string(list_of_str: List[str], main_string: str) -> bool:
    for string in list_of_str:
        if string in main_string:
            return True
    return False


def check_a_list_eq_eq_another_string(list_of_str: List[str], main_string: str) -> bool:
    for string in list_of_str:
        if string == main_string:
            return True
    return False
