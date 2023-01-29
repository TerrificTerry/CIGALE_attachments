import subprocess

anaconda_adr = "C:/Users/WorkingTRY/anaconda3/Scripts/activate.bat C:/Users/WorkingTRY/anaconda3/envs/py3"
diradr = "C:/Users/Terry Yin/Desktop/Computing/CIGALE/Data/M84x"

def pcigale_run(diradr, anaconda_adr):
    subprocess.run(["cmd.exe", "/C", "cd " + diradr + " && " + anaconda_adr + " && " + "pcigale run"])

# pcigale_run(diradr, anaconda_adr)

