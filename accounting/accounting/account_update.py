from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt

	
def balance_account(from_account,to_account,amount):
	#add total amount to asset account balance, decrease from credit_to account balance
	acc = frappe.get_doc("Account",from_account)
	acc.account_balance -= amount 		#amount credited
	acc.save()
	acc = frappe.get_doc("Account",to_account)
	acc.account_balance += amount  		#amount debited
	acc.save()

def balance_account_je(account,credit ,debit):
	acc = frappe.get_doc("Account",account)
	acc.account_balance -= flt(credit)		#amount credited
	acc.account_balance += flt(debit)		#amount debited
	acc.save()







