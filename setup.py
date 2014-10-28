from distutils.core import setup
setup(
name = 'minickt',
packages = ['minickt', 'cktParser', 'cktWriter'],
scripts = ['minic'],
install_requires=['matplotlib','networkx'],
version = '.8.3',
description = 'Analyzer and simulator of logic circuit',
author = 'dokelung',
author_email = 'dokelung@gmail.com',
url = 'https://github.com/dokelung/minickt',
download_url = 'https://github.com/dokelung/minickt/tarball/0.8.3',
keywords = ['circuit','eda','verification','logic','gate'],
classifiers = [],
)
