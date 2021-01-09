# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"
outcomes=["H", "T"]
def coin_flips(n):
    global outcomes
    if n == 1:
        return outcomes


    else:     
       return coin_flips(n - 1) + coin_flips(n - 1)
       
    
    
    # pass

print(coin_flips(3)) 
# => ["HH", "HT", "TH", "TT"]