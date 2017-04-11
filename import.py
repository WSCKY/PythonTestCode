#!/usr/bin/python

import sys
import test_module
import module_1 # call "module_1.fib(200)"
#from module_1 import fib # call "fib(200)"
#from module_1 import * # import all

test_module.welcome('kyChu');
print test_module.__name__
welcome = test_module.welcome
welcome('kaiyang')

print dir(module_1) # all of module_1
module_1.fib(200)

print dir() # current module

print 'input argument:'
for i in sys.argv:
  print i

print dir(sys)
print '\nPython path is: ', sys.path, '\n'

