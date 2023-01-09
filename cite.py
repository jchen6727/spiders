import re
"""
parse citation for author, title, journal, date
"""

mla = 'Borges, Fernando S., et al. "Large-scale biophysically detailed model of somatosensory thalamocortical circuits in NetPyNE." bioRxiv (2022).'
apa = 'Borges, F. S., Moreira, J. V., Takarabe, L. M., Lytton, W. W., & Dura-Bernal, S. (2022). Large-scale biophysically detailed model of somatosensory thalamocortical circuits in NetPyNE. bioRxiv.'
chi = 'Borges, Fernando S., Joao VS Moreira, Lavinia M. Takarabe, William W. Lytton, and Salvador Dura-Bernal. "Large-scale biophysically detailed model of somatosensory thalamocortical circuits in NetPyNE." bioRxiv (2022).'
har = 'Borges, F.S., Moreira, J.V., Takarabe, L.M., Lytton, W.W. and Dura-Bernal, S., 2022. Large-scale biophysically detailed model of somatosensory thalamocortical circuits in NetPyNE. bioRxiv.'
van = 'Borges FS, Moreira JV, Takarabe LM, Lytton WW, Dura-Bernal S. Large-scale biophysically detailed model of somatosensory thalamocortical circuits in NetPyNE. bioRxiv. 2022 Jan 1.'

rgx = {
    'mla' : r'(?P<authors>.*)"(?P<title>.*)"(?P<journal>.*)\((?P<date>.*)\)',
    'apa' : r'(?P<authors>.*)\((?P<date>.*)\).(?P<journal>.*)\.(?P<journal>.*)',
    'chi' : r'(?P<authors>.*)"(?P<title>.*)"(?P<journal>.*)\((?P<date>.*)\)',
    'har' : r'(?P<authors>.*)(?P<date>\d*)"',
    'van' : r'(?P<authors>.*)',
}

