#!/usr/bin/env python3

from PIL import Image
import random
import sys


def warp_sort(line):
    line.sort()


def warp_shuffle(line):
    random.shuffle(line)


def fuzz_single_img(img, fn):
    print('    Reading …')
    width, height = img.size
    data = list(img.getdata())
    cols = [data[col::width] for col in range(width)]
    print('    Columns …')
    [fn(col) and None for col in cols]
    rows = [list(row) for row in zip(*cols)]
    del cols
    print('    Rows …')
    [fn(row) and None for row in rows]
    print('    Reassemble …')
    #data = sum(rows, [])
    data = [px for row in rows for px in row]
    del rows
    img.putdata(data)


def run(argv):
    if len(argv) < 2 or argv[1].startswith('-'):
        print('USAGE: {} <INPUT_FILENAME>…'.format(argv[0]), file=sys.stderr)
        exit(1)
    for filename in argv[1:]:
        for mode_fn, mode_name in ((warp_sort, 'sorted'), (warp_shuffle, 'shuffled')):
            print('For {} ({});'.format(filename, mode_name))
            img = Image.open(filename)
            fuzz_single_img(img, mode_fn)
            print('    Write out …')
            img.save(filename + '_' + mode_name + '.png')
    print('Done!')
        

if __name__ == '__main__':
    run(sys.argv)
