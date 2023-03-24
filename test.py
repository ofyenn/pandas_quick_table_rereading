import os
import pfrtf

if __name__ == '__main__':
    path = os.path.join(os.getcwd(), 'tests', 'SampleData.xlsx')
    df = pfrtf.fast_read_file(path)
    print(df)
