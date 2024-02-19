import glob
from distutils.core import setup

# get all of the scripts
scripts = glob.glob('bin/*')

setup(
  name='docx2txtextended',
  packages=['docx2txtextended'],
  version='0.9.1',
  description='A pure python-based utility to extract text and images '
              'from docx files, extended for math formulas and styles.',
  author='J Taglione',
  author_email='',
  url='https://github.com/JonathanTaglioneCS/python-docx2txtextended',
  download_url='',
  keywords=['python', 'docx', 'text', 'images', 'extract'],
  scripts=scripts,
  classifiers=[],
)
