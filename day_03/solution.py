import re
from typing import List


DATA_FILE_NAME = "data.txt"
MULT_REGEX_PATTERN = r"mul\(\d{1,3},\d{1,3}\)"


def get_text(file_name: str) -> str:
    text = ""
    with open(file_name, "r") as file:
        for line in file:
            text += line
    return text


def get_total(found_mults: List[str]):
    total = 0
    for mult in found_mults:
        nums = re.findall(r"\d+", mult)
        total += int(nums[0]) * int(nums[1])
    return total


def main():
    text = get_text(DATA_FILE_NAME)
    found_mults = re.findall(MULT_REGEX_PATTERN, text)
    total = get_total(found_mults)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
