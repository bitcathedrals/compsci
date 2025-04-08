#!/bin/python

# Complete the function below.

from collections import namedtuple

SubSeq = namedtuple('SubSeq',
                    ['last',
                    'count'])

def  findLIS(s):

    # we are going to keep a two dimensional array to track all the possible
    # sub-sequences as we go

    sequences = []

    def update_sub(sub, value):
        return SubSeq(
                        last=value,
                        count=sub.count + 1
                    )

    def find_sequences(value):
        this_end = len(sequences)

        sequences.append(SubSeq(last=value, count=1))

        # traverse is walking across the sequences
        traverse = 0

        while traverse < this_end:
            this_value = sequences[traverse].last

#            print(f'this_value is {this_value}, value is {value}')
            # skip equals
            if value == this_value:
                pass

            elif value > this_value:
#               print(f'updating traverse {traverse}, this_value {this_value}, value {value}')

                sequences[traverse] = update_sub(sequences[traverse], value)

            traverse = traverse + 1

    def find_longest_sequence(data):
        [find_sequences(x) for x in data]
        traverse = 0

        longest = 0

        sequence_size = len(sequences)
#        print(f'sequence size is: {sequence_size} sequences = {sequences}')

        while traverse < sequence_size:
            if sequences[traverse].count > longest:
                longest = sequences[traverse].count

            traverse = traverse + 1

        return longest

#    print(f's = {s}')

    return find_longest_sequence(s)

_s_cnt = int(input())
_s_i=0
_s = []
while _s_i < _s_cnt:
    _s_item = int(input());
    _s.append(_s_item)
    _s_i+=1


res = findLIS(_s);
print(res)
