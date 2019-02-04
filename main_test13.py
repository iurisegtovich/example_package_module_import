from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print('Hello from: '+frameinfo.filename+' @ '+str(frameinfo.lineno))

import sys
print(sys.path)

print('import module_hue')
import module_hue
print(module_hue.list1)

sys.path.insert(1, '../..')
print(sys.path)
print('?')
from example_package.subpackage_redpill.module_hue import list1

print(list1)

module_hue.list1[0]=999

list1[0]=-999

print(module_hue.list1)
print(list1)
