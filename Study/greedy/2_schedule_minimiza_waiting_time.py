"""
Given service times for a setof queries, compute a schedule forprocessingthe queries thatminimizes
the total waiting time. Retum the minimum waiting time. For example, if the service times are
(2,5,1.,3),if wescheduleinthegivenordeq,thetotalwaitingtimeis0+(2)+(2+5)+(2+5 +1) =17.

If however, we schedule queries in order of decreasing service times, the total waiting time is
0+(5)+(5+3)+(5+3+2)=23.As we will see,for this example,the minimum waiting time is 10. 
"""

def minimum_total_waiting_time(service_times):
    # Sort the service times in increasing order
    service_times.sort()
    total_waiting_time = 0
    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries
    
    return total_waiting_time

print(minimum_total_waiting_time([2,5,1,3]))
