set term pngcairo size 640,480 enhanced
set output 'plot-CASE-charge.png'

set style data lines

dt = 2e-6 # timestep in ns

v0list = "V0LIST"
v1list = "V1LIST"
v2list = "V2LIST"
v3list = "V3LIST"

ncol = 3 # column to load

set title 'Charge traces (CASETITLE)'

set xlabel 't (ns)'
set ylabel 'Q (q_e)'

set key left top invert reverse

plot for [i=1:words(v0list)] '../../workspace/'.word(v0list,i).'/log.2' u ($1*dt):(-column(ncol)) every ::50 lc 1 t (i==1? '0V' : ''), \
 for [i=1:words(v1list)] '../../workspace/'.word(v1list,i).'/log.2' u ($1*dt):(-column(ncol)) every ::50 lc 2 t (i==1? '1V' : ''), \
 for [i=1:words(v2list)] '../../workspace/'.word(v2list,i).'/log.2' u ($1*dt):(-column(ncol)) every ::50 lc 3 t (i==1? '2V' : ''), \
 for [i=1:words(v3list)] '../../workspace/'.word(v3list,i).'/log.2' u ($1*dt):(-column(ncol)) every ::50 lc 4 t (i==1? '3V' : ''), \
 0 dt 2 lc black t ''
