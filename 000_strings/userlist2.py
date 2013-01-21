#!/usr/bin/env python

user_file = open('/etc/passwd', 'r')

for line in user_file.readlines():
  print( line.split(':')[0] )
