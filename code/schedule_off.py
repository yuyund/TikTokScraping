import json
import glob

interval_path = glob.glob("spreadsheet_json/*.json")
with open(interval_path[0],"r") as f:
    obj = json.load(f)
with open(interval_path[0],"w") as f:
    obj["run"] = "False"
    json.dump(obj,f)
