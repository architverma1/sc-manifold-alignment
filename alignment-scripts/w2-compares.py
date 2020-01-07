import numpy as np
import pandas as pd
import ot
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from scipy.spatial.distance import pdist, squareform
from sklearn.preprocessing import normalize
from joblib import Parallel, delayed
import multiprocessing
import h5py

folder = 'batch-effect-nonlinear-3'
latent_true = np.load('/home/archithpc/data/batch-effect-variable-genes-3/latent_true.npy')

dist_true = squareform(pdist(latent_true))
dist_norm = normalize(dist_true, norm = 'l1')
M = dist_true

N1 = 300
N2 = 200
batch_var = np.concatenate((np.zeros((N1,1)),np.ones((N2,1))),axis = 0)

#w2z = np.zeros((10,2,10,10,500))
#w2p = np.zeros((2,10,10,10,500))
#w2s = np.zeros((2,10,10,10,500))
#w2m = np.zeros((2,10,10,10,500))
#w2b = np.zeros((10,10,10,500))
init = 'rang-gpy'
iters = '100'
def w2(k):
    print(k)
    w2p = np.zeros((2,10,10,500))
    #w2b = np.zeros((10,10,500))
    for j in range(1,11):
        print('   j: ' + str(j))
        for i in range(1,11):
	    #Y = np.load('/home/archithpc/data/batch-variable-genes-3/sim-cluster-' + str(j) + '-' + str(i) + '.npy')[k,j-1,i-1]
	    Y = np.loadtxt('/home/archithpc/data/batch-effect-variable-genes-3/' + str(k) + '/sim-cluster-' + str(j) + '-' + str(i) + '.csv')
	    dist_obs = squareform(pdist(Y))
	    dist_obs_norm = normalize(dist_obs, norm = 'l1')

	    #path = './'+ folder + '/matern/' + init + '/'  + str(k) + '/' + str(j) + '/' + str(i) + '/model-output-' + iters + '.hdf5'
	    #fit = h5py.File(path, 'r')
	    #zfit = fit['x_mean']

	    #dist_z = squareform(pdist(zfit))
	    #dist_z_norm = normalize(dist_z, norm = 'l1')

	    ols = LinearRegression(fit_intercept = False)
	    ols.fit(batch_var, Y)
	    Yres = Y - ols.predict(batch_var)
	    pca = PCA(n_components = 2)
	    zpca = pca.fit_transform(Yres)

	    dist_pca = squareform(pdist(zpca))
	    dist_pca_norm = normalize(dist_pca, norm = 'l1')

	    #seurat = pd.read_csv('./'+folder+'/results/seurat-results/sim-' + str(i) + '.csv')
	    #dist_seurat = squareform(pdist(seurat.values))
	    #dist_s_norm = normalize(dist_seurat, norm = 'l1')

	    #mnn = pd.read_csv('./'+folder+'/results/mnn-results/' + str(k) + '/sim-' + str(j) + '-' + str(i) + '.csv')
	    #dist_m = squareform(pdist(mnn.values))
	    #dist_m_norm = normalize(dist_m, norm = 'l1')

	    for n in range(0,500):
		#w2z[0,j-1,i-1,n] = ot.emd2(dist_z_norm[j,:],dist_norm[j,:],M)
		#w2z[1,j-1,i-1,n] = ot.emd2(dist_z_norm[j,:],dist_obs_norm[j,:],M)

		w2p[0,j-1,i-1,n] = ot.emd2(dist_pca_norm[j,:],dist_norm[j,:],M)
		w2p[1,j-1,i-1,n] = ot.emd2(dist_pca_norm[j,:],dist_obs_norm[j,:],M)

		#w2s[0,k,j-1,i-1,n] = ot.emd2(dist_s_norm[j,:],dist_norm[j,:],M)
		#w2s[1,k,j-1,i-1,n] = ot.emd2(dist_s_norm[j,:],dist_obs_norm[j,:],M)

		#w2m[0,j-1,i-1,n] = ot.emd2(dist_m_norm[j,:],dist_norm[j,:],M)
		#w2m[1,j-1,i-1,n] = ot.emd2(dist_m_norm[j,:],dist_obs_norm[j,:],M)
	
		#w2b[j-1,i-1,n] = ot.emd2(dist_norm[j,:],dist_obs_norm[j,:],M)
    return w2p

num_cores = multiprocessing.cpu_count()
w2p = Parallel(n_jobs=num_cores)(delayed(w2)(i) for i in range(0,10))
#np.save('./w2-distance/' + init + iters, w2)

np.save('./w2-distance/pca-q2', w2p)
#np.save('./w2-distance/mnn', w2m)
#np.save('./w2-distance/batch', w2b)
