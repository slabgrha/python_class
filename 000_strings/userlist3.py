#!/usr/bin/env python2.7

import pwd

user_list = pwd.getpwall()

for entry in user_list:
  print( entry.pw_name )
