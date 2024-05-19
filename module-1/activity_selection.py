#!/usr/bin/env python3

class Activity:
    def __init__(self, name, initial_start_time, initial_finish_time):
        self.name = name
        self.start_time = initial_start_time
        self.finish_time = initial_finish_time
        
    def conflicts_with(self, other_activity):
        # No conflict exists if this activity's finish_time comes
        # at or before the other activity's start_time
        if self.finish_time <= other_activity.start_time:
            return False
            
        # No conflict exists if the other activity's finish_time
        # comes at or before this activity's start_time
        elif other_activity.finish_time <= self.start_time:
            return False
            
        # In all other cases the two activity's conflict with each
        # other
        else:
            return True

# Main program to test Activity objects
activity_1 = Activity('History museum tour', 9, 10)
activity_2 = Activity('Morning mountain hike', 9, 12)
activity_3 = Activity('Boat tour', 11, 14)

print('History museum tour conflicts with Morning mountain hike:',    
       activity_1.conflicts_with(activity_2))
print('History museum tour conflicts with Boat tour:', 
       activity_1.conflicts_with(activity_3))
print('Morning mountain hike conflicts with Boat tour:', 
       activity_2.conflicts_with(activity_3))
