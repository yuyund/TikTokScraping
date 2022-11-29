import main_task
import schedule
import json
import glob
import threading
from time import sleep
from functools import partial

quit_flag = [False]

def quit_check():
    with open(interval_path[0],"r") as f:
        obj = json.load(f)
        if obj.get("run") == "False":
            quit_flag[0] = True
            schedule.clear("tiktok")




interval_path = glob.glob("spreadsheet_json/*.json")
with open(interval_path[0],"r") as f:
    obj = json.load(f)
    interval = obj.get('interval')
with open(interval_path[0],"w") as f:
    obj["run"] = "True"
    json.dump(obj,f)




if interval:# 取得間隔を設定
    # schedule.every(int(interval)).minutes.do(main_task.main_task).tag("tiktok")
    schedule.every(30).seconds.do(main_task.main_task).tag("tiktok")
    schedule.every(30).seconds.do(quit_check).tag("tiktok")



while True:
    schedule.run_pending()
    if quit_flag[0]:
        break
    sleep(10)
