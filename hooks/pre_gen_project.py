import re
import sys

PLUGIN_REGEX = r'^[a-zA-Z][ a-zA-Z0-9]+$'

plugin_name = '{{ cookiecutter.plugin_name }}'

if not re.match(PLUGIN_REGEX, plugin_name):
    print('ERROR: {}'.format(plugin_name),
          'Plugin name should starts by a letter',
          'And containts only letters, numbers or spaces')

    # exits with status 1 to indicate failure
    sys.exit(1)
