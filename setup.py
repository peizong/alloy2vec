import math
import logging
import os
import requests
import wget

from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install

from tqdm import tqdm
import urllib.parse

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s",
                    level=logging.INFO)


class Word2vecModelDownload(install):
    """Downloads Word2vec models after installation if not already present."""

    _MODELS_URL = 'https://www.dropbox.com/s/'
    _MODELS_URL2=['tzl2zxzigbk2o9i/model_121520',
        'zj1uw4mlka6y2zx/model_121520.wv.vectors.npy',
        'tibgnb2higuzwca/model_121520.trainables.syn1neg.npy']
    _MODEL_FILES = [
        'model_121520',
        'model_121520.wv.vectors.npy',
        'model_121520.trainables.syn1neg.npy',
    ]
    _DOWNLOAD_LOCATION = 'alloy2vec/training/models'

    def run(self):
        for URL2,model_file in zip(self._MODELS_URL2,self._MODEL_FILES):
            file_url = urllib.parse.urljoin(self._MODELS_URL, URL2)
            final_location = os.path.join(self._DOWNLOAD_LOCATION, model_file)
            r = requests.get(file_url, stream=True)
            #r = wget.download(file_url)
            os.system("wget "+file_url)
            if not os.path.exists(self._DOWNLOAD_LOCATION)
               os.makedirs(self._DOWNLOAD_LOCATION)
            os.system("mv "+model_file+" "+self._DOWNLOAD_LOCATION)
            total_size = int(r.headers.get('content-length', 0))
            if self._file_exists_correct_size(model_file, total_size):
                logging.info("{} already present, skipping download.".format(model_file))
                continue  # If the file is already there, skip downloading it.

            logging.info('Starting download for {}'.format(model_file))
            block_size, wrote = 1024, 0
            with open(final_location, 'wb') as downloaded_file:
                for data in tqdm(r.iter_content(block_size),
                                 total=math.ceil(total_size // block_size),
                                 unit='KB',
                                 unit_scale=True):
                    wrote = wrote + len(data)
                    downloaded_file.write(data)
            if total_size != 0 and wrote != total_size:
                logging.ERROR(
                    "Something went wrong during the download "
                    "of {}, the size of the file is not correct. "
                    "Please retry.".format(model_file))
            else:
                logging.info("{} successfully downloaded.".format(model_file))
        install.run(self)
        os.system("wget "+https://www.dropbox.com/s/g196rrf56nthrt4/sys_sim6.csv)
        os.system("mv sys_sim6.csv alloy2vec/postprocessing/contextSimilarity/parallel_version/")
        
    def _file_exists_correct_size(self, filename, expected_size):
        """Checks if the file exists in the download location and has the correct size.

        Args:
            filename: The name of the file in the download location.
            expected_size: The expected size in bytes.

        Returns:
            True if the file exists and has the expected size, False otherwise.
        """
        full_file_path = os.path.join(self._DOWNLOAD_LOCATION, filename)
        if (not os.path.exists(full_file_path) or
                os.path.getsize(full_file_path) != expected_size):
            return False
        return True


with open('README.md', encoding="utf-8") as f:
    readme = f.read()

setup(
    name='alloy2vec',
    version='0.0',
    description='alloy2vec training and text processing code for Pei et al. XXX (2022).',
    long_description=readme,
    author='Pei et al. XXX (2022)',
    author_email='peizongrui@gmail.com, yinj@ornl.gov',
    packages=find_packages(),
    cmdclass={
        'install': Word2vecModelDownload,
    },
    include_package_data=True,
)
