'''
def BFS(root):
	my_queue = Queue()
    root.marked = True
    my_queue.enqueue(root)

    while not my_queue.is_empty():
		next_node = queue.dequeue()
        visit(next_node)
        for node in next_node.adjacent:
			if node.marked is False:
				node.marked = True
                my_queue.enqueue(node)

The BFS is similar to the DFS in that you keep track of what nodes have been visited and then
visit the adjacent neigbors of each node.

The main difference is that for a BFS you use ad the neighbors to a queue before
you actually visit them. The queue makes it so that you always will visit the nodes
that are closest to the root before the leaf nodes.

so, to do a BFS, first you have to create a queue. I have seen people used lists for these
but I find it easier to use an actual queue class. You then mark the starting node somehow.
You can use a visited set or a list. But you can also just have a marked property on the
node itself. for the purpose of this implementation we will be doing this.

After you create the queue and mark the starting node you simply add the first node to the queue.

Then as long as the queue still has nodes in it,
you grab the front node of the queue and 'visit' it.

Visiting the node can mean any number of things just like in a DFS, you can simply print out
the value, or make some sort of tranformation to the data itself. Either way, after you
visit the node, you look through all the nodes adjacent to this node that was just visited,
and then add them to the queue if they have not already been visited
as well as mark them as visited.

And that's it, the process will repeat until the queue is empty meaning all nodes have been visited
or we have reached a desired target.
'''
