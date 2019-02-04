from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print('Hello from: '+frameinfo.filename+' @ '+str(frameinfo.lineno))

list1=[1,2,3]
