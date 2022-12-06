from collections import defaultdict

with open("mini_input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line[:-1])
print(lines)

communication_channel = lines[0]

def find_marker(communication_channel):
    seen = set()
    counter = 0
    for index,char in enumerate(communication_channel):
        if char in seen:
            counter = 1
            seen = set()
            seen.add(char)
        else:
            counter += 1
            seen.add(char)
            if len(seen) == 4:
                print(index)
                print(seen)
                break
    return index+1,communication_channel[index-3:index+1]


def find_marker_2(communication_channel):
    left_pointer = 0
    right_pointer = 0

def lengthOfLongestSubstring(s: str) -> int:
    l, r = 0, 0
    max_len = 0

    letter_loc = {}

    while r < len(s):
        if max_len == 14:
            return r
        if s[r] not in letter_loc:
            max_len = max(max_len, r - l + 1)
            letter_loc[s[r]] = r
        else:
            while s[l] != s[r]:
                del letter_loc[s[l]]
                l += 1
            letter_loc[s[r]] = r
            l += 1
            max_len = max(max_len, r - l + 1)
        r += 1

    # return max_len

idx = lengthOfLongestSubstring(communication_channel)
print(idx)

# char_of_reveal, actual_marker = find_marker(communication_channel)
#
# print(f'Character of reveal is at index: {char_of_reveal}')
# print(f'Actual marker is: {actual_marker}')