__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

print('######################## current dir ######################')
import os
current_dir = os.getcwd()
print(current_dir)


print('######################## 1 ######################')


def clean_cache():
    import os
    if os.path.exists(r'cache'):
        for file in os.scandir(r'cache'):
            os.remove(file.path)

    else:
        os.mkdir(r'cache')
    return


clean_cache()

print('######################## 2 ######################')


def cache_zip(path_zip, path_cache_dir):
    import shutil
    shutil.unpack_archive(path_zip, path_cache_dir)


filename = current_dir + "/data.zip"
extract_dir = current_dir + "/cache"
cache_zip(filename, extract_dir)


print('######################## 3 ######################')


def cached_files():
    import os
    file_names = os.listdir(current_dir+'\cache')
    extract_dir = current_dir+'\cache'
    for i in range(len(file_names)):
        file_names[i] = extract_dir + '\\' + file_names[i]       
    return file_names


print(cached_files())

print('######################## 4 ######################')

file_names = cached_files()


def find_password(file_names):
    for i in range(len(file_names)):
        f = open(file_names[i], "r")
        data1 = f.read()
        if 'password' in data1:
            data1.find('password')
            f = open(file_names[i], "r")
            data2 = f.readlines()
            filter_object = list(filter(lambda a: 'password' in a, data2))
            text_str = filter_object[0]
            break
    return text_str[10:-1]


print(find_password(file_names))
