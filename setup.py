from setuptools import setup 

setup(
    name='Scylla',

    version='1.0',
    description='Information Gathering Engine (OSINT)',
    url='https://github.com/josh0xA/Scylla',
    
    author = 'Josh (josh0xA, overflowin) Schiavone',
    author_email='josh@profify.ca',
    license='MIT',

    install_requires = ['termcolor','requests','urllib3', 'urllib', 'pythonwhois', 
    'BeautifulSoup4', 'google', 're', 'json', 'contextlib']
    console =['scylla.py'],
)