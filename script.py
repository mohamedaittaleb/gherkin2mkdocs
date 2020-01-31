from os import listdir, rename
from os.path import isfile, join

def build_page_row(file):
    return '  - ' + file.rstrip() + ': ' + file.rstrip() + '.md' + '\n'

features_directory = './docs'
mkdocs_file_name = 'mkdocs.yml'
header = open("header.yml",'r')
footer = open("footer.yml",'r')

files_no_ext = [".".join(f.split(".")[:-1]) for f in listdir(features_directory)]

with open(mkdocs_file_name, "w") as mkdocs:
    mkdocs.write(header.read() + '\n')
    for file in files_no_ext:
        mkdocs.write(build_page_row(file))
    mkdocs.write(footer.read() + '\n')
