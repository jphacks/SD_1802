# -*- coding:utf-8 -*-
#!/usr/bin/env python2
#
# Example to compare the faces in two images.
# Brandon Amos
# 2015/09/29
#
# Copyright 2015-2016 Carnegie Mellon University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

start = time.time()

import argparse
import cv2
import itertools
import os
import re

import numpy as np
np.set_printoptions(precision=2)

import openface

parser = argparse.ArgumentParser()

parser.add_argument('--verbose', action='store_true')

def getRep(imgPath, align, net, imgDim, verbose=False):
    """
    入力された画像の認証スコアを算出する

    imgPath: 画像の path
    align: dlib の顔検出器
    net: 認証スコアを計算する facenet
    imgDim: 画像の次元 default=96 なんでこれに従う
    verbose: ログを出力するかどうか

    returns: 認証スコア
    """
    if verbose:
        print("Processing {}.".format(imgPath))
        
    bgrImg = cv2.imread(imgPath)
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
    
    print("  + Original size: {}".format(rgbImg.shape))

    start = time.time()
    bb = align.getLargestFaceBoundingBox(rgbImg)
    if bb is None:
        raise Exception("Unable to find a face: {}".format(imgPath))
    if verbose:
        print("  + Face detection took {} seconds.".format(time.time() - start))
    
    start = time.time()
    alignedFace = align.align(imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    cv2.imshow('aligned', alignedFace)
    cv2.waitKey(0)
    if alignedFace is None:
        raise Exception("Unable to align image: {}".format(imgPath))
    if verbose:
        print("  + Face alignment took {} seconds.".format(time.time() - start))

        
    start = time.time()
    rep = net.forward(alignedFace)
    if verbose:
        print("  + OpenFace forward pass took {} seconds.".format(time.time() - start))
        #print("Representation:")
        #print(rep)
        print("-----\n")
    return rep

def getDistance(reg_img_path, input_img_path, align, net, imgDim, verbose=False):
    """
    登録画像と入力画像との間の顔認証スコアを計算し、距離を出す
    reg_img_path: 登録画像の path
    input_img_path: 入力画像の path
    align: dlib の顔検出器
    net: 認証スコアを計算する facenet
    verbose: ログを出力するかどうか

    returns: 画像間のスコアから計算した距離(L2 norm)
    """
    reg_rep = getRep(reg_img_path, align, net, imgDim, verbose=verbose)
    input_rep = getRep(input_img_path, align, net, imgDim, verbose=verbose)

    dis = np.linalg.norm(reg_rep - input_rep)
    
    return dis

def get_all_images(root_dir):
    """
    ディレクトリを再帰的に探って画像ファイルを抽出
    """
    
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if re.search(r'.jpg', f) or re.search(r'.png', f):
                yield os.path.join(root, f)

def main():
    # general setting
    args = parser.parse_args()
    dlib_path = '/home/ubuntu/Documents/SD_1802/products/python/shape_predictor_68_face_landmarks.dat'
    facenet_model_path = '/home/ubuntu/Documents/SD_1802/products/python/nn4.small2.v1.t7'
    imgDim = 96
    verbose = args.verbose
    
    start = time.time()
    align = openface.AlignDlib(dlib_path)
    net = openface.TorchNeuralNet(facenet_model_path, imgDim)
    if verbose:
        print("Loading the dlib and OpenFace models took {} seconds.".format(
            time.time() - start))
    # get register images & input image
    register_root_dir = '/home/ubuntu/Documents/SD_1802/products/public/uploads/'
    input_img_path = '/home/ubuntu/Documents/SD_1802/products/python/image/input_image.jpg'
    for reg_img_path in get_all_images(register_root_dir):
        d = getDistance(reg_img_path, input_img_path, align, net, imgDim, verbose=verbose)
        print(d)
        
        

if __name__ == '__main__':
    main()

