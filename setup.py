
from setuptools import setup, find_packages
import versioneer

setup(
    name="q2-iqtree2",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Michael Robeson",
    author_email="soilbdelloid@gmail.com",
    description="IQ-TREE 2 functionality in QIIME 2.",
    license="BSD-3-Clause",
    url="https://github.com/mikerobeson/q2-iqtree",
    entry_points={
        'qiime2.plugins': ['q2-iqtree2=q2_iqtree2.plugin_setup:plugin']
    },
    package_data={
        'q2_iqtree2': ['citations.bib'],
        'q2_iqtree2.tests': ['data/*']
    },
    zip_safe=False,
)
