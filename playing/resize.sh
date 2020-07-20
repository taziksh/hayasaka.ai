find png/ -type f | xargs --max-procs=16 -n 9000 \
    mogrify -resize 512x512\> -extent 512x512\> -gravity center -background black
