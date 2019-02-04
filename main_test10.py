from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print('Hello from: '+frameinfo.filename+' @ '+str(frameinfo.lineno))

print('example_package import subpackage_redpill')
from example_package import subpackage_redpill

print(dir(subpackage_redpill))

print('from example_package.subpackage_redpill.module_hue import list1')
from example_package.subpackage_redpill.module_hue import list1

print(list1)

