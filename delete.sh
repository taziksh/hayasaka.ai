find jpg/ -type f | xargs --max-procs=16 -n 9000 identify | \
    # remember the warning: images must be identical, square, and sRGB/grayscale:
    fgrep -v " JPEG 512x512 512x512+0+0 8-bit sRGB"| cut -d ' ' -f 1 | \
    xargs --max-procs=16 -n 10000 rm
