from setuptools import setup


setup(
    name='ocrme',
    version='0.0.3',
    url="https://github.com/aniversarioperu/googlescholar_scrapper",
    author="AniversarioPeru",
    author_email="aniversarioperu1@gmail.com",
    maintainer="AniversarioPeru",
    maintainer_email="aniversarioperu1@gmail.com",
    contact="AniversarioPeru",
    contact_email="aniversarioperu1@gmail.com",
    license="GPL v3",
    description="do ocr for a PDF file",
    long_description=open('README.md').read(),
    platforms="any",
    download_url="",
    classifiers=[
        "Programming Language :: Python",
        ("Topic :: Scientific/Engineering :: Bio-Informatics"),
        ("Intended Audience :: Science/Research"),
        ("License :: OSI Approved :: GNU General Public License v3 (GPLv3)"),
        ("Operating System :: OS Independent"),
        ("Environment :: Console"),
    ],
    install_requires=[],
    packages=['ocrme'],
)

