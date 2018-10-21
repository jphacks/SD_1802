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
import requests
import sqlite3

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

    print('before get bounding box')
    bb = align.getLargestFaceBoundingBox(rgbImg)
    if bb is None:
        raise Exception("Unable to find a face: {}".format(imgPath))
    if verbose:
        print("  + Face detection took {} seconds.".format(time.time() - start))

    print('after get bounding box')
    start = time.time()
    alignedFace = align.align(imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    print('after face alingment')
    
    if alignedFace is None:
        raise Exception("Unable to align image: {}".format(imgPath))
    if verbose:
        print("  + Face alignment took {} seconds.".format(time.time() - start))

        
    start = time.time()
    print('start to calc')
    print('net', net)
    rep = net.forward(alignedFace)
    print('rep: ', len(rep))
    if verbose:
        print("  + OpenFace forward pass took {} seconds.".format(time.time() - start))
        #print("Representation:")
        #print(rep)
        print("-----\n")

    print('finish to calc')
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

def Line(mes):
    TOKEN = "Tp7OqzzHAMtnGSY5KsFV4gcGd5Q4f3Z8nbvE4GVulb0"
    URL = "https://notify-api.line.me/api/notify" 

    message = "\n" + mes
    
    payload = {"message": message}
    headers = {"Authorization": "Bearer " + TOKEN}
    lineNotify = requests.post(URL, data=payload, headers=headers)

def get_user_info(user_id):
    """
    rails で登録されている database から user_id に紐づく user_infos
    
    user_id: user_infos の外部キーになっている user_id

    return: user_info の辞書
    """

    dbpath = '/home/ubuntu/Documents/SD_1802/products/db/development.sqlite3'
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()

    try:
        cursor.execute('SELECT * FROM user_infos WHERE user_id = {}'.format(user_id))
        res = cursor.fetchone()

    except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

    dic = {'name': res[1], 'memo': res[3]}
    return dic

    

    
def main(input_img_path):
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
    register_root_dir = '/home/ubuntu/Documents/SD_1802/products/public/uploads/JPHACKS'
    #input_img_path = '/var/www/html/upload/image.jpg'
    
    mini = np.inf
    candidate = ""
    
    for reg_img_path in get_all_images(register_root_dir):
        print('reg_img_path: ', reg_img_path)
        print('input_img_path: ', input_img_path)
        d = getDistance(reg_img_path, input_img_path, align, net, imgDim, verbose=verbose)
        if mini > d:
            mini = d
            candidate = reg_img_path
            
    print('candidate: ', candidate)
    print('score: ', mini)

    Line(os.path.basename(candidate))
    #Line(str(mini))

if __name__ == '__main__':
    info = get_user_info(1)
    msg = '名前: {} \n情報: {}'.format(info['name'], info['memo'])
    Line(msg)
    
    #while(1):
    #    time.sleep(10)
    #    input_img_path = '/var/www/html/upload/image.jpg'
    #    if os.path.exists(input_img_path):
    #        print('Found the image.jpg')
    #        main(input_img_path)
    #        os.remove(input_img_path)
    #    else:
    #        print('Not found the image.jpg in upload directory')
