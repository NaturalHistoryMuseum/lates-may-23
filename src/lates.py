# !/usr/bin/env python
# encoding: utf-8

from jinja2 import Environment, PackageLoader, select_autoescape
import os
import shutil


env = Environment(
    loader=PackageLoader('lates'),
    autoescape=select_autoescape()
)

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

input_dir = os.path.dirname(__file__)

output_dir = os.path.join(base_dir, 'docs')


def copy_content(input_content_dir, output_content_dir, replace=True):
    if os.path.exists(input_content_dir):
        input_content = os.listdir(input_content_dir)
    else:
        input_content = []
    if not os.path.exists(output_content_dir):
        os.mkdir(output_content_dir)
    output_content = os.listdir(output_content_dir)
    for item in input_content:
        if item not in output_content or replace:
            shutil.copy(os.path.join(input_content_dir, item), os.path.join(output_content_dir, item))
    for item in output_content:
        if item not in input_content:
            os.remove(os.path.join(output_content_dir, item))


def get_images():
    input_images_dir = os.path.join(base_dir, 'images')
    output_images_dir = os.path.join(output_dir, 'images')
    copy_content(input_images_dir, output_images_dir)
    return os.listdir(output_images_dir)


def get_styles():
    input_styles_dir = os.path.join(input_dir, 'styles')
    output_styles_dir = os.path.join(output_dir, 'styles')
    copy_content(input_styles_dir, output_styles_dir)
    return os.listdir(output_styles_dir)


def render_page():
    images = get_images()
    styles = get_styles()
    template = env.get_template('index.html')
    template.stream(images=images, styles=styles).dump(os.path.join(output_dir, 'index.html'))


render_page()
