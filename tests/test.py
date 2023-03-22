import os
import pqtrr.table_reading as tr

if __name__ == '__main__':
    path = os.path.join(os.getcwd(), 'tests', 'SampleData.xlsx')
    df = tr.quick_table_rereading(path)
    print(df)
    # print(path)
