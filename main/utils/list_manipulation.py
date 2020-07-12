from typing import List


def check_a_list_in_another_list(list_of_str: List[str], main_string: str) -> bool:
    for string in list_of_str:
        return string in main_string
    return False
