# Goal: To Create the application as a package

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] # to replace new line by blank

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup (
    name='StudentPerformance',
    version="0.0.1",
    author="Vikram",
    author_email="datadude.ml@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
