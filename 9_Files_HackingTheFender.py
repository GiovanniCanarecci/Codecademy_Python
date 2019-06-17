import csv
import json

#We need to create a list of users whose passwords have been compromised.
compromised_users=[]
with open("passwords.csv") as password_file:
  password_csv=csv.DictReader(password_file)
  for password_row in password_csv:
    #print(password_row['Username'])
    compromised_users.append(password_row) 
#print(compromised_users)

#Start a new with block, opening a file called compromised_users.txt. 
# Open this file in write-mode, saving the file object as compromised_user_file.
with open("compromised_users.txt","w") as compromised_user_file:
  for compromised_user in compromised_users:
    #Write the username of each compromised_user in compromised_users to compromised_user_file.
    compromised_user_file.write(compromised_user['Username']+", ")


with open("boss_message.json","w") as boss_message:
  boss_message_dict={"recipient":"The Boss", "message" : "Mission Success"}
  #Write out boss_message_dict to boss_message using json.dump()
  json.dump(boss_message_dict,boss_message)
  
#Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv"
# file completely.
with open("new_passwords.csv","w") as new_passwords_obj:
  slash_null_sig=""" 
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __    ____  _  _ 
 ___   / ___)(  )   / _\  / ___)/ )( \#
(___)  \___ \/ (_/\/    \ \___ \) __ (
       (____/\____/\_/\_/ (____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""
  new_passwords_obj.write(slash_null_sig)