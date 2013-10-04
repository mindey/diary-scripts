# -*- coding: utf-8 -*-
# Given lines of diary written in a file generated by generate-days.py
# extract the content of each day, and write it into a vector
# (Python list) of tuples, where each tuple consists of two
# strings: one for the date, one for the contet of each day.

def daysof(diary):
    """
    Given diary lines, return a vector of contents of the days.
    daycontent(A)[0] -- content of the 1st day of life.
    Each day in diary, begins with "ID ■  ", and has "] " before the text.
    """
    content = []
    dates = []
    for line in diary:
        line = line[:-1]
        if ('%s ■  ' % (len(content)+1) in line) and (']' in line):
            dates.append(line.split(']')[0]+']')
            content.append(line.split(']')[1])
        else:
            content[-1] += '\n'+line
    return dates, content

# Usage example:
diary_lines = open('sample_diary.txt', 'rb').readlines()
days, contents = daysof(diary_lines)

for i, content in enumerate(contents):
    print days[i], 'CONTENT:' + content

