import gspread
from oauth2client.service_account import ServiceAccountCredentials
import glob
import json



class Spreadsheet:
    def __init__(self):
        spreadsheet_files = glob.glob('spreadsheet_json/*.json')
        with open(spreadsheet_files[0],"r") as f:
            sj_obj = json.load(f)
            url = sj_obj.get("sheet_url")
        client = self.__make_client(url)
        self.sheet = client.sheet1

    def __make_client(self,url):
        files = glob.glob("google_json/*.json")
        scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(files[0], scope)
        auth = gspread.authorize(creds)
        client = auth.open_by_url(url)
        return client
    def set_header(self):
        if not self.sheet.row_values(1):
            tmp = ["TikTokURL","更新日時",
               "フォロワー","いいね",
               "コメント", "シェア","再生数","投稿日時"]
            for i in range(len(tmp)):
                self.sheet.update_cell(1,i+1,tmp[i])
    def get_URL(self):
        return self.sheet.col_values(1)[1:]
    def update_row(self,row_number,lst):
        if lst:
            for i in range(len(lst)):
                if lst[i]:
                    self.sheet.update_cell(row_number,i+2,str(lst[i]))
