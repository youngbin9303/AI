import numpy
import queue
from copy import deepcopy
import time
import sys
import generate_random_widgets
fp = open('part1_input.txt', 'r')
lines = fp.readlines()
dist_arr = []
for line in lines:
    # print(line)
    single_dist_arr = [int(dist) for dist in line.split('\t')]
    dist_arr.append(single_dist_arr)
widgets = ['AEDCA', 'BEACD', 'BABCE', 'DADBD', 'BECBD']
if len(sys.argv) > 1:
    widgets = generate_random_widgets.generateWidget(int(sys.argv[1]))
factories = ['A', 'B', 'C', 'D', 'E']
node_count = 0
frontier_list = queue.PriorityQueue()
history = []
history_len = []
frontier_list.put((0, widgets, ''))
while not frontier_list.empty():
    node_count += 1
    curr_node = frontier_list.get()
    curr_widgets_left = curr_node[1]
    curr_path = curr_node[2]
    #if(curr_node[0] == 11):
        #print(curr_path)
    if curr_widgets_left == []:
        print(curr_path)
        print('length = ', len(curr_path))
        print('node = ', node_count)
        break
    for factory in factories:
        new_path = deepcopy(curr_path)
        new_path += factory
        widgets_left = []
        new_cost = len(new_path)
        for widgets in curr_widgets_left:
            if widgets:
                if widgets[0] == factory:
                    widgets = widgets[1:]
                if widgets != '':
                    widgets_left.append(widgets)
        length_of_widgets = [len(w) for w in widgets_left]
        length_left = 0
        if length_of_widgets != []:
            length_left = max(length_of_widgets)
        if widgets_left not in history:
            history.append(widgets_left)
            history_len.append(new_cost)
            priority = new_cost + length_left
            frontier_list.put((priority, widgets_left, new_path))
        if widgets_left in history:
            if new_cost < history_len[history.index(widgets_left)]:
                history_len[history.index(widgets_left)] = new_cost
                priority = new_cost + length_left
                frontier_list.put((priority, widgets_left, new_path))