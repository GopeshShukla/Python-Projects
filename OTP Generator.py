# OTP generator
import random   # this is module or packages

import string    # this is module or packages

OTP_len=6
charValues = string.digits

 # by list compression

# password="".join([random.choice(charValues) for i in range(OTP_len)])

#by loop
password=""
for i in range(OTP_len):
  password += random.choice(charValues)


print("Your OTP Is :-", password)
