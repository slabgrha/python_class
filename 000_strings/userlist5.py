#!/usr/bin/env python2.7

import pwd

user_list = pwd.getpwall()

# New - add format
#format = "%-10s\t%s"

# New - add header
#print("")
#print format % ("Username", "Home Directory")
#print("----------\t--------------")

for entry in user_list:
  print(entry.pw_name + "\t" + entry.pw_dir)
  #print format % (entry.pw_name, entry.pw_dir)

# New - print footer
#print("")
