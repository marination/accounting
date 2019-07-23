# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from accounting.accounting.account_update import balance_account_je

class InadequateEntriesError(frappe.ValidationError): pass

class DebitCreditError(frappe.ValidationError): pass

class JournalEntry(Document):
	def validate(self):
		for i in self.get("transaction"):
			if i.debit>0 and i.credit>0:
				frappe.throw(_("Cannot debit and credit from the same account at once"),DebitCreditError)

		if len(self.get("transaction"))	<=1 :
			frappe.throw(_("Need minimum two entries"),InadequateEntriesError)

		if self.difference < 0:
			frappe.throw(_("Total debit must be equal to total credit. The difference is {}".format(self.difference)))

	def on_submit(self):
		transaction
		for i in self.get("transaction"):
			balance_account_je(i.account,i.credit,i.debit)
			self.make_gl_entry(i.account,i.credit,i.debit,i.party)

	def on_cancel(self):
		for i in self.get("transaction"):
			if i.debit == 0.0 :
				balance_account_je(i.account,'0.0',i.credit)
				self.make_gl_entry(i.account,'0.0',i.credit,i.party)
			elif i.credit == 0.0 :
				balance_account_je(i.account,i.debit,'0.0')
				self.make_gl_entry(i.account,i.debit,'0.0',i.party)

	def make_gl_entry(self,account,credit,debit,party):
		generalLedger = ({
			"doctype":"General Ledger",
			'ge_date' : self.date,
			'ge_account': account,
			'debit_amount': debit,
			'credit_amount': credit,
			'ge_account_balance': frappe.db.get_value('Account',account,'account_balance'),
			'ge_party': party,
			'transaction_type': 'Journal Entry',
			'transaction_no':self.name,
			'ge_against_account': party
		})
		doc = frappe.get_doc(generalLedger)
		doc.insert()
	