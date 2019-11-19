#!/usr/bin/env python3

#
# Open multiple files, sort the content and write to a new file
#

import contextlib
import heapq



# Function that use "contextlib" and "heapq" libraries
def fileSorter(filelist, outputfile):
    ''' '''
    with contextlib.ExitStack() as stack:
        files = [stack.enter_context(open(fn)) for fn in filelist]
        with open(outputfile, 'w') as f:
            f.writelines(heapq.merge(*files))


# To be completed
def fileSorterHardWay(filelist, outputfile):
    ''' '''
    with contextlib.ExitStack() as stack:
        files = [stack.enter_context(open(fn)) for fn in filelist]

        tmp_list = []
        tmp_line_list = []
        for f in files:
            print(f.name)
            line_list = f.readline().strip().split()
            index = line_list[0]
            print(line_list)
            print(index)
            tmp_list.append(index)
            tmp_line_list.append(line_list)

        print(tmp_list)
        # print the min value postion of the list
        print(tmp_list.index(min(tmp_list)))
        print(tmp_line_list[tmp_list.index(min(tmp_list))])




# Calling the fileSorter function
fileSorter(['a.txt', 'b.txt', 'c.txt'], 'output1.txt')

# Calling the fileSorterHardWay function
fileSorterHardWay(['a.txt', 'b.txt', 'c.txt'], 'output2.txt')



