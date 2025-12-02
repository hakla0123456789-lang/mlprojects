from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str)->List[str]:
    ''' 
    These fumction will be returing the list of the requirements...
    '''
    E_DOT="-e ."
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if  E_DOT in requirements:
            requirements.remove(E_DOT)

        return requirements

setup(
    name="mlproject",
    version="1.0",
    author="Sahil",
    author_email="hakla0123456789@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
)