# Uncommented

def username_generator(first_name,last_name):
  try:
    out= first_name[:3] + last_name[:4]
  except IndexError:
     out= first_name + last_name
  return out

def password_generator(username):
  out=""
  for i in range(len(username)):
    out += username[i-1]
  return out