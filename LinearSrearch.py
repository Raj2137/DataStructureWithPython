def serch_card(cards, query):
  position=0 #creating a position
  
  while position< len(cards):
      
    if cards[position]==query:
      return position
    position+=1

    #if position == len(cards): # return -1 if there is no element
      #return -1
  
  return -1
