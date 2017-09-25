from prettytable import PrettyTable
from utils.utils_date_time import get_date_from_epoch
from utils.utils_date_time import DATE_FORMAT_TIME

def create_readable_table_from_jsonarray(json, epoch=False, format = DATE_FORMAT_TIME):
    print("len: {}".format(len(json)))
    if json == None or len(json)==0:
        print("ERROR")
        return None
    headers_table = []
    print(json)
    for col_name in json[0]:
        headers_table.append(col_name)
    table = PrettyTable(headers_table)
    for interval in json:
        row_array = []
        for attr in interval:
            if epoch: #if epoch was passed print time as epoch
                row_array.append(interval[attr])
            else:#if epoch=False print time as readable date
                if attr == 'time':
                    row_array.append(get_date_from_epoch(interval[attr], format))
                else:
                    row_array.append(interval[attr])
        table.add_row(row_array)
    return table

def create_readable_table_from_jsondict(json):
    headers_table = []


def print_readable_table(json):
    print(create_readable_table_from_jsonarray(json))