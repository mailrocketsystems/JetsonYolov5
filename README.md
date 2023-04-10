Running YoloV5 with TensorRT Engine on Jetson.
==========

This repository contains step by step guide to build and convert YoloV5 model into a TensorRT engine on Jetson. This has been tested on Jetson Nano or Jetson Xavier 

Please install Jetpack OS version 4.6 as mentioned by Nvidia and follow below steps. Please follow each steps exactly mentioned in the video links below :

Jetson Nano: 

Jetson Xavier:

Install Libraries
=============
Please install below libraries::

    $ sudo apt-get update
	$ sudo apt-get install -y liblapack-dev libblas-dev gfortran libfreetype6-dev libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev
	$ sudo apt-get install -y python3-pip
	

Install below python packages
=============
Numpy comes pre installed with Jetpack, so make sure you uninstall it first and then confirm if it's uninstalled or not. Then install below packages:

    $ numpy==1.19.0
	$ pandas==0.22.0
	$ Pillow==8.4.0
	$ PyYAML==3.12
	$ scipy==1.5.4
	$ psutil
	$ tqdm==4.64.1
	$ imutils

Install PyCuda
=============
We need to first export few paths

	$ export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}
	$ export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH
	$ python3 -m pip install pycuda --user
	

Install Seaborn
=============

    $ sudo apt install python3-seaborn
	
Install torch & torchvision
=============

	$ wget https://nvidia.box.com/shared/static/fjtbno0vpo676a25cgvuqc1wty0fkkg6.whl -O torch-1.10.0-cp36-cp36m-linux_aarch64.whl
	$ pip3 install torch-1.10.0-cp36-cp36m-linux_aarch64.whl
	$ git clone --branch v0.11.1 https://github.com/pytorch/vision torchvision
	$ cd torchvision
	$ sudo python3 setup.py install 
	
### Not required but good library
sudo python3 -m pip install -U jetson-stats==3.1.4
