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

    with sp.sqlite3 (r"test.db") as db:
        
        q = (db.select ("CITY")
            .get ("NAME", "STATE")
            )

        for row in q.execute ().fetchall ():
            print(row)


if __name__ == '__main__':
    startpy()