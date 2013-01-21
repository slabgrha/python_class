#!/usr/bin/env python2.7

from subprocess import check_output

output = check_output(['cat', '/etc/passwd'])

user_list = output.splitlines()

for user_entry in user_list:
  user_name = user_entry.split(':')[0]
  print(user_name)
