import math
"""this program is meant to simulate Arbitrage, which is the simultaneous
buying and selling of an asset in different markets to profit off the difference
in an asset's price in different currencies. It takes in a list of exchange
rates as in the following example:
5 6
NYSE JPX 110
JPX LSE 90
LSE SSE 110
SSE NYSE 111
SSE AMS 90
AMS NYSE 90

expected output:5

where the first line of input indicates the number of total exchanges n and the
number of possible trades m, and the remaining lines represent the exchange rate between
two stock exchanges. My program outputs the minimum possible transaction cost as percentage
that would eliminate the possiblity of profitable arbitrage.
"""
def main():
    #reading input to list data
    init = input().split()
    init[0] = int(init[0])
    init[1] = int(init[1])
    data = []
    for i in range(init[1]):
        temp = input().split()
        temp[2] = int(temp[2])
        data.append(temp)
    #For abitrage to be profitable, one must start and end up in the same currency
    #Therefore my program tracks the maximum cycle in order to find which order is most profitable.
    threadlist = []
    maxi = 0
    maxcycle = []
    cyclelist = []
    for i in data:
        #initializes a possible thread in threadlist since one could begin a cycle by making the exchange described in row i
        #A "thread" will track the possible buy/sell actions a trader can take starting with a given trade to loop back to the original stock exchange market
        i.append(1)
        threadlist.append(i)
        #searches the list of active threads for those which are currently in the given market to update them
        lis = search(threadlist, 1, i[0])
        if lis != []:
            for j in lis:
                #tracks each of the threads identified by threadlist, creates an updated copy, and adds it to the list of potentially active threads
                temp = threadlist[j][:]
                temp[1] = i[1]
                temp[2] = temp[2] * i[2]/100
                temp[3] += 1
                threadlist.append(temp)
        deadlist = []
        #identifies any cycles and removes them from the list of active threads
        for b in threadlist:
            if b[0] == b[1]:
                cyclelist.append(b)
                deadlist.append(b)
        for c in deadlist:
            threadlist.remove(c)
    for i in cyclelist:
        if i[2] > maxi:
            maxi = i[2]
            maxcycle = i
    #given the percent profit, identifies the transaction fee that would eliminate arbitrage
    final = (100/maxcycle[2])**(1/maxcycle[3])
    final = 1-final
    print(math.ceil(final*100))
#searches a column of a 2d list for a query and returns a list of the indices of results                            
def search(li, index, query):
    res = []
    for i in range(len(li)):
        if li[i][index] == query:
            res.append(i)
    return res
    
if __name__ == "__main__":
    main()
