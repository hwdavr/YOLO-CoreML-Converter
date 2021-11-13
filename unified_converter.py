import coremltools
import argparse
from tensorflow.keras.models import load_model

parser = argparse.ArgumentParser(
    description='Darknet h5 fiel To CoreML Converter.')
parser.add_argument('input_path', help='Path to Keras h5 file.')
parser.add_argument('output_path', help='Path to output CoreML model file.')
parser.add_argument(
    '-t',
    '--tiny',
    help='Is input keras h5 a tiny model.',
    action='store_true')

def _main(args):
    model = load_model(args.input_path, compile=False)

    coreml_model = coremltools.convert(model, inputs=[coremltools.ImageType(scale=1 / 255.0)])

    print("Input description", coreml_model.input_description)
    ## Modify the input description based on input model
    coreml_model.input_description['input_1'] = 'Input image'
    print("Output description", coreml_model.output_description)
    ## Modify the out description based on input model
    coreml_model.output_description['Identity'] = 'The 13x13 grid (Scale1)'
    coreml_model.output_description['Identity_1'] = 'The 26x26 grid (Scale2)'
    if (args.tiny == False):
        coreml_model.output_description['Identity_2'] = 'The 52x52 grid (Scale3)'

    coreml_model.author = 'Weidian Huang'
    coreml_model.license = 'Public Domain'
    coreml_model.short_description = "An YOLO CoreML converter"

    coreml_model.save(args.output_path)

if __name__ == '__main__':
    _main(parser.parse_args())