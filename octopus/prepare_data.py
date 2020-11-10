import os, cv2
import numpy as np

def make_folders():
    os.system('mkdir -p data/sample/frames')
    for i, img_name in enumerate(sorted(os.listdir('images'))):
        im = cv2.imread('images/' + img_name)
        if im.shape[0] < im.shape[1]:
            im = np.pad(im, (((im.shape[1]-im.shape[0])//2, (im.shape[1]-im.shape[0])//2), (0,0), (0,0)), mode = 'constant', constant_values=0)
        elif im.shape[0] > im.shape[1]:
            im = np.pad(im, ((0,0), ((im.shape[0]-im.shape[1])//2, (im.shape[0]-im.shape[1])//2), (0,0)), mode = 'constant', constant_values=0)
        im = cv2.resize(im, (1080,1080))
        cv2.imwrite('data/sample/frames/' + '000' + str(i) + '.png', im)

make_folders()
