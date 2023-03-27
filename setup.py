from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_reqirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] 
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
        return requirements

setup(
   name = 'mlproject' ,
   version = '0.0.1',
   author='Marko',
   author_email='marko.krajinovic1994@gmail.com',
   packages = find_packages(),
   install_requires = get_reqirements('requirements.txt')
)