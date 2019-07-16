# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from accounting.accounting.account_update import balance_account

class PaymentEntry(Document):
	def on_submit(self):
		balance_account(self.pay_from,self.pay_to,self.amount)
		self.make_gl_entry(self.pay_from,self.pay_to)

	def on_cancel(self):
		balance_account(self.pay_to,self.pay_from,self.amount)
		self.make_gl_entry(self.pay_to,self.pay_from)

	def make_gl_entry(self,pay_from,pay_to):
		generalLedger =[{
		"doctype":"General Ledger",
		'ge_date' : self.date,
		'ge_account': pay_from,
		'debit_amount': 0.0,
		'credit_amount': self.amount,
		'ge_account_balance': frappe.db.get_value('Account',pay_from,'account_balance') ,
		'ge_party': self.party,
		'transaction_type': 'Payment Entry',
		'transaction_no':self.name,
		'ge_against_account':pay_to
		},
		{
		"doctype":"General Ledger",
		'ge_date' : self.date,
		'ge_account': pay_to,
		'debit_amount': self.amount,
		'credit_amount': 0.0,
		'ge_account_balance':frappe.db.get_value('Account',pay_to,'account_balance'),
		'ge_party': self.party,
		'transaction_type': 'Payment Entry',
		'transaction_no':self.name,
		'ge_against_account': pay_from
		}]
		for row in generalLedger:
			doc = frappe.get_doc(row)
			doc.insert()
