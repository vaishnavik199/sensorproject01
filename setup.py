from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'



def get_requirements(file_path:str)->List[str]:
    reqirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return reqirements






setup(
    name='Fault detection',
    version='0.0.1',
    author='vaishnavi',
    author_email='kshirsagarvaishnavi199@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)