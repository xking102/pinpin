#!/usr/bin/python
# -*- coding: utf-8 -*-


def resizeImage(image_location, des_w, des_h, save_location):
    try:
        infile = image_location
        im = Image.open(image_location)
        src_w, src_h = im.size
        if src_w > src_h:
            ratio = des_h / src_h
            tmp_w = int(src_w * ratio)
            tmp_h = int(des_h)
            img = im.resize((tmp_w, tmp_h), Image.ANTIALIAS)
            a = int(tmp_w / 2)
            b = int(des_w / 2)
            x1 = a - b
            x2 = a + b
            box = [x1, 0, x2, des_h]
        else:
            ratio = des_w / src_w
            tmp_h = int(src_h * ratio)
            tmp_w = int(des_w)
            img = im.resize((tmp_w, tmp_h), Image.ANTIALIAS)
            a = int(tmp_h / 2)
            b = int(des_h / 2)
            y1 = a - b
            y2 = a + b
            box = [0, y1, des_w, y2]
        img.crop(box).save(save_location)
        return True
    except Exception, e:
        print e
        return False
