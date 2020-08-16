read -p "Enter dir: " dir 
convertPNGToJPG() { convert -quality 100 "$@" "$@".jpg && rm "$@"; }
export -f convertPNGToJPG
find $dir -type f -name "*.png" | parallel --progress convertPNGToJPG
