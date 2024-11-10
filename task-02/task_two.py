import os
import re


def initial_location(contents, part, current_map, map_dicts, sources, destinations, results):
    # Get all map types and seed numbers
    map_names = [s for s in contents if bool(re.match('[^0-9]+$', s))]
    if part == 1:
        seeds = [int(s) for s in re.findall(r'\d+', contents[0])]
    else:
        seeds = []
        seed_ranges = [int(s) for s in re.findall(r'\d+', contents[0])]
        for pair_index in range(int(len(seed_ranges) / 2)):
            start_seed = seed_ranges[pair_index * 2]
            end_seed = start_seed + seed_ranges[pair_index * 2 + 1]
            seeds += list(range(start_seed, end_seed))

    # Keys for to be created dicts
    keys = ['name', 'source_ranges', 'destination_ranges']

    # Create dicts containing info about each map
    for index, entry in enumerate(contents[2:]):
        if entry in map_names:
            current_map = entry
            continue
        elif entry is not current_map:
            destination, source, length = [int(s) for s in re.findall(r'\d+',entry)]
            sources.append(range(source, source + length))
            destinations.append(range(destination, destination + length))

        if index + 2 > len(contents[2:]) or contents[index + 3] in map_names:
            values = [current_map, sources, destinations]
            map_dicts.append(dict(zip(keys, values)))
            sources, destinations = [], []

    # Search for the end location by going through all maps
    for src in seeds:
        src_list = [src]
        for map_d in map_dicts:
            for list_index, source in enumerate(map_d['source_ranges']):
                if source.start <= src <= source.stop - 1:
                    dest_index = list(source).index(src)
                    src = map_d['destination_ranges'][list_index][dest_index]
                    break
            src_list.append(src)
        results.append(src_list)

    return min([loc[-1] for loc in results])


if __name__ == '__main__':
    # file_name = 'example_input.txt'
    file_name = 'actual_input.txt'

    # Open the inputs file and format the input into a list
    with open(os.path.join('inputs', file_name)) as inp:
        text_input = [line.strip() for line in inp if line.strip()]

    # print(initial_location(text_input, 1, '', [], [], [], []))
    print(initial_location(text_input, 2, '', [], [], [], []))
