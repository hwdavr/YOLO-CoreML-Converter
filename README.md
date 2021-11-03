# YOLOv4-CoreML-Converter

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

A conversion tool to convert Tensorflow model (weights file) to CoreML model via Keras and coremltools. Inspired by [MPieter](https://github.com/MPieter/YOLOv4-CoreML-Converter).

- Support both YOLOv4 and YOLOv4 Tiny models
- Support to export Keras h5 format model also. 

---

## Quick Start

```
python convert.py yolov4.cfg yolov4.weights model_data/yolov4.mlmodel --keras_output_path model_data/yolov4.h5
```

To also export the intermediate Keras model use the argument `--keras_output_path`.

## Tested with

    - Python 3.x.x
    - Keras 2.2.4
    - tensorflow 2.x.0
    - coremltools 5.0
