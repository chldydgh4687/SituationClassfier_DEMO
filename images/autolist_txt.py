from os.path import *
import glob
import os

def autolist():
    
    f = open(os.getcwd()+'/images/data_list.txt','w')
    folder=basename('/SituationClassfier_DEMO/images')
    print(basename('./SituationClassfier_DEMO/images'))
    for i in glob.iglob('*.jpg'):
        print("1")
        data = folder + "/" + i + "\n"
        f.write(data)
    f.close()

    
