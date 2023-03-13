#read_exces_or_pkl.py
import pandas as pd
import hashlib
import os


def read_excel_or_pkl(base_path, filename, header=0):
    path_file_xlsx = base_path + filename
    path_file_pkl = base_path + 'pickle/' + filename.replace('xlsx', 'pkl')
    if this_file_has_been_read(base_path, filename, path_file_xlsx, path_file_pkl):
        df = pd.read_pickle(path_file_pkl)
    else:
        df = pd.read_excel(path_file_xlsx, header=header)
        df.to_pickle(path_file_pkl)
    return df


def this_file_has_been_read(base_path, filename, path_file_xlsx, path_file_pkl):
    answer = False

    base_path_pickle = os.path.join(base_path, 'pickle')
    if not os.path.exists(base_path_pickle):
        os.mkdir(base_path_pickle)
    hash_table_file = os.path.join(base_path,  'hash_table.pkl')
    if os.path.exists(hash_table_file):
        df_hash_table = pd.read_pickle(hash_table_file)
    else:
        df_hash_table = pd.DataFrame(columns=['hash'])
    file_name_hash = hashlib.md5(filename.encode('utf-8')).hexdigest()
    file_hash = md5(path_file_xlsx)
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
    df = read_excel_or_pkl(path+'/', 'SampleData.xlsx')
    print(df)
