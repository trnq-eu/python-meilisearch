import meilisearch
import json
from dotenv import load_dotenv
import os

load_dotenv()

meilikey = os.environ.get('meilikey')

client = meilisearch.Client('http://localhost:7700', meilikey)

json_file = open('data/movies.json', encoding='utf-8')
movies = json.load(json_file)
client.index('movies').add_documents(movies)

