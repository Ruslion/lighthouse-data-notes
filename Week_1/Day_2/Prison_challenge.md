```python
prison =  [1, 1, 0, 0, 0, 1, 0]
total_saved=0
while prison: #Loop will continue until there is an item in it.
    if prison[0]==1: #Unlock cell found, releasing prisoner
        del prison[0] #Deleting this item since we do not need it anymore
        total_saved+=1 #Counting saved ones
        #reverse the rest values in the list
        for i in range(len(prison)):
            if prison[i]==0:
                prison[i]=1
            else:
                prison[i]=0
        print(prison)
        print(f'Total saved {total_saved}')
    else:
        del prison[0] # Locked cell found, deleting item
        print(prison)
```
