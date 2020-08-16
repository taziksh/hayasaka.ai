## Delete failed/empty files
find /home/tazik/Nextcloud/Code/lbpcascade_animeface/examples/datasets/hand_tuned_larger_2x/ -size 0    -type f -delete

## Delete 'too small' files which is indicative of low quality:
find /home/tazik/Nextcloud/Code/lbpcascade_animeface/examples/datasets/hand_tuned_larger_2x/ -size -40k -type f -delete

## Delete exact duplicates:
fdupes --delete --omitfirst --noprompt /home/tazik/Nextcloud/Code/lbpcascade_animeface/examples/datasets/hand_tuned_larger_2x/

## Delete monochrome or minimally-colored images:
### the heuristic of <257 unique colors is imperfect but better than anything else I tried
deleteBW() { if [[ `identify -format "%k" "$@"` -lt 257 ]];
             then rm "$@"; fi; }
export -f deleteBW
find /home/tazik/Nextcloud/Code/lbpcascade_animeface/examples/datasets/hand_tuned_larger_2x -type f | parallel --progress deleteBW
