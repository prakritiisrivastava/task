import os
import shutil


src_dir = os.getcwd()  
dest_dir = os.path.join(src_dir, "Configs")

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Copy the ActionFiles folder to the Configs folder
action_files_src = os.path.join(src_dir, "ActionFiles")
action_files_dest = os.path.join(dest_dir, "ActionFiles")
shutil.copytree(action_files_src, action_files_dest)

# Move the remaining files to the Configs folder, excluding .gitignore and readme.md
for file_name in os.listdir(src_dir):
    src_file = os.path.join(src_dir, file_name)
    dest_file = os.path.join(dest_dir, file_name)

    if os.path.isfile(src_file) and file_name not in [".gitignore", "readme.md"]:
        shutil.move(src_file, dest_file)

print("Executed successfully.")