from logging import root
import os
import shutil
import argparse
import yaml
import pandas as pd
import numpy as np
import random
from get_data import get_data, read_params


def train_and_test(config_file):
    config = get_data(config_file)
    root_dir = config['raw_data']['data_src'] #to access main sorce of data...........['raw_data']['data_src'] this 2 terms are copied from params.yaml
    dest = config['load_data']['preproseesd_data'] # to save data
    p = config['load_data']['full_path'] #p=full path
    cla = config['load_data']['num_classes']  

    splitr = config['train']['split_ratio']

    for k in range(cla): # number of classes i.e 4
        per = len(os.listdir((os.path.join(root_dir, cla[k]))))
        print(k, "->", per)
        cnt = 0
        split_ratio = round((splitr/100)*per) #spliter is having my training data
        
        for j in os.listdir((os.path.join(root_dir,cla[k]))):
            pat = os.path.join(root_dir+'/'+cla[k])
            print(pat)
            if (cnt!=split_ratio):
                shutil.copy(pat, dest+'/'+'train'+'/'+'class_'+str(k)) #k will be having index
                cnt+=1
            else:
                shutil.copy(pat, dest+'/'+'test'+'/'+'class_'+str(k))
        
        print("Done")



# copied from create_folder.py as a main part

if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    passed_args=args.parse_args()
    train_and_test(config_file=passed_args.config)
