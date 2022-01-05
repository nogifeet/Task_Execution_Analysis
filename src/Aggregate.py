from src.LinkedList import LinkedList

"""
Aggregate class is responsible for implementating various operations on the linked list
    1. Get Minimum Timed Task Details
    2. Get Maximum Timed Task Details
    3. Get Average of all the execution times of the tasks pushed in the linked list
"""

class Aggregate:
    
    #Initializing linked list object for various operations 
    def __init__(self, linked_list:LinkedList):
        self.linked_list = linked_list
    
    def get_maximised_time_task(self):

        '''
        Function responsible for searching the task having maximum execution time among all the tasks
        '''

        maxmimum_time = self.linked_list.head.data['duration']
        maximum_task = self.linked_list.head.data

        temp = self.linked_list.head.next 

        while temp:
            if temp.data['duration'] >= maxmimum_time:
                maxmimum_time = temp.data['duration']
                maximum_task = temp.data

            temp = temp.next 
        
        return maximum_task,maxmimum_time



    
    def get_minimised_timed_task(self):

        '''
        Function responsible for searching the task having minimum execution time among all the tasks
        '''
        
        minimum_time = self.linked_list.head.data['duration']
        minimum_task = self.linked_list.head.data

        temp = self.linked_list.head.next 

        while temp:
            if temp.data['duration'] <= minimum_time:
                minimum_time = temp.data['duration']
                minimum_task = temp.data

            temp = temp.next 
        
        return minimum_task,minimum_time


        
    def get_average_time_of_all_tasks(self):
        '''
        Function responsible for calculating average of the all execution times of the tasks in the linked list
        '''
        
        nodes = 1
        total_time = self.linked_list.head.data['duration']

        temp = self.linked_list.head.next 

        while temp:
            total_time += temp.data['duration']
            nodes+=1
            temp = temp.next 
        
        avg_time = total_time/nodes

        return avg_time,total_time,nodes

        


       

