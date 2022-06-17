"""
Suppose you need to write a load test for a server. You have studied the inter-arrival time of
requests to the server over a period of one year. From this data you have computed a histogram
58
of the distribution of the inter-arrival time of requests. In the load test you would like to generate
requests for the seryer such that the inter-arrival times come from the same distribution that was
observed in the historical data. The following problem formalizes the generation of inter-arrival
times.
Youaregivenrnumbersaswellasprobabilitiespo,pt,...,pn-r,whichsumuptol. Givenarandom
number generator that produces values in [0, 1) uniformly, how would you generate one of the n
numbers according to the specified probabilities? For example, if the numbers are 3,5,7,11, and
the probabilities are 9118,611.8,2118,1118, then in 1000000 calls to your program,3 should appear
roughly 500000 times,5 should appear roughly 333333 times, 7 should appear roughly 111111 times,
and 11 should appear roughly 55555 times.
"""
def nonuniform_random_number_generation(values, probabilities):
  """
  An easy way to create these intervals is to use p0,p0+pl,p0+p1+p2,...,p0+p1+p2+... +
Pn-1 as the endpoints. Using the example given in the problem statement, the four intervals are
[0.0,0.5), [0.5,0.833),10.833,0.944),10.944,1.0]. Now, for example, if the random number generated
uniformly in [0.0, 1.0] is 0.873, since 0.873 lies in [0.833,0.944), which is the third interval, we retum
the third numbeq, which is 7.
  """
  prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
  interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
  retrun values[interval_idx]

  
