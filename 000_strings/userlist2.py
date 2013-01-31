#!/usr/bin/env python

user_file = open('/etc/passwd', 'r')

user_list = user_file.readlines()

for line in user_list:
  user = line.split(":")[0]
  print( user )
