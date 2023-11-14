from setuptools import setup, find_packages

setup(
    name='tradeviewmalamas',
    version='0.1',
    description='Aplicacion de visualizacion de cotizacion de Bitcion y Ethereum',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[paquete.strip() for paquete in open('requirements.txt').readlines()]

)