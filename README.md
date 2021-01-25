# Algs4's Union-Find

Python implementation of Union-Find in _Princeton's Algorithms: [1.5 - Case Study: Union-Find]_,
with test cases downloaded from [the website] embedded.

### Usage
```bash
python run.py command data-file
```

#### Commands:

- `simple` - Quick-Find Union-Find
- `quick-union` - Quick-Union Union-Find
- `weighted` - Weighted quick-Union Union-Find

#### Data Files:

Located in `test-data` directory.

- `tinyUF.txt` - Contains the 11 connections used in the example on [the website]
- `mediumUF.txt` - Contains 900 connections
- `largeUF.txt` - Contains about 2 millions of connections


#### Example:

```bash
python run.py weighted "test-data/largeUF.txt"
```
to execute the Weighted Quick-Union Union-Find with the largest data file. 


### Requirements
- Python 3.5+
- [tqdm](https://tqdm.github.io/)


[the website]: https://algs4.cs.princeton.edu/15uf/
[1.5 - Case Study: Union-Find]: https://algs4.cs.princeton.edu/15uf/


### License
All Python code in this project are provided under _BSD 3-Clause "New" or "Revised" License_.
