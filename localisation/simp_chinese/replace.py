import os

folder_path = 'F:\\Onedrive\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\hrs\\localisation\\simp_chinese\\replace'
for filename in os.listdir(folder_path):
    new_filename = filename.replace('l_english', 'l_simp_chinese')
    os.rename(os.path.join(folder_path, filename),
              os.path.join(folder_path, new_filename))
