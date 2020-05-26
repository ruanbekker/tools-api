#!/usr/bin/env python3

from flask import Flask, request, jsonify
from base64 import b64encode
import bcrypt
import binascii
import random
import os

app = Flask(__name__)

colors = ['blue', 'red', 'silver', 'green', 'yellow', 'orange', 'purple']
words = ['evil', 'hungry', 'goofy', 'adoring', 'tender', 'lekke', 'focused', 'trusting', 'jolly', 'insane', 'funny', 'agitated']
animals = ['tiger', 'lion', 'cheetah', 'fish', 'snake', 'dog', 'cat', 'bear', 'hamster']

def generate_name():
    response = "{color}-{word}-{animal}".format(
        color=random.choice(colors), 
        word=random.choice(words), 
        animal=random.choice(animals)
    )
    return response

def generate_string():
    return response

def generate_hex(n):
    nbytes = os.urandom(n)
    response = b64encode(nbytes)
    return response

def generate_base64(n):
    response = generate_hex(n)
    return response

def generate_hash(string_value):
    return bcrypt.hashpw(string_value.encode('utf-8'), bcrypt.gensalt())

def check_string_from_hash(string_value, hash_value):
    return bcrypt.checkpw(string_value.encode('utf-8'), hash_value.encode('utf-8'))

@app.route('/strings/name', methods=['GET'])
def gen_name():
    response = {}
    name = generate_name()
    response['name'] = name
    return jsonify(response)

@app.route('/strings/hex', methods=['GET'])
def gen_hex():
    response = {}
    hexval = generate_hex(random.randint(12,18))
    response['hex'] = hexval
    return jsonify(response)

@app.route('/strings/base64', methods=['GET'])
def gen_base64():
    response = {}
    base64val = generate_base64(random.choice([12,15,18,21,24,27]))
    response['base64'] = base64val
    return jsonify(response)

@app.route('/hash/create', methods=['POST'])
def gen_hash():
    response = {}
    data = request.get_json(force=True)
    print(data)
    try:
        string_value = data['string']
        hashval = generate_hash(string_value)
        print(hashval)
        response['hash'] = hashval
    except Exception as e:
        print(e)
        response['error'] = 'something bad happened'

    return jsonify(response)

@app.route('/hash/lookup', methods=['POST'])
def lookup_hash():
    response = {}
    data = request.get_json(force=True)
    try:
        string_value = data['string']
        hash_value = data['hash']
        lookup_string_val = check_string_from_hash(string_value, hash_value)
        response['string'] = lookup_string_val
    except:
        response['error'] = 'something bad happened'

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
