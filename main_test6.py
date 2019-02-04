from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print('Hello from: '+frameinfo.filename+' @ '+str(frameinfo.lineno))

print('import example_package')
import example_package
