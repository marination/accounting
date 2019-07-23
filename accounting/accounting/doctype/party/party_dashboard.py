import frappe
from frappe import _

def get_data():
    return{
            'fieldname' : "party_name",
            'non_standard_fieldnames':{
                'Purchase Invoice': "supplier",
                'Sales Invoice' : "customer"
            },
            'transactions': [
                {
                    'label': 'Buying',
                    'items': ['Purchase Invoice']
                },
                {
                    'label': 'Selling',
                    'items': ['Sales Invoice']
                }
            ]
    }