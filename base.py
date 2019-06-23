#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    https://pypi.org/project/sqlphile/
'''

# Import necessary modules
import sqlphile as sp


def startpy():

    rows = None
    
    with sp.sqlite3 ("test.db", dir = "./sqlmap") as db:
        rows = (db.file.get_all_cities
            .execute ().fetchall ())
    
    for row in rows:
        #print(type(row))
        print(row[0], row[1])


if __name__ == '__main__':
    startpy()