# SQL-PyForger
## Purpose
The purpose of this repo is to solve an issue I had wich was to forge a query from a really
long table output. I needed to modify quickly the value of a column, what is now easily
possible. 

for now, the only queries possible are :
- update
- insert

## Install
```
git clone git@github.com:glifth/SQL-PyForger.git
```
## File format
the file need to follow a specific format wich is :
```
1 table name
2 column name
3 column values
```
example :
```
table
| rowid | tms                 | ref         | entity | fk_soc | fk_projet | ref_ext | ref_int | ref_customer | date_creation |
|     1 | 2019-07-12 21:09:34 | SH2134-0001 |      1 |      1 |         0 |    NULL |    NULL |         NULL |             1 |
```
## Usage
The proper usage of this script is :
```
$ python3 forge.py -h
  Usage : python3 forge.py <option> <file>
  Options :
	  - insert
	  - update
```
