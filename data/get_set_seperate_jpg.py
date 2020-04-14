import os,random,glob
import argparse
parser = argparse.ArgumentParser()
parser.description='please enter two parameters a and b ...'
parser.add_argument("-p", "--path", help="A list of paths to jpgs for seperate",
                    type=str,
                    default=['/mnt/data7/resampled_jpgs/masked_train1',
      '/mnt/data7/resampled_jpgs/masked_train2',
      '/mnt/data7/resampled_jpgs/masked_train_lidc',
      '/mnt/data7/resampled_jpgs/masked_train3',
      '/mnt/data7/resampled_jpgs/masked_ild',
                             '/mnt/data7/resampled_jpgs/masked_CAP'])
parser.add_argument("-t", "--train_txt",
                    help="train list output path",
                    type=str,                    
                    default='txt/train5cls1000.txt')
parser.add_argument("-v", "--val_txt",
                    help="validation list output path",
                    type=str,
                    default='txt/test5cls1000.txt')

args = parser.parse_args()
if isinstance(args.path,str):
    path=eval(args.path)
else:
    path=args.path
#path=['/mnt/data7/slice_test_seg/jpgs2']
f1 = open(args.train_txt, 'w')
f2 = open(args.val_txt, 'w')

train_count=1000
c=0
for ipath in path:
    cnt = 0
    files=os.listdir(ipath)
    names_id=[file.split('_')[0].split('c--')[-1] for file in files]
    names_id=list(set(names_id))
    random.shuffle(names_id)
    train=names_id[:-len(names_id)//4]
    #val=names_id[len(names_id)//2:-len(names_id)//4]
    test=names_id[-len(names_id)//4:]
    for _,i in enumerate(train):
        if cnt >= train_count:
            break
        names=glob.glob(ipath+'/'+i+'_*')
        for name in names:
            if cnt>=train_count:
                break
            cnt+=1
            c+=1
            f1.writelines(name+'\n')
        names=glob.glob(ipath+'/c--'+i+'_*')
        for name in names:
            if cnt>=train_count:
                break
            cnt+=1
            c+=1
            f1.writelines(name+'\n')
#print(c)
    for i in test:
        names=glob.glob(ipath+'/'+i+'_*')
        for name in names:
            f2.writelines(name+'\n')
        names=glob.glob(ipath+'/c--'+i+'_*')
        for name in names:
            f2.writelines(name+'\n')