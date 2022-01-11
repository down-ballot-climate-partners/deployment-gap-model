from setuptools import setup, find_packages

setup(
    name='dbcp',
    version='0.1.0',
    url='https://github.com/catalyst-cooperative/down_ballot_climate.git',
    author='Catalyst Cooperative',
    author_email='hello@catalyst.coop',
    description='Data engineering for the Down Ballot Climate Project (DBCP)',
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=['catalystcoop.pudl>=0.5', 'psycopg2', 'tqdm', 'python-docx',],
)