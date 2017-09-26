from prettytable import PrettyTable
from utils.utils_date_time import get_date_from_epoch
from utils.utils_date_time import DATE_FORMAT_TIME

def create_readable_table_from_jsonarray(json, epoch=False, format = DATE_FORMAT_TIME):
    if json == None or len(json)==0:
        print("JSON == NONE OR LENGTH OF IT IS ZERO")
        return None
    headers_table = []

    for col_name in json[0]:
        headers_table.append(col_name)
    table = PrettyTable(headers_table)

    for interval in json:
        row_array = []
        for attr in interval:
            # if epoch was passed print time as epoch
            if epoch:
                row_array.append(interval[attr])
            # if epoch=False print time as readable date
            else:
                if attr == 'time':
                    row_array.append(get_date_from_epoch(interval[attr], format))
                else:
                    row_array.append(interval[attr])
        table.add_row(row_array)
    return table

def print_readable_table(json):
    print(create_readable_table_from_jsonarray(json))