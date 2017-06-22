hashcracker is a rainbow table using ES for faster access. 
It has precomputer sha1, md5 and sha256

=============================================================
## Components:

Collector - > ES (DB) -> resolver


collector:
--------------

creating hash of the passwords from `input.txt` and compute all hash and store in ES



resolver:
-------------

dumping all the found password from the input hash file and store in caracked file. 

================================================================

## Setup :

Install Elastic search and create the mapping from `config.py`

================================================================
## Usage :

- Always have to tweek the getPass/getHash funtions from main.py file from collector/resolver respectivley.
have to mention the seprators and index value after parsing the input.txt

- input.txt has to be changed by user everytime whenever you want to use this script.


### Collector: 
python main.py (run when you have to feed new password to ES)

### Resolver : 
python main.py (run when you have to crack the hash file, save it as the input.txt in resolver)

