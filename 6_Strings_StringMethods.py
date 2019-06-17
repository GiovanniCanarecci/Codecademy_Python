# Uncommented

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)
highlighted_poems_list=highlighted_poems.split(",")
print(highlighted_poems_list)
highlighted_poems_stripped=[]
highlighted_poems_stripped=[poem.strip() for poem in highlighted_poems_list]

print(highlighted_poems_stripped)
highlighted_poems_details=[]
highlighted_poems_details=[poem.split(":") for poem in highlighted_poems_stripped]
titles=[]
poets=[]
dates=[]
for list in highlighted_poems_details:
  titles.append(list[0])
  poets.append(list[1])
  dates.append(list[2])

for i in range(len(highlighted_poems_details)):
  #print(f"The poem {titles[i]} was published by {poets[i]} in {dates[i]}.")
  print("The poem {} was published by {} in {}.".format(titles[i],poets[i],dates[i]))
