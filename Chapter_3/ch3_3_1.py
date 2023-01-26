'''Describe how you could use a single array to implement three stacks'''

'''
I believe that in order to use an array to implement three stacks
all you have to do would be to put the head node of each stack in
one index of the array

visualized, it would look something like this:

	H = Head_node
	N = prev_node.next_node
	[0: H1, 1: H2, 2: H3]
		|      |       |
		N      N       N
		|      |       |
		N      N       N
		|      |       |
		N      N       N

so in practice you could just initilize an array with three head nodes
(or make an array and push those head nodes into it)

	my_arr = [Stack(), Stack(), Stack()]

then to add data you would simply call the push() method on
the index whos stack you want to push to

	my_arr[0].push(2)
	my_arr[1].push(4)
	my_arr[2].push(6)

peek, pop, and is_empty would also work the same
'''
