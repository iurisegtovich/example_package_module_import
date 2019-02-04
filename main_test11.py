from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print('Hello from: '+frameinfo.filename+' @ '+str(frameinfo.lineno))

print('example_package import subpackage_bluepill')
from example_package import subpackage_bluepill

print(dir(subpackage_bluepill))

print(subpackage_bluepill.module_ping.list1)

print('from example_package.subpackage_bluepill.module_ping import list1')
from example_package.subpackage_bluepill.module_ping import list1

print(list1)

subpackage_bluepill.module_ping.list1[0]=999

list1[0]=-999

print(subpackage_bluepill.module_ping.list1)
print(list1)
