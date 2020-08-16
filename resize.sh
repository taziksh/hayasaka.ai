find ~/Nextcloud/Code/lbpcascade_animeface/examples/datasets/hand_tuned_larger_2x -name *.jpg | xargs --max-procs=16 -n 9000 \
    mogrify -resize 512X512\> -extent 512X512\> -gravity center -background black
