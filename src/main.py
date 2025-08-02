import os
import shutil
import sys

from generate_page import generate_page, generate_pages_recursive
from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
basepath = sys.argv[0] if len(sys.argv) > 0 else "/"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(
        os.path.join(dir_path_content),
        template_path,
        os.path.join(dir_path_public),
        basepath,
    )


main()
