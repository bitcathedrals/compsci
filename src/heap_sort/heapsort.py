# This is a exploration of the heapsort algorithm.
# I started with a description in Essential Algorithms by Rod Stephens. Then
# I examined source code examples on the Internet, I checked Wikipedia, and
# finally MIT Introduction to Algorithms 3rd ed. The design was the same for
# Wikipedia and MIT Introduction to Algorithms.
#
# When I implemented the algorithm initially from Essential Algorithms I found
# errors in the heap construction that seemed to interfere with sorting in some
# cases. It is detailed under heapify_bottom_up()

# I corrected the flaw in the algorithm and here I present my modified version.

# I have also implemented the Wikipedia/MIT algorithm.

# Here I test them with a fixed sample that reproduces the error in Essential Algorithms.
# I try it with all the algorithms.

# Then I generate a number sequence that is shuffled and test performance on 10,000 elements.

# There are many debugging and verification tools available in execute_test_run()

# My conclusion is that the Wikipedia/MIT algorithm is simpler and a little faster it seems.
# My version was not much slower though which is interesting.

# The program only requires Python 3 and Graphviz. It generates .dot files which are the input file for the graphviz
# dot program. It also generates .png files which are a rendering of the heap just before sorting.

# additional information at: https://en.wikipedia.org/wiki/Heapsort

import copy
import random
import timeit
import os


class HeapSort:
    def __init__(self, data=None, fix=True):
        if data is None:
            raise ValueError("HeapSort objects must be initialized with data.")

        self.tree = copy.deepcopy(data)
        self.size = len(self.tree)

        self.fix = fix

    # mapping a binary tree onto an array. For a general mapping it's
    # slightly different, this mapping places the root node at the beginning of
    # the array and the formulas for calculating the children and parent were
    # adjusted. This is standard for a heap kind of tree.

    def parent(self, i: int):
        if i <= 0:
            raise ValueError(f"in the parent function i = {i} must not be <= 0")

        if i >= self.size:
            raise ValueError(f"in the parent function i = {i} must not be >= size = {self.size}")

        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        if i >= self.size:
            raise ValueError(f"in the left_child function i = {i} must not be >= size = {self.size}")

        return 2 * i + 1

    def right_child(self, i: int) -> int:
        if i >= self.size:
            raise ValueError(f"in the right_child function i = {i} must not be >= size = {self.size}")

        return 2 * i + 2

    def heapify_bottom_up(self):
        # heapify from the end of the array which is the lowest rightmost value on the tree. This is a breadth
        # first traverse in reverse.

        # the current node is compared with the parent and they are swapped if the child is greater than
        # the parent. Since every node is touched in the traverse it will build a heap.

        # this is the textbook version. I implemented it pretty carefully. However with some inputs I found
        # errors. Specifically the scenario where the root element contains the smallest value.

        # In the scenario where the lowest value is in the root node, the lowest value will be "demoted"
        # or swapped down one level. This breaks the heap property at the lower level. Since it has reached
        # the root the heapify algorithm leaves that poison value on the second level of the tree as it halts.

        # I also discovered another corner case where the right child contains a value that is a heap property,
        # and the left child contains a high value, even the highest. It will swap up and the demoted value will end
        # up at the parent of the tree. The heap property is broken, but the algorithm always moving to the left will
        # never check that invariant again as it proceeds up the tree.

        # In other words poison values can get "stuck" in spots where the heap invariant will never be checked again
        # because the algorithm never looks backwards to clean up it's mess as it climbs the tree.

        for data_index in range(self.size - 1, 0, -1):
            # heapify the current node
            traverse_index = data_index

            # when a traverse is the root we are done.
            while traverse_index != 0:
                parent_index = self.parent(traverse_index)

                # if we encounter a heap that is valid we are done too
                if self.tree[traverse_index] <= self.tree[parent_index]:
                    break

                # we don't have a heap property so swap to restore the heap property.
                # do this by swapping
                self.tree[parent_index], self.tree[traverse_index] = self.tree[traverse_index], self.tree[parent_index]

                # This is where I fix the algorithm. Fix the invariant working down the tree on the demoted node.
                if self.fix:
                    self.heapify_top_down(traverse_index, self.size)

                # continue moving up the tree.
                traverse_index = parent_index

    def heapify_wikipedia(self):
        # the Wikipedia heapify is a bottom up application of the top down heapify pushing low values as low as
        # they will go and bubbling up one level the higher values.

        for index in range(self.size - 1, -1, -1):
            self.heapify_top_down(index, self.size - 1)


    def heapify_top_down(self, parent_index: int, size: int):
        # compute the children
        left_index = self.left_child(parent_index)
        right_index = self.right_child(parent_index)

        # if we fall off the end of the tree set the child to the parent index
        if left_index >= size:
            left_index = parent_index

        if right_index >= size:
            right_index = parent_index

        # if we have a heap property terminate
        if self.tree[left_index] <= self.tree[parent_index] and self.tree[right_index] <= self.tree[parent_index]:
            return

        # next need to consider both nodes, by swapping the larger of the two children. If the child that you swap
        # with is greater than the other child then the heap property will be maintained for both children
        # after swapping one child.
        greater_child_index = left_index

        if self.tree[right_index] > self.tree[left_index]:
            greater_child_index = right_index

        self.tree[parent_index], self.tree[greater_child_index] = self.tree[greater_child_index], self.tree[parent_index]

        self.heapify_top_down(greater_child_index, size)

    def sort(self):
        # the sort algorithm is simple. Swap the root for the end, and move the end marker down. then heapify_top_down
        # again. this algorithm seems to tolerate broken heaps since it pushes values downward in the heapify_top_down
        # call.
        for index in range(self.size - 1, 0, -1):
            self.tree[0], self.tree[index] = self.tree[index], self.tree[0]

            self.heapify_top_down(0, index)

    def verify_heap(self):
        bad_nodes = []

        for index in range(self.size - 1):
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if left_index >= self.size:
                left_index = index

            if right_index >= self.size:
                right_index = index

            if self.tree[index] >= self.tree[left_index] and self.tree[index] >= self.tree[right_index]:
                continue

            bad_nodes.append(index)

        return bad_nodes

    def node_name(self, index: int) -> str:
        return "node" + str(index)

    def __str__(self):
        declaration = "digraph heap {\n"

        index = 0
        while index < self.size:
            name = self.node_name(index)
            value = self.tree[index]

            declaration += f'  {name} [ label="{value}" ]\n'

            if index > 0:
                ancestor_index = self.parent(index)
                declaration += f'  {self.node_name(ancestor_index)} -> {self.node_name(index)}\n'

            index += 1

        declaration += "}"

        return declaration

    def heap(self):
        return self.tree

    def full_sort(self, name, wikipedia=True, verify_heap=True, graph=False):
        if wikipedia:
            self.heapify_wikipedia()
        else:
            self.heapify_bottom_up()

        if verify_heap:
            invalid_heaps = self.verify_heap()

            if invalid_heaps:
                output = f"{name} -> invalid heaps found: " + ",".join([str(x) for x in invalid_heaps])
                print(output)
            else:
                print(f"{name} -> perfect heap!")

        if graph:
            write_graph(name, str(self))

        self.sort()


def write_graph(filename: str, graph: str):
    file_handle = open(filename + ".dot", "w")

    file_handle.write(graph)

    file_handle.close()

    try:
        os.system(f"dot -Tpng {filename}.dot >{filename}.png")
    except KeyboardInterrupt:
        raise
    except:
        print("could not generate graph: " + filename + ".dot")


def verify_is_sorted(sorted_data):
    bad_sorts = []

    for i in range(len(sorted_data) - 1):
        if sorted_data[i] > sorted_data[i+1]:
            bad_sorts.append((i, sorted_data[i], i+1, sorted_data[i+1]))

    return bad_sorts


def print_bad_sort(invalid):
    print(f"bad sort at: [{invalid[0]}] = {invalid[1]}, [{invalid[2]}] = {invalid[3]}")


def execute_test_run(name, data=None, count=0,
                     fix=True,
                     wikipedia=False,
                     graph=False,
                     truncate=True,
                     print_results=False,
                     verify=True):
    test_data = data
    if not test_data:
        if count <= 0:
            print("test: " + name + " has a invalid data specification")

        test_data = list(range(count))
        random.shuffle(test_data)

    print("-" * 80)

    if wikipedia:
        implementation="Wikipedia"
    else:
        if fix:
            implementation="Essential Algorithms (My modification)"
        else:
            implementation="Essential Algorithms (textbook)"

    count = str(len(test_data))

    print(f"{name} running {implementation} heapify for ({count}) items.")

    test_heap = HeapSort(data=test_data, fix=fix)

    test_fn = lambda: test_heap.full_sort(name, wikipedia=wikipedia, verify_heap=verify, graph=graph)

    time = timeit.timeit(test_fn, number=1)

    print(f"{name} -> execution time: " + str(time))

    bad_sorts = verify_is_sorted(test_heap.heap())

    if bad_sorts:
        print(f"{name} -> Bad Sorts!")
        if truncate:
            print(f"{len(bad_sorts)} bad sorts!")
        else:
            [print_bad_sort(x) for x in bad_sorts]
    else:
        print(f"{name} -> GOOD SORT!")

    if print_results:
        print(repr(test_heap.heap()))


if __name__ == "__main__":

    # this list of values produces the broken heap with the standard algorithm.
    broken_sample = [1, 5, 6, 3, 9, 10, 2]

#    execute_test_run("broken_sample", data=broken_sample, print_results=True, wikipedia=False, fix=False)

#    execute_test_run("corrected_sample", data=broken_sample, print_results=True, wikipedia=False, fix=True)

#    execute_test_run("Wikipedia_sample", data=broken_sample, print_results=True, wikipedia=True, truncate=False)

#    execute_test_run("medium_broken", count=10000, wikipedia=False, fix=False)

#    execute_test_run("medium_corrected", count=10000, wikipedia=False, fix=True)

    execute_test_run("medium_wikipedia", count=1000000, wikipedia=True)
