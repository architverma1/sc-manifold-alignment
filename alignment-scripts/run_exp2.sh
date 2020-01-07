#/bin/bash

js='1 2 3 4 5'
for j in $js
	do
		echo $j
		outdir="/home/archithpc/alignment/batch-effect-noise/matern/pca-lin/$j"
		python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 1000 --save_freq 250 --batch 0 --m12 True --k 0 --j $j --pca_init True --lin_reg True
		outdir="/home/archithpc/alignment/batch-effect-noise/matern/rand-lin/$j"
                python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 1000 --save_freq 250 --batch 0 --m12 True --k 0 --j $j --pca_init False --lin_reg True
done
