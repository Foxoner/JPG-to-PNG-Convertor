import sys
import os
from PIL import Image

folder_path1 = sys.argv[1]
folder_path2 = sys.argv[2]

if not os.path.exists(folder_path2):
    os.mkdir(folder_path2)

for filename in os.listdir(folder_path1):
    try:
        img = Image.open(f'{folder_path1}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{folder_path2}{clean_name}.png', 'png')
        print('all done!')

    except OSError:
        pass

