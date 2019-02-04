from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print('Hello from: '+frameinfo.filename+' @ '+str(frameinfo.lineno))

set1=set(vars())

print('from example_package.subpackage_redpill import module_br')
from example_package.subpackage_redpill import module_br

print(set(vars())-set1-{'set1'})

