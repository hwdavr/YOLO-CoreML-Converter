# YOLO-CoreML-Converter

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

A conversion tool to convert Tensorflow model (weights file) to CoreML model via Keras and coremltools. Inspired by [MPieter](https://github.com/MPieter/YOLOv4-CoreML-Converter).

- Support both YOLOv3, Tiny YOLOv3, YOLOv4 and Tiny YOLOv4(not tested) models
- Support to export Keras h5 format model 

---

## Quick Start

```
python convert.py cfg/yolov4.cfg yolov4.weights model_data/yolov4.mlmodel --keras_output_path model_data/yolov4.h5
```

To also export the intermediate Keras model use the argument `--keras_output_path`.

## Tested with

    - Python 3.x.x
    - Keras 2.2.4
    - tensorflow 2.3.0
    - coremltools 5.0
    
## Pretrained Models
- YOLOv3: https://pjreddie.com/media/files/yolov3.weights
- Tiny YOLOv3: https://pjreddie.com/media/files/yolov3-tiny.weights
- YOLOv4: https://drive.google.com/open?id=1bV4RyU_-PNB78G-OtoTmw1Q7t_q90GKY
If above link cannot work, please go to (YOLOv4-model-zoo)[https://github.com/AlexeyAB/darknet/wiki/YOLOv4-model-zoo] and download YOLOv4-Mish-416 or YOLOv4-Leaky-416 weights file.

