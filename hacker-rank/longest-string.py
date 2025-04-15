import sys
import string

#
# Complete the 'getLargestString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
# 1. STRING s
# 2. INTEGER k
#

from collections import namedtuple

Fetched = namedtuple('Fetched',
                     ['index',
                      'Bucket'])

spacers=[]

class Bucket:
    table = {}
    max_length = 0

    def __lt__(self,other):
        if self.count < other.count:

            if ord(self.char) < ord(self.char):
                return True

            return False

        return False

    def __init__(char, max):
        self.char = char
        self.count = 1

        if table[char] is not None:
            table[char].append(self)

    def __call__(self, char):
        if self.count < Bucket.max_length:
            self.count += 1

            return None

        # will self-insert into table
        Bucket(char)
        return None

def fill_buckets(char):
    if Bucket.table[char] is None:
        Bucket(char)
    else:
        Bucket.table[char][-1](char)

    return None

def build_buckets(data):
    for char in data:
        fill_buckets(char)

def sort_buckets():
    bucket_list = []

    for table in Bucket.table:
        bucket_list = bucket_list + table

    bucket_list.sort()

    return bucket_list

def build_spacers():
    # spacers are single characters we can use to break up things

    for bucket_list in Bucket.table:
        if len(bucket_list) == 1:
            char = bucket_list[0].char

            spacers.append(char)
            Bucket.table.remove(char)

def getLargestString(s, k):
    largest = ""

    build_buckets(s)
    build_spacers()

    for bucket in sort_buckets():
        if len(largest) < 1:
            largest = largest + bucket.count * bucket.char
            continue

        if largest[-1] == bucket.char:
            if len(spacer) > 0:
                largest = largest + spacer.pop()
                continue
            else:
                # no spacer, have to skip
                continue
        else:
            # a different character
            largest = largest + bucket.count * bucket.char
