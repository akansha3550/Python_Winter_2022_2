import glob
import os
dir_name = r'C:\Program Files\Python311'

count = 0

for root_dir, cur_dir, files in os.walk(dir_name):
    count += len(files)
print('file count:', count)

#computes the total space occupied by all those files.

list_of_files = filter(os.path.isfile,
                        glob.glob(dir_name + '/**/*', recursive=True))

files_with_size = [(file_path, os.stat(file_path).st_size)
                    for file_path in list_of_files]

for file_path, file_size in files_with_size:
    print("{} : {}MB".format(file_path, round(file_size / (1024 * 1024), 3)))



