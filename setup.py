from setuptools import setup 

setup(
	name='SimpliPyTEM',
	version='1.0.4',
	description='A python package to simplify the processing and analysis of TEM and in situ TEM images and videos',
	long_description='SimpliPyTEM is a python package to make python-based analysis of Transmission electron microscopy images easier and more approachable. Although TEM is the focus, this could also easily be adapted to other microscopy images. Importantly, SimpliPyTEM is designed to make automated, basic work accessible for beginners (through a simple GUI), while more complicated methods can be accessed through simple python code. This package centers around the image data being held in a Numpy array which makes the image data easy to access for further analysis.\nThis project aims to make use of the rapid automation of image analysis methods available through python while making it approachable for the user.\nFunctions to generate pdf and html files containing images and videos are also included in this package. This allows easy viewing and sharing of all the images/videos taken in an imaging session, making experiment evaluation significantly easier.',
	url='https://github/gabriel-ing/Micrograph-analysis-scripts',
	author='Gabriel Ing',
	author_email='ucbtgrb@ucl.ac.uk',
	license = 'BSD 2-clause',
	packages =['SimpliPyTEM'],
	install_requires=['numpy',
	 'ncempy==1.9.0',
	 'Pillow',
	 'mrcfile',
	 'moviepy',
	 'airium',
	 'matplotlib',
	 'opencv-python',
	 'tifffile',
	 'notebook',
	 'scikit-image',
	 'imutils',
	 'fpdf',
	 'PyQt5'],
	classifiers=[
		'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',     
        'Programming Language :: Python :: 3',
		'Topic :: Scientific/Engineering :: Image Processing'],


)
