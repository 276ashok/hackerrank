def staircase(n):
    for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)

input=int(input())
staircase(input)

"""
sample input
6

sample output
     #
    ##
   ###
  ####
 #####
######
"""