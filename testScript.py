import os
import torch
import numpy as np
import cv2
from HourGlass3D import *

all_frames = os.listdir('../train_frames/train2')
n_frames = len(all_frames)
frames_seq = np.zeros((1, 24, n_frames, 256, 256))
for idx, frame in enumerate(all_frames):
	frames_seq[0,0:2,idx,:,:] = cv2.imread('../train_frames/train2/'+ frame).transpose(2,0,1)

for i in range(21):
	frames_seq[0,3*i:3*i+2,:,:,:] = frames_seq[0,0:2,:,:,:]

frames_seq = torch.from_numpy(frames_seq).float() /256
frames_var = torch.autograd.Variable(frames_seq).float().cuda()

hg = Hourglass3D(63).cuda()

hg(frames_var)


"""
Can Improve it!!
"""