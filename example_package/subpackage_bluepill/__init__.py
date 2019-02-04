from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print('Hello from: '+frameinfo.filename+' @ '+str(frameinfo.lineno))

from . import module_ping
