```python
from collections import Counter
def poker_hand_ranking(lst):
    cards_suited = False
    cardsInSeq=False
    suits=[]
    cards=[]
    right_order=['A','K','Q','J','10','9','8','7','6','5','4','3','2'] #The right order of the face cards

    #iterating list
    for item in lst:
        suits.append(item[-1])  #Adding suit to the list
        cards.append(item[:-1]) #Adding face card to the list
    count_suits=Counter(suits)  #counting suits by counter
    count_cards=Counter(cards)  #counting face cards by counter
    
    if count_suits.most_common(1)[0][1]==5:
        #all suited cards and no card duplicate
        cards_suited= True
        
    if count_cards.most_common(1)[0][1]==4:
        #Four of a Kind detected
        return 'Four of a Kind'
    elif count_cards.most_common(1)[0][1]==1:
        #All face cards are different
        #Need to define the order of the cards
        count_order=0
        cardFound=False
        for card in right_order:
            if card in cards:
                cardFound=True
                if count_order==0:
                    high_card= card #Defining the high card in hand
                count_order+=1
                #print(f'Count = {count_order}, card = {card}')
                if count_order==5:
                    cardsInSeq=True
                    break #all five cards in order
            elif cardFound and count_order>0:
                if not cards_suited:
                    return "High card " + high_card 
                break     #order is broken. No need to continue loop
    elif count_cards.most_common(1)[0][1]==3:
        #Three of kind found. Need to verify for full house
        if count_cards.most_common(2)[1][1]==2:
            #Full house detected
            return "Full house"
        else:
            return "Three of a kind"
    elif count_cards.most_common(1)[0][1]==2:
        #Pair detected. Need to verify for second pair
        if count_cards.most_common(2)[1][1]==2:
            return "Two pairs"
        else:
            return "Pair"
    if cards_suited:
        if cardsInSeq:
            if high_card=='A':
                return "Royal Flush"
            else:
                return "Straight Flush"
        else:
            return "Flush"
    elif cardsInSeq:
        return "Straight"
        
print(poker_hand_ranking(["10h", "10c", "10d", "Ah", "Ac"]))
print(poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]))
print(poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]))
print(poker_hand_ranking(["3h", "5h", "Qh", "9h", "Ah"]))
print(poker_hand_ranking(["9h", "10h", "Qh", "Jh", "Kc"]))
```