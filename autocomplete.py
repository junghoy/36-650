#!/usr/bin/env python
import os 
import sys
from Queue import PriorityQueue

#Defining the class Trie
"""
Trie class has five characteristics: 
1) children: It contains a dictionary of its children
2) flag: It tells you whether the trie is a node with word or not 
3) freq: It tells you the frequency of its own node 
4) maxweight: It represents the maximum weight of its children
5) name: refers to its name
"""
class Trie(object):


    def __init__(self):

        self.children = {}
        self.flag = False 
        self.freq = 0
        self.maxweight = 0
        self.name = None

#'Add' method is a helper method to supplement insert function

    def add(self, char):

        self.children[char] = Trie()

#'Contains' method returns True if the dictionary contains that word
# and returns False otherwise

    def contains(self, word):

        node = self
        for char in word: 
            if node is not None:
                node = node.children.get(char)

        if node is not None and node.flag:
            return node
        else:
            return False

# After initializing the root Trie, we could use 'insert' function to 
# create a map of Trie nodes  

    def insert(self, word, freq):

        node = self

        # Use recursive method to create Trie nodes for each character in word
        # If a particular node was born before, we update the maxweight and weight of that node

        for char in word:
            if char not in node.children.keys():
                node.add(char)
                node.children[char].maxweight = freq
            
            elif char in node.children.keys():
                if node.children[char].maxweight < freq: 
                    node.children[char].maxweight = freq
                else:
                    pass

            node = node.children[char]

        node.flag = True
        node.name = word
        node.freq = freq


    # Function find_subtrie returns a dictionary of children for a particular prefix 
    # This is a helper function for find_top_k

    def find_subtrie(self, prefix):

        node = self
        prefix = prefix.lower()

        #If prefix is empty, we return the root's children

        if len(prefix)==0:
            return node.children

        #Else, we iterate through each character in prefix and returns the final node's children
        #If there is no child, return None

        else:
            for char in prefix:
                child = node.children.get(char)
                if child is not None:
                    node = node.children[char]
                else:
                    return None

        return node.children

    """"
     Function find_top_k finds the top k elements that are associated with the prefix in a list 
     We use recursion to insert elements in priority queue to store which nodes should be prioritized 
     PriorityQueue class has been imported
    """

    def find_top_k(self, k, prefix):
        
        node = self
        prefix = prefix.lower()
        priority_q = PriorityQueue()
        top_k = []

        subtrie = node.find_subtrie(prefix)

        """
         Insert information in priority queue defined as priority_q 
         priority_q contains three information: 
         1) maxweight or frequency of the node
         2) indicator that tests whether the node is a word or not
         3) the node itself 

         Note that if the node is a word and has one or more child, we input both its frequency and maxweight to the priority_q
        """

        if bool(subtrie):
            for child in subtrie.values():
                priority_q.put((-child.maxweight, 0, child))
                
                if child.flag and bool(child.children):  
                    priority_q.put((-child.freq, 1, child))


        # Use while loop until we have appended k elements in top_k or we are out of the priority queue

            while(priority_q.qsize() > 0 and len(top_k) < k):

                pop = priority_q.get()
                pop_value = pop[0]
                pop_end = pop[1]
                pop_node = pop[2]

            # Append the frequency and name of the node to top_k 
            # if the node is a word and (its freq and maxweight are the same or its indicator function indicates that its priority is associated with its freq, not maxweight

                if pop_node.flag and (pop_node.freq == pop_node.maxweight or pop_end == 1) and pop_node.name not in [x[1] for x in top_k]:
                    top_k.append((pop_node.freq, pop_node.name))

                if bool(pop_node.children) and pop_end == 0:
                    for child in pop_node.children.values():
                        priority_q.put((-child.maxweight, 0, child))

                        if child.flag and bool(child.children):
                            priority_q.put((-child.freq, 1, child))
        
        
        return top_k


#Read_terms reads in the file and for each line we insert the word and its associated frequency to the root Trie

def read_terms(filename):

    root = Trie()
    try:
        with open(filename) as f:
            next(f)
            for line in f:
                if len(line.split(None)) > 0:
                    freq, name = line.split(None,1)
                    root.insert(name.strip().lower(), int(freq.strip()))
                
        return root
    except IOError:
        print "Could not read file:", filename


#Prints out top_k matches in the right format 

def print_top_k(top_k_matches):
        if not top_k_matches:
            print ('There is no match')
        else:
            for item in top_k_matches:
                print item[0], item[1]   

# Final method to print out desired output

def autocomplete(prefix, root, k):

    try:
        print_top_k(root.find_top_k(k, prefix))
    except:
        print "Error encountered"


def main():

    prefix = str(sys.argv[1])
    filename = str(sys.argv[2])
    k = int(sys.argv[3])
    assert k > 0, "k is not an positive integer: %r" % k
    root = read_terms(filename)
    autocomplete(prefix, root, k)
   
if __name__ == "__main__":
    main()




