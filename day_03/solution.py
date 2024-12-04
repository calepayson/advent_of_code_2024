import re
from typing import List, Optional


DATA_FILE_NAME = "data.txt"
MULT_REGEX_PATTERN = r"mul\(\d{1,3},\d{1,3}\)"
DO_SECTION_REGEX_PATTERN = r"(?:^[\s\S]*?don't\(\))|(?:do\(\)[\s\S]*?(?:don't\(\)|$))"


def get_text(file_name: str) -> str:
    """
    Reads the text from the data file into a string.

    Args:
        file_name (str): The name of the data file.

    Returns:
        (str): The text in the file.
    """
    text: str = ""
    with open(file_name, "r") as file:
        for line in file:
            text += line
    return text


def find_do_mults(text: str) -> List[Optional[str]]:
    """
    Returns all parts of the text preceeded by a do() instruction.

    Uses a beefy regex to grab all text up to the first don't(), any text
    between do and don't instructions, and the last bit of text.

    Args:
        text (str): The text to search.

    Returns:
        (List[Optional[str]]): A list of all mult()'s within valid do()
            instructions.
    """
    result: List[Optional[str]] = []
    do_sections = re.findall(DO_SECTION_REGEX_PATTERN, text)
    for section in do_sections:
        found_mults = re.findall(MULT_REGEX_PATTERN, section)
        result += found_mults
    return result


def get_total(found_mults: List[Optional[str]]) -> int:
    """
    Calculate the sum of all mult() statements.

    Args:
        found_mults (List[Optional[str]]): A list of valid mult()'s.

    Returns:
        (int): The sum of all valid mult() statements.
    """
    total: int = 0
    for mult in found_mults:
        nums: List[str] = re.findall(r"\d+", mult)
        if len(nums) == 2:
            total += int(nums[0]) * int(nums[1])
    return total


def main():
    """
    The main function.

    Reads the data from a file into the string. Gathers all valid mult()s in a
    list. Calculates the sum of all valid mult()s. Prints the sum.
    """
    text = get_text(DATA_FILE_NAME)
    found_mults = find_do_mults(text)
    total = get_total(found_mults)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
