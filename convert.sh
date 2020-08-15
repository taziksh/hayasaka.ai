convertPNGToJPG() { convert -quality 100 "$@" "$@".jpg && rm "$@"; }
export -f convertPNGToJPG
find jpg/ -type f -name "*.png" | parallel --progress convertPNGToJPG
