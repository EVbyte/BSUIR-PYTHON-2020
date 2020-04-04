from distutils.core import setup

setup(
    name='labs',
    version='1.0',
    package_dir={'labs': '../labs'},
    packages=['labs', 'labs.code', 'labs.code.Cashed', 'labs.code.ExternalMergeSort','labs.code.from_json','labs.code'
                                                                                                           '.SingleTone','labs.code.to_json','labs.code.vector' ],
    url='https://vk.com/hartrs',
    license='',
    author='Zinin E.V.',
    description='lab 2', requires=['numpy', 'numpy']
)