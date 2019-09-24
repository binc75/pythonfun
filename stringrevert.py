#!/usr/bin/env python3

#
# Tricks and fun strings related functions
#

##
def revstring1(x):
    ''' Reverse a string. Not particularly memory efficient because strings are immutable so that output is always copied over '''
    output = ''
    for c in x:
        output = c + output
    return output

print(revstring1('ciao'))


##
def revstring2(x):
    '''Reverse a string in an optimized way using list'''
    output = []
    for c in x:
        output.insert(0, c)
    return ''.join(output)

print(revstring2('ciao'))


##
def revstring3(x):
    '''Reverse a string using slices'''
    return x[::-1]


print(revstring3('ciao'))
