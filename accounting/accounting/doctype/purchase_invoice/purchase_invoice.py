# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from accounting.accounting.account_update import balance_account


class PurchaseInvoice(Document):

	def validate(self):

		#check if quantity is not negative or zero 
		for i in self.get("items"):
			if i.quantity <= 0:
				frappe.throw(_("Quantity cannot be zero or negative. Please enter a valid quantity"))

			if i.rate <= 0 :
				frappe.throw(_("Rate cannot be zero or negative. Please enter a valid rate "))

		#check if due date is lesser purchase date
		if self.duedate < self.date:
			frappe.throw(_("Due Date cannot be before Posting Date. Please enter a valid Due Date"))

		#check if there's enough funds in Creditors account
		from_acc_balance = frappe.db.get_value('Account',self.credit_to,'account_balance')
		if from_acc_balance < self.total_amount:
			frappe.throw(_("Insufficient funds in Credit account"))

	def on_submit(self):
			balance_account(self.credit_to,self.asset_account,self.total_amount)
			self.make_gl_entry(self.credit_to,self.asset_account)
			
	def on_cancel(self):
			balance_account(self.asset_account,self.credit_to,self.total_amount)
			self.make_gl_entry(self.asset_account,self.credit_to)

	def make_gl_entry(self,from_account,to_account): 
		gl_entry =[{
			"doctype":"General Ledger",
			'ge_date' : self.date,
			'ge_account': from_account,
			'debit_amount': 0.0,
			'credit_amount': self.total_amount,
			'ge_account_balance': frappe.db.get_value('Account',from_account,'account_balance') ,
			'ge_party': 'Supplier',
			'ge_party_name':self.supplier_name,
			'transaction_type': 'Purchase Invoice',
			'transaction_no':self.name,
			'ge_against_account': to_account
		},
		{
			"doctype":"General Ledger",
			'ge_date' : self.date,
			'ge_account': to_account,
			'debit_amount': self.total_amount,
			'credit_amount': 0.0,
			'ge_account_balance':frappe.db.get_value('Account',to_account,'account_balance'),
			'ge_party': 'Supplier',
			'ge_party_name':self.supplier_name,
			'transaction_type': 'Purchase Invoice',
			'transaction_no':self.name,
			'ge_against_account': self.dri
		}]
		for row in gl_entry:
			doc = frappe.get_doc(row)
			doc.insert()

	