from behave import given, when, then
from grappa import should
import requests
import json

@given('I have a store')
def set_way(context):
    context.url = 'https://fakestoreapi.com/products'

@when('add a product')
def post_products(context):
    context.headers = {'content-type': 'application/json'}
    context.body = {
        'title': 'iphone 12 64GB',
        'price': 5000.5,
        'description': 'Iphone 12 64GB cor preto',
        'image': 'https: //i.pravatar.cc',
        'category': 'celulares'
    }
    context.request_data = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)

    global response_data
    response_data = context.request_data.json()

@then('I check that the product has been added')
def validate_products(context):
    assert context.request_data.status_code == 200
    response_data | should.have.key('title') > should.be.equal.to('iphone 12 64GB')
    response_data | should.have.key('price') > should.be.equal.to(5000.5)
    response_data | should.have.key('description') > should.be.equal.to('Iphone 12 64GB cor preto')
    response_data | should.have.key('image') > should.be.equal.to('https: //i.pravatar.cc')
    response_data | should.have.key('category') > should.be.equal.to('celulares')
    response_data | should.have.key('id')

@when('I get all the products')
def get_products(context):
    context.data = requests.get(context.url)

    global response
    response = context.data.json()

@then('I check and validate all products')
def validate_list(context):
    assert context.data.status_code == 200
    price = None

    for key in response:
        if 'SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s' in key['title']:
            price = key['price']
    
    price | should.be.equal.to(109)
    response | should.have.length.of(20)
