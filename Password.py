# Password generator
import random
import string

pass_len=12
charValues = string.ascii_letters + string.digits + string.punctuation

 # by list compression

password="".join([random.choice(charValues) for i in range(pass_len)])







 #by loop
# password=""
# for i in range(pass_len):
#   password += random.choice(charValues)


print("Your Password Is :-", password)


#  -------------------------THE END------------------------------