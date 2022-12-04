
def main(mini_input,first_star):
    if mini_input:
        text_file = "mini_input.txt"
    else:
        text_file = "input.txt"
    with open(text_file) as file_in:
        lines = []
        for line in file_in:
            lines.append(line[:-1])

    def parse_input(pair_str):
        pair = pair_str.split(',')
        pair = (pair[0].split('-'), pair[1].split('-'))
        first_elf = [int(num) for num in pair[0]]
        second_elf = [int(num) for num in pair[1]]

        return (tuple(first_elf), tuple(second_elf))

    lines = [parse_input(pair) for pair in lines]
    print(lines)

    if first_star:
        def fully_contains(elf_1, elf_2):
            if elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]:
                return 1
            elif elf_2[0] >= elf_1[0] and elf_2[1] <= elf_1[1]:
                return 1
            return 0

        num_useless_schedules = sum([fully_contains(pair[0], pair[1]) for pair in lines])
        print(num_useless_schedules)

    else:
        def intersects(elf_1,elf_2):
            if elf_1[0] <= elf_2[0] <= elf_1[1] or elf_1[0] <= elf_2[1] <= elf_1[1]:
                return 1
            elif elf_2[0] <= elf_1[0] <= elf_2[1] or elf_2[0] <= elf_1[1] <= elf_2[1]:
                return 1
            return 0

        num_useless_schedules = sum([intersects(pair[0], pair[1]) for pair in lines])
        print(num_useless_schedules)


if __name__ == '__main__':
    # This code won't run if this file is imported.
    main(False,False)