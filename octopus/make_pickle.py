import pickle
import glob
import numpy as np
import os
import sys

def loader(file_path):
    f = open(file_path, 'r')
    vertices = []
    for line in f.readlines():
        line = line.rstrip()
        line = line.split(' ')
        if line[0] == 'v':
            vertcd = []
            for i in range(1, len(line)):
                vertcd.append(line[i])
            vertcd = (np.array(vertcd)).astype('float32')
            vertices.append(vertcd)
    vertices = np.array(vertices)
    vertices = vertices.astype('float32')
    return vertices

file = 'data/sample/out/sample.obj'
lst = []
out_dict = {}
out_dict['width'] = 1080
out_dict['camera_c'] = [540.0, 540.0]
out_dict['camera_f'] = [1080, 1080]
out_dict['height'] = 1080
verts = loader(file)
lst.append(verts)
out_dict['vertices']  = np.asarray(lst)
pickle_out = open('data/sample/out/frame_data.pkl', 'wb')
pickle.dump(out_dict, pickle_out, protocol = 2)
pickle_out.close()
