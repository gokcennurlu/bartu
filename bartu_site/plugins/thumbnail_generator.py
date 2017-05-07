import distutils.dir_util
import shutil
import os
from cactus.utils.filesystem import fileList
from PIL import Image, ImageOps

def preBuild(site):
    print("Checking for thumbnails")
    for path in fileList(os.path.join(site.paths['static'], 'images/gallery')):
        filename = os.path.basename(path)
        parent_folder_name = os.path.basename(os.path.dirname(path))
        if parent_folder_name != 'thumbs':
            thumbs_dir = os.path.join(os.path.dirname(path), 'thumbs')
            if not os.path.exists(thumbs_dir):
                os.makedirs(thumbs_dir)
                print("Thumbs dir created for %s" % parent_folder_name)

            thumb_image_path = os.path.join(thumbs_dir, filename)

            if not os.path.exists(thumb_image_path):
                _im = Image.open(path)
                _im = ImageOps.fit(_im, (400, 320))
                _im.save(thumb_image_path, "jpeg")
                print("Thumbnail generated for %s in %s" % (filename, parent_folder_name))

    print("TEST########")