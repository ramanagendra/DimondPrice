# om setuptools import find_packages,setup
from typing import List
from setuptools import find_packages,setup

"""HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements"""

setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='sunny savita',
    author_email='sunny.savita@ineuron.ai',
    # stall_requires=["scikit-learn","pandas","numpy","-e ."],
    packages=find_packages()
)