import os
from solid import *
from solid.utils import *
import importlib

SEGMENTS = 48
openscad_exec = 'C:/Program Files/OpenSCAD/openscad.exe'

def load_model_and_name():
    model_module = importlib.import_module('model')
    if hasattr(model_module, 'assembly') and hasattr(model_module, 'model_name'):
        return model_module.assembly(), model_module.model_name
    else:
        raise AttributeError("The model file must have both 'assembly' and 'model_name' defined.")

def create_model_directory(model_name):
    directory = os.path.join(os.getcwd(), model_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def render_to_files(model, model_name):
    model_dir = create_model_directory(model_name)
    scad_file = os.path.join(model_dir, model_name + '.scad')
    scad_render_to_file(model, scad_file, file_header=f'$fn = {SEGMENTS};', include_orig_code=False)

if __name__ == '__main__':
    model, model_name = load_model_and_name()
    render_to_files(model, model_name)
    model_dir = create_model_directory(model_name)
    model_file = os.path.join(model_dir, model_name + '.py')
    with open(model_file, 'w') as f:
        f.write(open('model.py').read())