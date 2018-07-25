import re

def convert(CamelCase):
      string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', CamelCase)
      return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()
