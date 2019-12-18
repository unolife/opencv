import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

save_dir = '/Users/test/Desktop/opencv/sample_data/'

img_list = sorted(os.listdir(save_dir))

cnt = 0

for i in img_list:
    if i == '.DS_Store':
        pass
    else:
        img = plt.imread(os.path.join(save_dir, i))
        print(img.shape)
        divided = img/255
        reshaped = divided.reshape(divided.shape[0]*divided.shape[1], divided.shape[2])
        print('reshape_done')
        
        kmeans = KMeans(n_clusters=5+cnt, random_state=0).fit(reshaped)
        pic2show = kmeans.cluster_centers_[kmeans.labels_]

        cluster_pic = pic2show.reshape(img.shape[0], img.shape[1], img.shape[2])
        plt.imsave('{}segmented_{}'.format(save_dir,i), cluster_pic)
        print('{} ended'.format(i))
        cnt += 1