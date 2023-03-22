cd gnuplots
cases=("neat_emimtfsi" "acn_emimtfsi" "acn_litfsi" "wat_litfsi")

for case in ${cases[@]}; do
  echo $case
  ct=$( echo $case | sed 's/_/-/' )
  fn=gn-"$case"_charge.gnu
  cp template_charge.gnu $fn
  for v in {0..3}; do
    sed -i 's/V'"$v"'LIST/'"$(grep "$case $v" ../dict.txt | awk 'BEGIN {i=0} {a[i++]=$1} END {print a[0],a[1],a[2],a[3]}')"'/' $fn
  done
  sed -i -e 's/CASETITLE/'"$ct"'/' -e 's/CASE/'"$case"'/' $fn
  gnuplot $fn
done

cd ..
montage -density 300 -tile 2x2 -geometry +0+0 -border 0 gnuplots/*.png charge-graphs.png
