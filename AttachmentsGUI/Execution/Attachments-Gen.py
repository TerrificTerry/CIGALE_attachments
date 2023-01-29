import subprocess
import sys
import os

# def envst(env):
#     subprocess.run(["cmd.exe", "/K", env], shell=True)
    
# def cmr(cmd):
#     subprocess.run(["cmd.exe", "/C", cmd], shell=True)

anaconda_adr = "C:/Users/WorkingTRY/anaconda3/Scripts/activate.bat C:/Users/WorkingTRY/anaconda3/envs/py3"

# envst(anaconda_adr)

# subprocess.run(["cmd.exe", "/c", "pcigale"])

# envst("C:/Users/WorkingTRY/anaconda3/Scripts/activate.bat C:/Users/WorkingTRY/anaconda3/envs/py3")

diradr = "C:/Users/Terry Yin/Desktop/Computing/CIGALE/Data/M84x"
final_command = "cd " + diradr + " && " + anaconda_adr

def addcmd(cmd):
    fc = final_command
    fc = fc + " && " + cmd
    return fc

final_command = addcmd("pcigale genconf")

subprocess.run(["cmd.exe", "/C", final_command])

# subprocess.run(["cmd.exe", "/C", "pcigale"])
