#We have provided you with two lists, letters and points. 
# We would like to combine these two into a dictionary that would map a letter to its point value.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#Using a list comprehension and zip, create a dictionary called letter_to_points that has 
# the elements of letters as the keys and the elements of points as the values.
letter_to_points = {letter:point for letter,point in zip(letters,points)}
#print(letter_to_points)

#Our letters list did not take into account blank tiles. 
#Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[" "]=0

#We want to create a function that will take in a word and return 
# how many points that word is worth.
def score_word(word):
  point_total=0
  for letter in word:
    #make your letter_to_points dictionary able to handle lowercase inputs as well
    if letter.upper() in letter_to_points.keys():
      point_total+=letter_to_points[letter.upper()]
  return point_total

brownie_points =score_word("BROWNIEzzz")
#print(brownie_points)

#Create a dictionary called player_to_words that maps players to a 
# list of the words they have played. 
player_to_words ={"player1":["BLUE","TENNIS","EXIT"], 
                  "wordNerd":["EARTH","EYES","MACHINE"], 
                 "Lexi Con" :["ERASER","BELLY","HUSKY"], 
               "Prof Reader"   :["ZAP","COMA","PERIOD"]}
player_to_points={}
def update_point_totals(player_to_words):
  #Iterate through the items in player_to_words. 
  # Call each player player and each list of words words.
  for player,words in player_to_words.items():
      player_points =0
      for word in words:
        player_points+=score_word(word)
      player_to_points[player]=player_points

#player_to_points should now contain the mapping of players to how many points they’ve scored. 
# Print this out to see the current standings for this game!
update_point_totals(player_to_words)     
print(player_to_points)

#play_word() — a function that would take in a player and a word, 
# and add that word to the list of words they’ve played
def play_word(player,word):
  player_to_words[player].append(word)
  
play_word("player1","CIAO")
#print(player_to_words)