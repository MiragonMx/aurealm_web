import os
import glob

search_path = "content/"
assets_path = "assets/img/"

file_list = glob.glob(search_path + '/**/img/*', recursive=True)

for file in file_list:
    filename = os.path.basename(file)
    os.rename(file, assets_path + filename)
