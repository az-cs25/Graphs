
# children are nodes
# neighbors/edges are parents - child relationships
# directed graph (relationship only flows one way either child to parent or parenn to child)
# i.e 1 is 3's parent but 3 is not 1's parent
# need to find the longest route - so DFS


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):

    # create a Queue
    qq = Queue()

    # this is where we will store the max_len and earliest_ancestor:
    earliest_ancestors = []
    # get a list of all children
    children = [a[1] for a in ancestors]

    # initiate max length
    max_len = 0

    # Enqueue a list to use as our path
    qq.enqueue([starting_node])

    # make a set to keep track of where we've been
    visited = set()

    # while there is stuff in the queue
    while qq.size() > 0:

        # pop the first item
        path = qq.dequeue()
        vertex = path[-1]
        # If not visited
        if vertex not in visited:
            # DO THE THING i.e do the check if we've hit the desired vertex

            # if the vertex was never a child, it's the oldest in the lineage
            if vertex not in children:

                # if a path with that length already exists and this vertex(ancestor) is smaller
                if len(path) == max_len and vertex < earliest_ancestors[1]:

                    # replace it
                    earliest_ancestors = [max_len, vertex]

                # if len(path) is bigger than the current max length,
                if len(path) > max_len:

                    # we have a new earliest ancestor & max_len
                    max_len = len(path)

                    # and we replace earliest ancestor with this path
                    earliest_ancestors = [max_len, vertex]

            # visit the child
            visited.add(vertex)
            # queue up the next node
            for node in ancestors:
                print(node[1])
                if vertex == node[1]:
                    # copy path to avoid pass by reference bug
                    new_path = list(path)
                    # add the next parent to the path
                    new_path.append(node[0])
                    # enqueue a new path
                    qq.enqueue(new_path)

    # if max_length=1 return -1 (there's no ancestors)
    if max_len == 1:
        return -1

    return earliest_ancestors[1]
