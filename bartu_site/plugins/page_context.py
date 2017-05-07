#coding:utf-8
import os

from cactus.utils.filesystem import fileList

GALLERY_IMAGES = []

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def preBuild(site):
    global GALLERY_IMAGES
    
    for path in fileList(os.path.join(site.paths['static'], 'images/gallery')):
        #im = Image.open(path)
        parent_folder_name = os.path.basename(os.path.dirname(path))
        if parent_folder_name != 'thumbs':
            fname = os.path.basename(path)
            img_path = "/static/images/gallery/%s" % fname
            thumb_path = "/static/images/gallery/thumbs/%s" % fname
            GALLERY_IMAGES.append((img_path, thumb_path))
    print(GALLERY_IMAGES)

def preBuildPage(page, context, data):
    global GALLERY_IMAGES
    """
    Updates the context of the page to include: the page itself as {{ CURRENT_PAGE }}
    """

    # This will run for each page that Cactus renders.
    # Any changes you make to context will be passed to the template renderer for this page.

    extra = {
        "CURRENT_PAGE": page,
        'images': list(chunks(GALLERY_IMAGES, 4))
        # Add your own dynamic context elements here!
    }

    context.update(extra)
    return context, data
