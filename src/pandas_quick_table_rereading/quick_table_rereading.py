#quick_table_rereading.py
import pandas as pd
import hashlib
import os


def quick_table_rereading(path_file, header=0):
    pre, ext = os.path.splitext(path_file)
    path_file_pkl = pre+'_pkl.pkl'
    if this_file_has_been_read(path_file, path_file_pkl):
        df = pd.read_pickle(path_file_pkl)
    else:
        if ext in ['.xls', '.xlsx', '.xlsm', '.xlsb']:
            df = pd.read_excel(path_file, header=header)
        elif ext == '.csv':
            df = pd.read_csv(path_file, header=header)
        else :
            raise Exception("Module quick_table_rereading.py does not support format '" + ext + "'!")
        df.to_pickle(path_file_pkl)
    return df


def this_file_has_been_read(path_file, path_file_pkl):
    answer = False
    hash_table_file = os.path.join(os.path.abspath(path_file),  'hash_table.pkl')
    if os.path.exists(hash_table_file):
        df_hash_table = pd.read_pickle(hash_table_file)
    else:
        df_hash_table = pd.DataFrame(columns=['hash'])
    filename = os.path.basename(path_file)
    file_name_hash = hashlib.md5(filename.encode('utf-8')).hexdigest()
    file_hash = md5(path_file)
    try:
        if df_hash_table.loc[file_name_hash, 'hash'] == file_hash and \
                os.path.exists(path_file_pkl):
            answer = True
    except KeyError:
        answer = False
    if answer == False:
        df_hash_table.loc[file_name_hash, 'hash'] = file_hash
        df_hash_table.to_pickle(hash_table_file)
    return answer


def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


if __name__ == '__main__':
    path = os.getcwd()
    df = quick_table_rereading(path, 'SampleData.xlsx')
    print(df)
