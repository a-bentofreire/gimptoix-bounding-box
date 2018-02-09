#!/usr/bin/env python

# uuid: a2a8bd34-9d35-4648-9500-d6c62a2557c9

# @preserve Copyright (c) 2018 Alexandre Bento Freire. All rights reserved.
# @author Alexandre Bento Freire
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice, and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


from gimpfu import *


def bounding_box(timg):
    has_selection, x1, y1, x2, y2 = pdb.gimp_selection_bounds(timg)
    if has_selection:
        pdb.gimp_message(str(x2 - x1) + ',' + str(y2 - y1))
        pdb.gimp_image_select_rectangle(timg, 0, x1, y1, x2 - x1, y2 - y1)


register(
    "python_fu_bounding_box",
    "Bounding box",
    "Selects the Bounding box",
    "Alexandre Bento Freire",
    "Alexandre Bento Freire",
    "2018",
    "Bounding box",
    "",
    [
        (PF_IMAGE, "image", "Input image", None)
    ],
    [],
    bounding_box, menu="<Image>/Select")

main()
