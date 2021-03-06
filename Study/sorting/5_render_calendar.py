"""
Consider the problem of designing an online calendaring application. One component of the design
is to render the calendar, i.e., display it visually.

Suppose each day consists of a number of events, where an event is specified as a start time and
a finish time. Individual events for a day are to be rendered as nonoverlapping rectangular regions
whose sides are parallel to the X- and Y-axes. Let the X-axis correspond to time. If an event starts
at time b and ends at time e, the upper and lower sides of its corresponding rectangle must be at b
and e, respectively. 

Suppose the Y-coordinates for each day's events must lie between 0 and L (a pre-specified
constant), and each event's rectangle must have the same "height" (distance between the sides
parallel to the X-axis). Your task is to compute the maximum height an event rectangle can have.
In essence, this is equivalent to the following problem.

Write a program that takes a set of events, and determines the maximum number of events that
take place concurrently.
"""

# Time O(nlogn)

Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(A):
    # Create an array of all endpoints
    E = ([Endpoint(event.start, True)for event in A] + [Endpoint(event.finish, False) for event in A])
    # sorts the endpoint array according to the time, putting start times before end times
    E.sort(key = lambda e: (e.time, not e.is_start))

    # Track the number of simultaneous events, record the maximum number of simultaneous events
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(max_num_simultaneous_events, num_simultaneous_events)
        else:
            num_simultaneous_events -= 1

    return max_num_simultaneous_events


