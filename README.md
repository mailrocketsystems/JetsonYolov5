Running YoloV5 with TensorRT Engine on Jetson.
==========

This repository contains step by step guide to build and convert YoloV5 model into a TensorRT engine on Jetson. This has been tested on Jetson Nano or Jetson Xavier 

Please install Jetpack OS version 4.6 as mentioned by Nvidia and follow below steps:

Install Libraries:
=============
Please install below libraries::

    $ sudo apt-get update
	$ sudo apt-get install -y liblapack-dev libblas-dev gfortran libfreetype6-dev libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev
	$ sudo apt-get install -y python3-pip
