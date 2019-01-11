from setuptools import setup


requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(name='PyLog',
      author='Mat Frayne',
      url='https://github.com/Mat-Frayne/PythonDebugger',
      version="0.0.1",
      packages=['PyLog'],
      license='MIT',
      description='Im Learning',
      long_description=readme,
      include_package_data=True,
      install_requires=requirements,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)