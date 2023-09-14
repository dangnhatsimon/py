#!/usr/bin/en python3
import argparse
import csv
import sqlite3
import sys

def process_options():
    arg_parser = argparse.ArgumentParser(
        description='Update products CSV into the specified database'
    )
    arg_parser.add_argument('--server', default='products')
    arg_parser.add_argument('filename', default='products.csv')
    args=arg_parser.parse_args()
    return args

def database_connection(name):
    db=sqlite3.connect(f'{name}.db', isolation_level='DEFERRED')
    cursor=db.cursor()
    #Check if the table is already present
    cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name='products'
    ''')
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE products (product_code, description)
        ''')
    return db

def update_data(database, options):
    with open(options.filename, 'r', encoding='utf-8-sig') as products:
        reader=csv.DictReader(products)
        cursor=database.cursor()
        for row in reader:
            print('Updating {} with value: {}'.format(row('product_code'), row['description']))
            cursor.execute('''
                
            ''')
