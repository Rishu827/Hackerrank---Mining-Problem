# Enter your code here. Read input from STDIN. Print output to STDOUT
def mining():
    n,k=map(int,input().split())

    goldTons=[0]*n
    minesLocation=[None]*n
    pickupMine=[0]*n #int pickupMine[n]
    costarray=[0]*n
    for i in range(n):
        loc,wt=map(int,input().split())
        goldTons[i]=wt
        minesLocation[i]=loc
        
    def recomputedest(i):
        left=None
        right=None
        for j in range(i-1,-1,-1):
            if minesLocation[j]!=None:
                left=j
                break    
        if i<n-1:
            for j in range(i+1,n):
                if minesLocation[j]!=None:
                    right = j
                    break
        else:
            pickupMine[i]=left
            costarray[i]=goldTons[i]*abs(minesLocation[pickupMine[i]]-minesLocation[i])
            #print 'New cost for mine',i,':',costarray[i]
            return
        if right==None:
            pickupMine[i]=left
            costarray[i]=goldTons[i]*abs(minesLocation[pickupMine[i]]-minesLocation[i])
            #print 'New cost for mine',i,':',costarray[i]
            return        
        if i==0 or left==None:
            pickupMine[i]=right
            costarray[i]=goldTons[i]*abs(minesLocation[pickupMine[i]]-minesLocation[i])
            #print 'New cost for mine',i,':',costarray[i]
            return
        #print 'Recomputed for',i,'Right:',right,'Left:',left
        pickupMine[i]= right if abs(minesLocation[right]-minesLocation[i])<abs(minesLocation[left]-minesLocation[i]) else left
        costarray[i]=goldTons[i]*abs(minesLocation[pickupMine[i]]-minesLocation[i])
        #print 'New cost for mine',i,':',costarray[i]
        return
    #print minesLocation
    for i in range(n):
        recomputedest(i)
        
    nodes=n
    #print pickupMine
    #print costarray
    tot=0
    while nodes>k:
        #print '\tMine removed:',costarray.index(min(costarray)),
        nodes = nodes -1
        
        #print 'Nodes left:',nodes
        moved = costarray.index(min(costarray))
        #print 'Cost Added:',costarray[moved]
        minesLocation[moved]=None
        #print 'New Mine locations:',minesLocation
        goldTons[pickupMine[moved]] += goldTons[moved] #pickupMine[moved] tells the mine where mine indexed at moved is copied to
        
        tot = tot + costarray[moved]
        costarray[moved]=float('inf')
        goldTons[moved]=None
        #print 'New Weights',goldTons
        
        if nodes!=k:
            recomputedest(pickupMine[moved])
            for i in range(n):
                if pickupMine[i]==moved and minesLocation[i]!=None:
                    #print i
                    recomputedest(i)
        #print 'New Costs:',costarray
                
    return tot