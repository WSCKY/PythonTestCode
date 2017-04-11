#!/usr/bin/python

# ------ while ------ #
n = 100
sum = 0
counter = 1

while counter <= n:
  sum = sum + counter
  counter += 1

print('1 + 2 + ... + 100 = %d' %(sum))

languages = ["C", "C ++", "Perl", "Python"]
for x in languages:
  print (x)
