convertPNGToJPG() { convert -quality 33 "$@" "$@".jpg && rm "$@"; }
export -f convertPNGToJPG
find png/ -type f -name "*.png" | parallel --progress convertPNGToJPG
