from os import listdir, getcwd
from os.path import isfile, join, dirname, abspath
import random

ACTUAL = getcwd()
BASE_DIR = join(ACTUAL, 'images')

files = sorted([f for f in listdir(BASE_DIR) if isfile(join(BASE_DIR, f)) if f.endswith('.jpg')])
grupos = [files[i:i+3] for i in range(0, len(files), 3)]
html = ''

for tercia in grupos:
    for elemento in tercia:
        if elemento is tercia[0]:
            html += f'<div class="columns">\n'
        if elemento in grupos[0]:
            html += f'\t<div class="column">\n\t\t<figure class="image is-3by5">\n\t\t\t<img src="images/{elemento}">\n\t\t</figure>\n\t</div>\n'
        else:
            html += f'\t<div class="column">\n\t\t<figure class="image is-3by5">\n\t\t\t<img class="lazyload" data-src="images/{elemento}" loading="lazy">\n\t\t</figure>\n\t</div>\n'
        if elemento is tercia[-1]:  
            html += '</div>\n'

with open(join(ACTUAL, 'listacontodo.html'), 'w') as archivo:
    archivo.write(html)
