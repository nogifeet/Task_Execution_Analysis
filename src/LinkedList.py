"""
Node Class:
    This is responsible for storing task details in the class and can be added to linked list
"""
class Node:
    #Constructor Implementation
    def __init__(self,taskID,start,end, duration):
        
        self.data = {'task_id':taskID , 'start_time':start, 'end_time':end , 'duration':duration}
        self.next = None 
    
"""
LinkedList Class:
    This is responsible for implementing Linked List for the tasks and is used for implementing
    various aggregate operations.

"""
class LinkedList:
    #Constructor Implementation
    def __init__(self):
        self.head = None
        
        
    #This method will return the head of the linked list
    def get_list_head(self):
        return self.head
    
    #This method is responsible for printing the linked list nodes
    def print_linked_list(self):
       temp = self.head 

       while temp:
           print(temp.data)
           temp = temp.next 
        
    #This method is responsible for inserting node in the linked list 
    #in the beginning or at end based on the flag as insert_at_starting
    def insert_node(self, node:Node, insert_at_starting=0):
        
        if insert_at_starting:

            node.next = self.head 
            self.head = node 
        
        else:

            if self.head is None:
                node.next = self.head 
                self.head = node 
        
            else:

                temp = self.head 

                while temp.next!=None:
                    temp = temp.next 
                
                temp.next = node 
                node.next = None 

    
    #This method is responsible for printing the linked list nodes in reverse order
    def print_in_reverse(self, node):
        
        if node.next is None:
            print(node.data)
            return 
        
        self.print_in_reverse(node.next)

        print(node.data)