# Graph Analytics Libraries Comparison 

## Overview
This is code repo for testing 3 different graph analytic libraries: [iGraph](http://igraph.org/redirect.html) (R), [NetworkX](https://networkx.github.io/) (Python)
and [SNAP](http://snap.stanford.edu/) (C++)

Both real and synthetic datasets are used. 

**Real datasets**( All of them are from [SNAP](http://snap.stanford.edu/data/index.html) website ):
1) [wiki-Talk](https://snap.stanford.edu/data/wiki-Talk.html)
2) [cit-Patents](https://snap.stanford.edu/data/cit-Patents.html)
3) [soc-Pokec](https://snap.stanford.edu/data/soc-pokec.html)
4) [soc-LiveJournal1](https://snap.stanford.edu/data/soc-LiveJournal1.html)

**Synthetic Datasets** 
Erdős–Rényi, Watts-Strogatz Small-World and Preferential Attachment are used to generate synthetic datasets.

**Erdős–Rényi**:

Number of Nodes| Number of Edges 
| ----| -----
| 1M  | 10M          
| 1M  | 100M           
| 10M | 100M   

**Watts-Strogatz Small-World**:

Number of Nodes|Number of Neighbors|Rewiring Probability 
|----|----| ----
|100k| 200 |0.5
|1M| 200 | 0.5

**Albert-Barabasi Preferential Attachment**: 

Number of Nodes| Number of Edges Created by Each New Node
----|----
1M|10

Compare the runtime of following algorithms using above real datasets: 
1) Page Rank
2) Weakly-Connected Component(WCC)
3) 3-cores
4) Clustering Coefficient
5) Edge Existence

## Installation and Setup
Clone/ Donwload all files from this repo.

**1. iGraph**

Step 1: Download [R](https://www.r-project.org/)

Step 2: Download [RStudio](https://www.rstudio.com/)


**2. SNAP**

Step 1: Download [Snap](https://snap.stanford.edu/snap/download.html) examples

Step 2: Download Ubuntu Desktop/Cygwin on windows or alternatives on Mac OS X or use command prompt on Linux

Step 3: Copy code in Snap folder to Snap-4.0/examples/graphgen


**3. NetworkX** 

Step 1: Download [Python 2.7](https://www.python.org/downloads/) 

Step 2: 
```
pip install networkx
```

## Examples

To generate Erdos-Renyi graph:

**1. iGraph** 

Step 1: Open RStudio

Step 2: File > Open File > Migrate to iGraph/er.r

Step 3: Click run

**2. SNAP** 

Step 1: Copy Snap folder to Snap-4.0/examples folder

Step 2: Change the Main value to graphgen

Step 3: Type make on command prompt under Snap-4.0 directory

Step 4: Run

```
./graphgen -g:e -n:1000000 -m:10000000 -o:er.txt
```
under Snap-4.0/examples/graphgen directory 

**3. NetworkX** 

Step 1: Migrate to networkx/er.py

Step 2: Run 
```
python er.py
```


*graphgen.cpp from Snap folder are copied from original Snap code*
