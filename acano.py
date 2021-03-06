import xml.etree.ElementTree as ET
import requests

HOST = 'https://127.0.0.1/api/v1'
API_USER = 'user'
API_PASS = 'password'
SSL_VERIFY = True

def _get_many(api_path, tag_name):
    res = requests.get(HOST + api_path, auth=(API_USER, API_PASS), verify=SSL_VERIFY)
    root = ET.fromstring(res.text)
    many = []
    for child in root.iter(tag_name):
        one = { 'id': child.attrib['id'] }
        for e in child:
            one[e.tag] = e.text
        many.append(one)
    return many

def _get_one(api_path, tag_name):
    res = requests.get(HOST + api_path, auth=(API_USER, API_PASS), verify=SSL_VERIFY)
    root = ET.fromstring(res.text)
    one = {}
    for child in root.iter(tag_name):
        one['id'] = child.attrib['id']
        for e in child:
            one[e.tag] = e.text
    return one

def cospaces_get():
    return _get_many('/coSpaces', 'coSpace')

def cospace_get(filt):
    return _get_one('/coSpaces?filter=' + filt, 'coSpace')

def cospace_create(data):
    res = requests.post(HOST + '/coSpaces', data=data, auth=(API_USER, API_PASS), verify=SSL_VERIFY)
    return res

def cospace_delete(co):
    res = requests.delete(HOST + '/coSpaces/' + co['id'], auth=(API_USER, API_PASS), verify=SSL_VERIFY)
    return res

def accessmethod_create(co, data):
    res = requests.post(HOST + '/coSpaces/' + co['id'] + '/accessmethods', data=data, auth=(API_USER, API_PASS), verify=SSL_VERIFY)
    return res

def users_get():
    return _get_many('/users', 'user')

def user_get(_id):
    return _get_one('/users/' + _id, 'user')

def user_cospaces_get(_id):
    return _get_many('/users/' + _id + '/usercoSpaces', 'userCoSpace')
