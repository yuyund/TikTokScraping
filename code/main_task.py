from tiktok import create_data
import spread
from pprint import pprint


def main_task():
    sp = spread.Spreadsheet()
    sp.set_header()

    urls = sp.get_URL()
    data = create_data(urls)

    for i in range(len(urls)):
        sp.update_row(i+2,data[i])
