"""
References:
    COP3530 Exam 1 review video,
    COP3530 Module 7 lectures,
    https://www.geeksforgeeks.org/python/python-lists/,
    https://docs.python.org/3/howto/sorting.html
"""

class MaxHeap:
    def __init__(self, k):
        self.max_size = k # max number of nodes
        self.heap_list = [] # list containing nodes

    def insert_first_k(self, galaxy_list):
        # If k is greater than number of galaxies stored, reset max size of heap to galaxy list size
        if self.max_size > len(galaxy_list):
            self.max_size = len(galaxy_list)
        # Add k elements to heap_list
        for i in range(0, self.max_size):
            self.heap_list.append(galaxy_list[i])
            self.heapify_up(i)

    def insert_node(self, new_galaxy):
        # If room in heap, insert node
        if len(self.heap_list) < self.max_size:
            self.heap_list.append(new_galaxy)
            # Heapify up
            index = len(self.heap_list)-1
            self.heapify_up(index)
        # If heap is full, compare node distance to root distance. If smaller than root, replace root with new galaxy and heapify down.
        else:
            if new_galaxy.distance < self.heap_list[0].distance:
                self.heap_list[0] = new_galaxy
                self.heapify_down(0)

    def heapify_up(self, index):
        # Return if node is root
        if index == 0:
            return
        # Find parent index
        parent = (index - 1) // 2
        # If child is larger than parent, swap
        if self.heap_list[index].distance > self.heap_list[parent].distance:
            self.heap_list[index], self.heap_list[parent] = self.heap_list[parent], self.heap_list[index]
            # Recurse up
            self.heapify_up(parent)

    def heapify_down(self, index):
        # Find indices for children
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2

        # If node has children, compare its distance to its children and find the largest. Return if node is leaf or node is greater than children.
        largest_index = index
        if left_child_index < len(self.heap_list) and self.heap_list[left_child_index].distance > self.heap_list[largest_index].distance:
            largest_index = left_child_index
        if right_child_index < len(self.heap_list) and self.heap_list[right_child_index].distance > self.heap_list[largest_index].distance:
            largest_index = right_child_index
        if largest_index == index:
            return

        # Swap node with largest child
        self.heap_list[index], self.heap_list[largest_index] = self.heap_list[largest_index], self.heap_list[index]

        # Recurse down
        self.heapify_down(largest_index)

    def return_all_nodes(self):
        result = sorted(self.heap_list, key=lambda galaxy: galaxy.distance)
        return result
