"""
https://leetcode.com/discuss/interview-question/1920662/Google-or-Phone-or-Calculate-Total-Wait-Time

Calculate the total wait time for a customer C to speak to an agent given N agents, M customers, and T[] time for an agent to serve a customer. T[i] represents the amount of time it takes for an agent i to serve one customer. One agent can serve one customer at a time. All N agents can serve concurrently. The customer chooses the agent with the lowest wait time.

Examples:

N = 2
M = 2
T = [4, 5]
First customer chooses agent 1. Second customer chooses agent 2.
Customer C will wait 4 minutes.


N = 2
M = 4
T = [4, 5]

    | |   |  |  12   15 16
First customer chooses agent 1. Second customer chooses agent 2.
Third customer chooses agent 1. Forth customer chooses agent 2.
Customer C will wait 8 minutes.

0 -> 1
1 -> 2
wait 4
2 -> 1
wait 1
3 -> 2

keep a curr_time 
keep a availability heap
[(next_avail_time, agent_cost, agent)]
0, 1, 0, 1
wait = get_available_agent()
curr_time += wait
use_agent((curr_time + agent_cost, agent_cost, agent))


O(M * log(N))


Initial questions:

Bounds on N and M - No bounds
Can N or M be zero - Both can be zero
Are the T values constant - Yes
Are the T values integers - Yes

"""
