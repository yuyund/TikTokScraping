import glob
import json
import tkinter as tk
import tk_func
from functools import partial

google_files = glob.glob("google_json/*.json")
spreadsheet_files = glob.glob("spreadsheet_json/*.json")
with open(google_files[0],"r") as f:
    gj_obj = json.load(f) # service
with open(spreadsheet_files[0],"r") as f:
    sj_obj = json.load(f)


def ok(ui,sj_obj):
    with open(spreadsheet_files[0],"w") as f:
        sj_obj["sheet_url"] = f"{ui.get_sheetbox()}"
        sj_obj["custom_verifyFp"] = f"{ui.get_verify_addr()}"
        sj_obj["interval"] = f"{ui.get_interval()}"
        json.dump(sj_obj,f)
    ui.root.quit()
def cancel(ui):
    ui.root.quit()

# gj_obj['client_email']
# sj_obj.get("sheet_url")
ui = tk_func.UI(gj_obj,sj_obj)
ui.set_okbutton(partial(ok,ui,sj_obj))
ui.set_cancelbutton(partial(cancel,ui))
ui.start()
