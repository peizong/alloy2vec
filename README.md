### This toolkit is part of our work "Towards the design of ultra-high-entropy alloys enabled by mining 6.4 million texts", submitted, 2022, by Zongrui Pei, Junqi Yin, Peter K. Liaw and Dierk Raabe.

We acknowledge all the contributors whose existing work/toolkits make our work possible, particularly gensim and mat2vec. This new toolkit introduces the power of text mining to the high-entropy and ICME community. It provides a powerful and brand-new way to design multicomponent alloys with many components. We coin a new term, ultra-high entropy alloys, for this kind of alloy. This work is partly motivated by Cantor, who called for bolder actions to explore high-entropy alloys with more than five components. We show structural materials can benefit from mining the vast amount of publications.

### Set up
There are two methods to install alloy2vec. The first method is, to download this toolkit as a whole and follow the instruction below. This is similar to mat2vec, but with difference in details. There are lots of new files, and even files with the same names were modified, and thus are different from mat2vec.

The second one is to install mat2vec, and then (i) replace all existing files with the modified ones of alloy2vec; (ii) for data preprocessing and postprocessing that involves our new method, you have to put our files in the right directory. This is more complex than the first method.

### Instructions
1. Make sure the python version is `python3.6`; Or create an environment with the right version using `conda` or `pip`, like, `conda create --name py36 python=3.6` 
We recommend using [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
1. Navigate to the root folder of this repository (the same folder that contains this README file)
and run `pip install --ignore-installed -r requirements.txt`. Note: If you are using a conda env and any packages fail to compile during this step, you may need to first install those packages separately with `conda install package_name`. 
1. Wait for all the requirements to be downloaded and installed.
1. Run `python setup.py install` to install this module. This will also download the Word2vec model files.
If the download fails, manually download the [model](e.g., wget https://www.dropbox.com/s/tzl2zxzigbk2o9i/model_121520), 
[word embeddings](e.g., wget https://www.dropbox.com/s/tibgnb2higuzwca/model_121520.trainables.syn1neg.npy, and wget https://www.dropbox.com/s/8bz4h2dia7eop6h/model_121520.trainables.syn1.npy) and 
[output embeddings](e.g., wget https://www.dropbox.com/s/zj1uw4mlka6y2zx/model_121520.wv.vectors.npy) and put them in alloy2vec/training/models. This can be achieved simply by the following command:
```shell
bash download_data.sh
```
1. Finalize your chemdataextractor installation by executing ``cde data download`` (You may need to restart your virtual environment for the cde command line interface to be found).

#### Preparing data
Most of the corpora are downloaded using the Elsevier API, which is in json format. Then they were cleaned and tranformed into (i) plain text for skip-gram model, and (ii) tabulated word triples for knowledge graph model.

Since we design a model for alloys, all metallic-materials related corpora are placed double weight. More details are referred to the paper.

#### Processing

Example python usage:

```python
from alloy2vec.processing import MaterialsTextProcessor
text_processor = MaterialsTextProcessor()
text_processor.process("The Cantor alloy is CoCrFeNiMn.")
```
> (['the', 'cantor', 'alloy', 'is', 'CoCrFeMnNi', '.'], [('CoCrFeNiMn', 'CoCrFeMnNi')])

For the various methods and options see the docstrings in the code.

#### Pretrained Embeddings

Load and query for similar words and phrases:
```python
from gensim.models import Word2Vec
w2v_model = Word2Vec.load("alloy2vec/training/models/model_121520")
w2v_model.wv.most_similar("CoCrFeMnNi")
```
> w2v_model.wv.most_similar("CoCrFeMnNi",topn=10)
[('alloy_HEA', 0.8737579584121704), ('CoCrFeNi', 0.8341557383537292), ('equiatomic_CoCrFeMnNi', 0.8291258811950684), ('AlCoCrFeNi', 0.8107213973999023), ('equiatomic', 0.7687329053878784), ('HfNbTaTiZr', 0.7615582942962646), ('non-equiatomic', 0.7596109509468079), ('CoCrCuFeNi', 0.7591570019721985), ('entropy_alloys_HEAs', 0.7554466724395752), ('CoCrNi', 0.7503445148468018)]


Analogies:
```python
# magnesium is to Mg as ___ is to Fe? 
w2v_model.wv.most_similar(
    positive=["magnesium", "Fe"], 
    negative=["Mg"], topn=1)
```
> [('iron', 0.8962439298629761)]

Material formulae need to be normalized before analogies:
```python
# "CoCrFeNiMn" is not in the vocabulary (i.e., not normalized)
w2v_model.wv.most_similar("CoCrFeNiMn")
```
> KeyError: "word 'CoCrFeNiMn' not in vocabulary"
```python
from mat2vec.processing import MaterialsTextProcessor
text_processor = MaterialsTextProcessor()
w2v_model.wv.most_similar(text_processor.normalized_formula("CoCrFeNiMn"))
```
> [('alloy_HEA', 0.8737579584121704), ('CoCrFeNi', 0.8341557383537292), ('equiatomic_CoCrFeMnNi', 0.8291258811950684), ('AlCoCrFeNi', 0.8107213973999023), ('equiatomic', 0.7687329053878784), ('HfNbTaTiZr', 0.7615582942962646), ('non-equiatomic', 0.7596109509468079), ('CoCrCuFeNi', 0.7591570019721985), ('entropy_alloys_HEAs', 0.7554466724395752), ('CoCrNi', 0.7503445148468018)]

Keep in mind that words should also be processed before queries.
Most of the time this is as simple as lowercasing, however, it is the safest
to use the `process()` method of `mat2vec.processing.MaterialsTextProcessor`.

#### Training

To run an example training, navigate to *mat2vec/training/* and run

```shell
python phrase2vec.py --corpus=data/corpus_example --model_name=model_example
```

from the terminal. It should run an example training and save the files in *models*
and *tmp* folders. It should take a few seconds since the example corpus has only 5 abstracts.

For more options, run

```shell
python phrase2vec.py --help
```

### Postprocessing
To trend a new model, you can set parameters in postprocessing/contextSimilarity/parallel_version/alloyDesign-para.py

The important parameters include, the number of components for targeted high-entropy alloys, and the chemical elements to be considered in alloy design. Once these parameters are all set, submit the job to supercomputer, using the following command for slurm manager.

```shell
sbatch sub-text-mining.sh
```
We have performed high-throughput screening using 30 transition-metal elements, the results are stored in sys_sim6.csv for 6-component HEAs, and sys_sim7.csv for 7-component HEAs.

```python
import pandas as pd
data=pd.read_csv("postprocessing/contextSimilarity/parallel_version/sys_sim6.csv")
print(data)
```
>        Unnamed: 0                sys1           sys     sim
>0                0   Sc1Ti1V1Cr1Mn1Fe1   ScTiVCrMnFe  0.6377
>
>1                1   Sc1Ti1V1Cr1Mn1Co1   ScTiVCrMnCo  0.6232
>
>2                2   Sc1Ti1V1Cr1Mn1Ni1   ScTiVCrMnNi  0.6302
>
>3                3   Sc1Ti1V1Cr1Mn1Cu1   ScTiVCrMnCu  0.6262
>
>4                4   Sc1Ti1V1Cr1Mn1Zn1   ScTiVCrMnZn  0.6245
>
>...            ...                 ...           ...     ...
>
>593770      593770   W1Re1Os1Ir1Au1Hg1   WReOsIrAuHg  0.4081
>
>593771      593771   W1Re1Os1Pt1Au1Hg1   WReOsPtAuHg  0.4031
>
>593772      593772   W1Re1Ir1Pt1Au1Hg1   WReIrPtAuHg  0.4216
>
>593773      593773   W1Os1Ir1Pt1Au1Hg1   WOsIrPtAuHg  0.4615
>
>593774      593774  Re1Os1Ir1Pt1Au1Hg1  ReOsIrPtAuHg  0.4735

The last column is the averaged context similarity for HEAs, according the Eq. 1 (S).

### Related Work
Pei et al., Towards the design of ultra-high-entropy alloys enabled by mining 6.4 million texts, submitted, 2022.

### Issues?

When problems are found, users can report an issue on github or contact one of us directly. 
peizongrui@gmail.com,yinj@ornl.gov.

