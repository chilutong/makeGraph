import numpy as np
import pandas as pd

import os
root_dir='./mean_std/'
for dirpath, dirnames, filenames in os.walk('./5cv_result'):
    for filename in filenames:
        # print(os.path.join(dirpath, filename))
        print(filename)
        if filename=='.DS_Store':
            break
        datafile=os.path.join(dirpath, filename)
        print(dirpath.split('/')[-1:])
        # print(filename.split('.')[0])
        dataset=dirpath.split('/')[-1:][0]
        method = filename.split('.')[0]
        res_dir=root_dir+dataset+'/'+method
        result=[]
        data=pd.read_csv(datafile,header=None).values[0:5]
        mean=np.mean(data,axis=0)
        std=np.std(data,axis=0,ddof=1)
        result.append(mean)
        result.append(std)
        result=pd.DataFrame(result)
        result.to_csv(res_dir,sep=',',header=False,index=False)

        print(1)

