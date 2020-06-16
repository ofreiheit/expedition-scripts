###Expedition System Boolean
#Skript to check the SystemBooleans
from ctypes import *
from enum import Enum
import winreg
import json
import psutil

class SystemBoolean(Enum):
    UTC = 2
    Mag = 4
    Quit = 24
    UserFlag = 44

REG_PATH = 'SOFTWARE\Expedition\Core'
def get_dll_location():
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, 'Location')
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None
dll_location = get_dll_location()

expedition = windll.LoadLibrary(dll_location +'\ExpDLL.dll')

def get_sys_bool(sys_channel, boat_id): 
    results_bool = c_bool()
    expedition.GetSysBool(c_short(sys_channel.value), pointer(results_bool))
    return results_bool.value
i = 0
i = i+1
boat_id = 0
results_bool = {}

for channel in SystemBoolean:
    results_bool[channel.name] = get_sys_bool(channel, boat_id)
print (results_bool)