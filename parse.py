import xml.etree.ElementTree as ET
import cv2
from PIL import Image
import glob


def _traverse_tree(root, tmp):
    if root.getchildren():
        for child in root:
            #print "traversing child"
            _traverse_tree(child, tmp)
    else:
        print root.attrib
        val = root.attrib['bounds']
        tmp.append(val)
    return tmp

def parse_xml(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    k = []
    _traverse_tree(root, k) 
    return k

def split_image(image_name, coordinates):
    prefix = image_name.replace('.png', '')
    im = Image.open(image_name)
    cnt=1
    for item in coordinates:
        tmp = ""
        item = item.replace("][", ",")
        for i in item:
            if i.isdigit() or i == ',':
                tmp = tmp+i
        print tmp
        tmp =  tmp.split(',')
        tmp = [float(i) for i in tmp]
        if tmp[2] - tmp[0] == 0 or tmp[3] - tmp[1] == 0:
            print "Invalidate parameter"
            continue
        icon = im.crop((tmp[0], tmp[1], tmp[2], tmp[3]))
        icon.save(prefix + '_' + str(cnt) + '.png')  # generating all the parts
        cnt = cnt+1


# Parsing all the xml files and cropping corresponding images accordingly
xmlfiles = (glob.glob("*.xml"))
for xfile in xmlfiles:
    print xfile
    coords = parse_xml(xfile)
    split_image(xfile.replace('.xml', '') + '.png', coords)

