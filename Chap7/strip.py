
#! python3
# strip.py - strips shit.
import re

huwite = re.compile(r'(^(\s+)|(\s+)$)')

def strip(str, replace=None):
    if replace:
        reg = re.compile(f"^([{re.escape(replace)}])+|([{re.escape(replace)}])+$")
        return reg.sub('', str)
    return huwite.sub('', str)

print(strip('      begin'))
print(strip('          end'))
print(strip('   middle    '))
print(strip('...aaabegin', '.a'))
print(strip('...aaaend', '.a'))
print(strip('...aa  amiddle....aaa  a', '.a'))
