#!/bin/python3 

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

template_dir, template_file = os.path.split(sys.argv[1])

env = Environment(
  loader=FileSystemLoader(template_dir),
  trim_blocks=True,
  lstrip_blocks=True)

final = env.get_template(template_file)

show = {
  'seasons': {
    's1': {
      'slug': 'korra_b1',
      'name': 'Air',
      'icon_path': 'empty',
      'episodes': {
        'e1': {
          'slug': 's01e01',
          'name': 'Welcome to Republic City',
          'video_filepath': 'videopath',
          'subititle_filepath': 'subpath'
        },
        'e2': {
          'slug': 's01e02',
          'name': 'I dunno',
          'video_filepath': 'videopath',
          'subititle_filepath': 'subpath'
        }
      }
    },

    's2': {
      'slug': 'korra_b2',
      'name': 'Spirits',
      'icon_path': 'empty',
      'episodes': {
        'e1': {
          'slug': 's02e01',
          'name': 'poopoo',
          'video_filepath': 'videopath',
          'subititle_filepath': 'subpath'
        },
        'e2': {
          'slug': 's02e02',
          'name': 'peepee',
          'video_filepath': 'videopath',
          'subititle_filepath': 'subpath'
        }
      }
    }
  }
}

print(show)

print(final.render(show))