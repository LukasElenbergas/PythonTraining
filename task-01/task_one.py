import os
import re
from typing import List


def part_one(contents: List[str], num_sum: int) -> int:
    # For loop to get position of each line and numbers extracted using regular expression
    for index, line in enumerate(contents):
        num_info = [(match.group(), match.span()) for match in re.finditer(r'\d+', line)]

        # Evaluation whether a number should be added or not
        # This is done by checking the combined characters around a number for special chars
        for num, (span_start, span_end) in num_info:
            adjacent_chars = ''
            left_position = span_start - 1 if span_start != 0 else span_start
            right_position = span_end + 1 if span_start != len(contents[index]) else span_end

            if span_start != 0:
                adjacent_chars += line[span_start - 1]
            if span_end != len(contents[index]):
                adjacent_chars += line[span_end]
            if index != 0:
                adjacent_chars += contents[index - 1][left_position:right_position]
            if index != len(contents) - 1:
                adjacent_chars += contents[index + 1][left_position:right_position]
            if bool(re.search('[^0-9.]', adjacent_chars)):
                num_sum += int(num)

    return num_sum

def part_two(contents: List[str], adjacent_nums: List) -> int:
    # Get all numbers from the start
    num_info = [[(match.group(), match.span()) for match in re.finditer(r'\d+', line)] for line in contents]

    # For loop to get position of each gear and adjacent numbers to it by checking overlapping spans (ranges)
    for index, line in enumerate(contents):
        gear_matches = [match.span() for match in re.finditer(r'\*', line)]

        # Evaluation whether a gear has adjacent numbers
        # This is done by evaluating if a number's span overlaps with the gear's span
        for gear_span_start, gear_span_end in gear_matches:
            nums_to_mul = []
            for i in [index - 1, index, index + 1]:
                for num, (num_span_start, num_span_end) in num_info[i]:
                    if index != 0 or index != len(line):
                        if max(gear_span_start - 1, num_span_start - 1) < min(gear_span_end, num_span_end):
                            nums_to_mul.append(int(num))
            adjacent_nums.append(nums_to_mul)

    return sum([pair[0] * pair[1] for pair in adjacent_nums if len(pair) == 2])


if __name__ == '__main__':
    # file_name = "example_input.txt"
    file_name = "actual_input.txt"

    # Open the inputs file and format the input into a list
    with open(os.path.join('inputs', file_name)) as inp:
        text_input = inp.read().split('\n')

    print(part_one(text_input, 0))
    print(part_two(text_input, []))
