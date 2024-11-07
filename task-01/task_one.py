import os
import re
from typing import List


def part_one(file_name: str, correct_nums: List) -> int:
    # Open the inputs file and format the input into a list
    with open(os.path.join('inputs', file_name)) as inp:
        contents = inp.read().split('\n')

    # For loop to get position of each line and numbers extracted using regular expression
    for index, line in enumerate(contents):
        str_matches = [(match.group(), match.span()) for match in re.finditer(r'\d+', line)]

        # Evaluation whether a number should be added or not
        for num, (span_start, span_end) in str_matches:
            adjacent_chars = ''
            left_position = span_start - 1 if span_start != 0 else span_start
            right_position = span_end + 1 if span_start != len(contents[index]) else span_end

            if span_start != 0:
                adjacent_chars += contents[index][span_start - 1]
            if span_end != len(contents[index]):
                adjacent_chars += contents[index][span_end]
            if index != 0:
                adjacent_chars += contents[index - 1][left_position:right_position]
            if index != len(contents) - 1:
                adjacent_chars += contents[index + 1][left_position:right_position]
            if bool(re.search('[^0-9.]', adjacent_chars)):
                correct_nums.append(int(num))

    return sum(correct_nums)


if __name__ == '__main__':
    print(part_one('example_input.txt', []))
    print(part_one('actual_imput.txt', []))
