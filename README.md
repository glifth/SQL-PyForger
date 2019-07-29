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
llx_commande
| rowid | ref         | entity | ref_ext | ref_int | ref_client | fk_soc | fk_projet | tms                 | date_creation       | date_valid          | date_cloture        | date_commande | fk_user_author | fk_user_modif | fk_user_valid | fk_user_cloture | source | fk_statut | amount_ht  | remise_percent | remise_absolue | remise | tva        | localtax1  | localtax2  | total_ht     | total_ttc    | note_private | note_public | model_pdf | last_main_doc                        | facture | fk_account | fk_currency | fk_cond_reglement | fk_mode_reglement | date_livraison | fk_shipping_method | fk_warehouse | fk_availability | fk_input_reason | fk_delivery_address | fk_incoterms | location_incoterms | import_key | extraparams | fk_multicurrency | multicurrency_code | multicurrency_tx | multicurrency_total_ht | multicurrency_total_tva | multicurrency_total_ttc |
|   5 | CO1907-0004 |      1 | NULL    | NULL    | NULL       |      1 |      NULL | 2019-07-23 02:55:47 | 2019-07-12 21:08:05 | 2019-07-12 21:08:53 | 2019-07-13 01:50:47 | 2019-07-12    |              1 |          NULL |             1 |               1 |   NULL |         1 | 0.00000000 |              0 |           NULL |      0 | 0.00000000 | 0.00000000 | 0.00000000 | 360.00000000 | 360.00000000 |              |             | einstein  | commande/CO1907-0001/CO1907-0001.pdf |       0 |       NULL | NULL        |                 1 |                 4 | 2019-07-19     |                  2 |         NULL |            NULL |            NULL |                NULL |            0 |                    | NULL       | NULL        |                0 | EUR                |       1.00000000 |           360.00000000 |              0.00000000 |            360.00000000 |

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
