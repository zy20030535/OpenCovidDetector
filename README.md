# OpenCovidDetector: Open source algorithm for detecting COVID-19 on Chest CT


OpenCovidDetector is a opensource covid-19 diagnosis system implementing on pytorch, which is also 
as presented in our paper: Development and Evaluation of an AI System for COVID-19 Diagnosis
 (https://www.medrxiv.org/content/10.1101/2020.03.20.20039834v2)
 
 If you find this project helpful, please cite our paper:
```
@article {OpenCovidDetector,
	author = {Jin, Cheng and Chen, Weixiang and Cao, Yukun and Xu, Zhanwei and Zhang, Xin and Deng, Lei and Zheng, Chuansheng and Zhou, Jie and Shi, Heshui and Feng, Jianjiang},
	title = {Development and Evaluation of an AI System for COVID-19 Diagnosis},
	year = {2020}, doi = {10.1101/2020.03.20.20039834},journal = {medRxiv}}
```

About the Project
------
Early detection of COVID-19 based on chest CT will enable timely treatment of patients and help control the spread of the disease. With rapid spreading of COVID-19 in many countries, however, CT volumes of suspicious patients are increasing at a speed much faster than the availability of human experts. Here, we propose an artificial intelligence (AI) system for fast COVID-19 diagnosis with an accuracy comparable to experienced radiologists.

<img src="https://github.com/ChenWWWeixiang/diagnosis_covid19/blob/master/pic/workflow.png" width =80% height = 80% div align = center />

Performance
----------
 A large dataset was constructed by collecting 970 CT volumes of 496 patients with confirmed COVID-19 and 260 negative cases from three hospitals in Wuhan, China, and 1,125 negative cases from two publicly available chest CT datasets. Trained using only 312 cases, our diagnosis system, which is based on deep convolutional neural network, is able to achieve an accuracy of 94.98%, an area under the receiver operating characteristic curve (AUC) of 97.91%, a sensitivity of 94.06%, and a specificity of 95.47% on an independent external verification dataset of 1,263 cases. In a reader study involving five radiologists, only one radiologist is slightly more accurate than the AI system.
 
 <img src="https://github.com/ChenWWWeixiang/diagnosis_covid19/blob/master/pic/roc_reader.png" width =50% height = 50% div align = center />
 
 Visualization 
----------
 <img src="https://github.com/ChenWWWeixiang/diagnosis_covid19/blob/master/pic/19_1-30_115_1.00.jpg" width =60% height = 60% div align = center />

  <img src="https://github.com/ChenWWWeixiang/diagnosis_covid19/blob/master/pic/9_1-31_95_1.00.jpg" width =60% height = 60% div align = center />
  
  <img src="https://github.com/ChenWWWeixiang/diagnosis_covid19/blob/master/pic/20_2-7_195_1.00.jpg" width =60% height = 60% div align = center />
  
Guidance to Use
-------
###  Environment

Ubuntu==16.04
python==3.6.1
matplotlib==3.1.2
six==1.13.0
torch==1.3.1
scikit_image==0.16.2
imageio==2.6.1
scipy==1.3.3
numpy==1.15.3
opencv_python==4.1.1.26
pandas==0.23.4
torchvision==0.4.2
Pillow==7.0.0
pydicom==1.4.2
pyradiomics
scikit_learn==0.22.2.post1
seaborn==0.10.0
SimpleITK==1.2.4
skimage
toml==0.10.0
xlrd==1.2.0

### Use Trained Model for Inference
1. __Data Preparation__ : A demo covid-19 data can be made at <https://cloud.tsinghua.edu.cn/f/365e7f81e4b443eb9fab/?dl=1>. When using your own data, make sure keeping the same format and naming scheme as our demo data)

2. __Download Trained Weight__: a trained model is available at <https://cloud.tsinghua.edu.cn/f/ba180ea9b2d44fdc9757/?dl=1>

3. __Test__:  
```
python testengine.py -p <path to trainedmodel> -m <list of paths for lung segmentation> -i <list of paths for image data> -o <path to save record> -g <gpuid>
``` 
### Train on Your Own Data

1. __Data Preparation__ : The datasets from Wuhan Union Hospital, Western Campus of Wuhan Union Hospital, and Jianghan Mobile Cabin Hospital were used under the license of the current study and are not publicly available. Applications for access to the LIDC-IDRI database can be made at <https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI>. ILD-HUG database can be accessed at <http://medgift.hevs.ch/wordpress/databases/ild-database/>. 

2. __Volumes to Images__: We suggest that test data should be in ".nii" format (any formats that *SimpleITK* can work on is OK with small changes in codes) and training data should be in ".jpg" format (any formats that *opencv-python* can work on is OK with small changes in codes). A script "data/test_hu.py" is used to cut volumes into images. 

3. __Lung Segmentation__ : using Deeplabv1 (https://github.com/DrSleep/tensorflow-deeplab-resnet)
 or any other segmentation methods.
 
4. __Split Dataset__: 
```
python data/get_set_seperate_jpg.py -p <list of paths to jpgs for seperate> -t <train list output path> -v <validation list output path>
```

5. __Begin Training__: training parameters are listed on _options_lip.toml_```python main.py ```

### More Research Tools
* __Model Visualization__:
A script to show Grad-CAM/CAM result is available. Input images should be in jpg formats and should be concatenated with lung mask as Red channel:
```
python models/gradcam.py --image_path <raw jpg img path> --mask_path <jpg img with mask path> --model_path <path to trained model> --output_path <path to output>
```
   You can also use our volume cam script, which demands   raw data volumes and lung segmentation volumes as inputs.
```
python models/grad_volume.py --image_path <raw data nii path> --mask_path <lung mask nii file path> --model_path <path to trained model> --output_path <path to output>
```

* __Fractal Dimension Features__ (TODO):

    in fractal-dimension/


* __Radiomics__ (TODO):
python get_r_features.py

* __LASSO Analysis__ (TODO):
python plot_lasso_mse.py

* __Abnormal Locating__ (TODO):

