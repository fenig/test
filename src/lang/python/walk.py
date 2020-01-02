#!/usr/bin/env python3
from __future__ import unicode_literals, print_function, absolute_import

import time
import json
import sys
import os
import os.path
import convert
# import msgpack

def is_translatable(f):
    return f.endswith('.py')

def walk(indir, outdir):
    num_translated = 0
    try:
        os.remove(outdir)
    except:
        pass
    for root, _, files in os.walk(indir):
        outpath = os.path.join(outdir, root.strip(os.path.commonprefix([root, indir])))
        try:
            os.makedirs(outpath) #, exist_ok=True)
        except:
            pass
        for fn in files:
            if is_translatable(fn):
                translation = convert.translate(os.path.join(root, fn))
                td = translation.to_dict()
                # Turns out JSON is makes the translation about twice as slow as msgpack
                with open(os.path.join(outpath, fn + '.json'), 'w') as outf:
                    json.dump(td, outf, indent=2)
                # with open(os.path.join(outpath, fn + '.mpk'), 'wb') as outf:
                #     msgpack.pack(td, outf)
                num_translated += 1
    return num_translated

if __name__ == '__main__':
    if len(sys.argv) > 2:
        indir = sys.argv[1]
        outdir = sys.argv[2]
    else:
        indir = '/Users/michael/src/noam/lang/python/'
        outdir = '/Users/michael/src/noam/lang/python/trans'
    print('walking...',end=' ')
    start = time.time()
    count = walk(indir, outdir)
    end = time.time()
    print('done.')
    print('Translated {} files in {:.2f} seconds.'.format(count, end - start))
