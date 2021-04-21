#introduction to madlib app, instructions
print ('Welcome to the Madlib app, Fill in the blanks with the proper parts of speech!')
#parts of speech include- nouns, verbs, adjectives, pronoun, adverb, preposition, places, items, exclamation, emotion, form of transportation, and color
speech = ['noun', 'verb',  'adjective','pronoun', 'adverb', 'preposition', 'place', 'item', 'exclamation', 'emotion', 'form of transportation', 'color']

for speech in speech: # traversal of List sequence
   print ('Parts of speech needed :', speech)

#speech comands

noun =input('noun:')
noun2 =input('noun:')
verb= input('verb:')
adverb= input('adverb:')
place= input('place:')
place2= input('Place2:')
preposition= input('preposition:')
preposition2= input('preposion2:')
item= input('item:')
formoftransportation=input('form of transportation:')
emotion= input('emotion:')
color= input('color:')
adj= input('adjective:')
excla= input ('exclamation:')

#print out story plus combine inputs
print ('I once had a dream that I was a ' + noun+ '. I would ' + verb + adverb+ ', towards the ' + place+ preposition + ' I was at '+ place2 +' I would use '+ item +'. This '+ item + ' would help,me turn into a ' + formoftransportation+'. Then '+ preposition2+ 'I woke up I would feel'+emotion+'I would always look up at the ceiling after the dream and see the most vibrant '+ color+' from up on my ceiling. After staring at that color I would try going back into a ' + adj+ 'sleep. If that did not work I would yell,'+ excla  )
#ASCII art

print("___________.__                                .___")
print("\__    ___/|  |__   ____     ____   ____    __| _/")
print("  |    |   |  |  \_/ __ \  _/ __ \ /    \  / __ | ")
print("  |    |   |   Y  \  ___/  \  ___/|   |  \/ /_/ |")
print("  |____|   |___|  /\___  >  \___  >___|  /\____ | ")
print("               \/     \/       \/     \/      \/ ")