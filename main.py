#!/usr/bin/python3

import sqlite3
import json

try:
    from flask import Flask
except ImportError:
    raise ImportError('Please install Flask')

database = "cma-artworks.db"

def create_dict_from_sql(cursor, row):
    dict = {}
    for id, column in enumerate(cursor.description):
        dict[column[0]] = row[id]
    return dict

connection = sqlite3.connect(database)
connection.row_factory = create_dict_from_sql
cursor = connection.cursor()

query ='''
    SELECT DISTINCT artwork.accession_number AS id, artwork.title as artwork_title, GROUP_CONCAT(IFNULL(creator.role, "") || " " || IFNULL(creator.description, ""), "|") AS attribution, department.name AS department_name, artwork.tombstone FROM artwork
    LEFT OUTER JOIN artwork__department ON artwork.id = artwork__department.artwork_id
    LEFT OUTER JOIN department ON department_id = department.id
    LEFT OUTER JOIN artwork__creator ON artwork.id = artwork__creator.artwork_id
    LEFT OUTER JOIN creator ON artwork__creator.creator_id = creator.id
    GROUP BY artwork.accession_number
'''

cursor.execute(query)
result = cursor.fetchall()
connection.close()

# save json to file
with open('static/output.json', 'w') as outfile:
    json.dump(result, outfile)

# start web server
app = Flask(__name__, static_url_path='')
@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
