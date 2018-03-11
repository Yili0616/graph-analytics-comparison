# Graph Analytic Libraries Comparison 

## Overview
This is code repo for testing 3 different graph analytic libraries: iGraph(R),NetworkX(python)
and SNAP(C++)

Following functions are tested: 

**Random Graph Generators**: 
1) Erdos-Renyi
2) Watts–Strogatz small-world graph 
3) Preferential Attachment

**Save/Load Time** for 4 different datasets. All of them are from [SNAP](http://snap.stanford.edu/data/index.html) website 
1) [Wikitalk](https://snap.stanford.edu/data/wiki-Talk.html)
2) [US Patent](https://snap.stanford.edu/data/cit-Patents.html)
3) [Pokec Social Network](https://snap.stanford.edu/data/soc-pokec.html)
4) [LiveJournal Social Network](https://snap.stanford.edu/data/soc-LiveJournal1.html)

**Graph Analytics**: 
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

Step 1: Open Rstudio

Step 2: File > Open File > Migrate to iGraph/er.r

Step 3: Click run

**2. SNAP ** 

**3. NetworkX** 

Step 1: Migrate to Net
