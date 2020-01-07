#/bin/bash

qs='9 10'
js='7 8 9 10'
ks='0 1 2 3 4 5 6 7 8 9'
#qs='1'
dir_name='pollen-pca'
for k in $ks
do
	for q in $qs
	do

		for j in $js
		do
			echo $q
			outdir="/home/archithpc/alignment/batch-effect-nonlinear-3/matern/pca-lin/$k/$q/$j"
			python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 500 --save_freq 100 --batch $q --m12 True --k $k --j $j --pca_init True --lin_reg True
			outdir="/home/archithpc/alignment/batch-effect-nonlinear-3/matern/rand-lin/$k/$q/$j"
                        python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 500 --save_freq 100 --batch $q --m12 True --k $k --j $j --pca_init False --lin_reg True
			outdir="/home/archithpc/alignment/batch-effect-nonlinear-3/matern/gpy-gpy/$k/$q/$j"
                        python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 500 --save_freq 100 --batch $q --m12 True --k $k --j $j --gpy_init True --gpy_reg True
			outdir="/home/archithpc/alignment/batch-effect-nonlinear-3/matern/rang-gpy/$k/$q/$j"
                        python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 500 --save_freq 100 --batch $q --m12 True --k $k --j $j --gpy_reg True
			#outdir="/home/archithpc/alignment/batch-effect-nonlinear/matern/rand/simulate-$q/"
        		#python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 5000 --pca_init False --batch $q --m12 True --k $k --j $j
			#outdir="/home/archithpc/alignment/batch-effect-nonlinear/rbf/pca/simulate-$q/"
        		#python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 5000 --pca_init True --batch $q --k $k --j $j
        		#outdir="/home/archithpc/alignment/batch-effect-nonlinear/rbf/rand/simulate-$q/"
        		#python alignment-sim.py --out $outdir --Q 2 --M 500 --iter 5000 --pca_init False --batch $q --k $k --j $j
		done
	done

done
