# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _, _dict
from frappe.utils import getdate,cstr,flt

def execute(filters=None):
	if not filters:
		return [], []
	account_details = {}
	for acc in frappe.db.sql("""select name, is_group from tabAccount""", as_dict=1):
		 account_details.setdefault(acc.name, acc)
	validate_filters(filters,account_details)
	columns = fetch_columns(filters)
	result = get_results(filters,account_details)
	return columns,result

def validate_filters(filters,account_details):
	if filters.get("ge_account") and not account_details.get(filters.account):
		frappe.throw(_("Account {0} does not exists").format(filters.account))

	if filters.from_date > filters.to_date :
		frappe.throw(_("From date must be before To date"))


def get_results(filters, account_details):
	gl_entries = get_gl_entries(filters)
	data = get_data_with_opening_closing(filters, account_details, gl_entries)
	result = get_result_as_list(data, filters)
	return result

def get_gl_entries(filters):
	order_by = "order by ge_date,ge_account"
	gl_entries = frappe.db.sql(
		"""
		select * from `tabGeneral Ledger` {conditions} {order_by}"""
		.format(
			conditions=get_conditions(filters),
			order_by = order_by
		),
		filters, as_dict=1)
	return gl_entries

def get_conditions(filters):
	conditions = []
	if filters.get("account"):
		lft, rgt = frappe.db.get_value("Account", filters["account"], ["lft", "rgt"])
		conditions.append("""ge_account in (select name from tabAccount
			where lft>=%s and rgt<=%s and docstatus<2)""" % (lft, rgt))
	if not (filters.get("account")):
		conditions.append("ge_date >=%(from_date)s")
		conditions.append("ge_date <=%(to_date)s")
		
	if filters.get("transaction_no"):
		conditions.append("transaction_no=%(transaction_no)s")

    
	return "where {}".format(" and ".join(conditions)) if conditions else ""

def get_result_as_list(data, filters):
	for d in data:
		d['against'] = d.get('against_account')
		if not d.get('ge_date'):
			balance = 0
		balance = get_balance(d, balance, 'debit', 'credit')
		d['balance'] = balance
	return data

def get_balance(row, balance, debit_field, credit_field):
	balance += (row.get(debit_field, 0) -  row.get(credit_field, 0))
	return balance

def get_data_with_opening_closing(filters, account_details, gl_entries):
	data = []
	gle_map = frappe._dict()
	totals, entries = get_accountwise_gle(filters, gl_entries, gle_map)
	#table starts with opening, then the entries, total and then closing
	data.append(totals.opening)
	data += entries
	data.append(totals.total)
	data.append(totals.closing)
	return data

def get_totals_dict():
	def _get_debit_credit_dict(label):
		return _dict(
			ge_account="'{0}'".format(label),
			debit_amount=0.0,
			credit_amount=0.0
		)
	return _dict(
		opening = _get_debit_credit_dict(_('Opening')),
		total = _get_debit_credit_dict(_('Total')),
		closing = _get_debit_credit_dict(_('Closing (Opening + Total)'))
	)

def get_accountwise_gle(filters, gl_entries, gle_map):
	totals = get_totals_dict()
	entries = []

	def dict_value_update(data, key, gle):
		data[key].debit_amount += flt(gle.debit_amount)
		data[key].credit_amount += flt(gle.credit_amount)

	from_date, to_date = getdate(filters.from_date), getdate(filters.to_date)
	for gle in gl_entries:
		if (gle.ge_date < from_date):
			dict_value_update(totals, 'opening', gle)
			dict_value_update(totals, 'closing', gle)

		elif gle.ge_date <= to_date:
			dict_value_update(totals, 'total', gle)
			entries.append(gle)
			dict_value_update(totals, 'closing', gle)

	return totals, entries



def fetch_columns(filters):
	columns = [{
	    "fieldname": "ge_date",
	    "label": _("Posting Date"),
	    "fieldtype": "Date",
	    "width": 180
	},
	{
	    "fieldname": "ge_account",
	    "label": _("Account"),
	    "fieldtype": "Link",
	    "options": "Account",
	},
	{
	    "fieldname": "debit_amount",
	    "label": _("Debit (INR)"),
	    "fieldtype": "Currency",
		"width": 180
	},
 	{
	    "fieldname": "credit_amount",
	    "label": _("Credit (INR)"),
	    "fieldtype": "Cuurency",
	    "width": 180
	},
	{
	    "fieldname": "ge_account_balance",
	    "label": _("Balance (INR)"),
	    "fieldtype": "Float",
	    "width": 180
	},
	{
	"fieldname": "transaction_type",
	"label": _("Transaction Type"),
	"fieldtype": "Link",
	"options": "DocType",
	"width": 180
	},
	{
	"fieldname": "transaction_no",
	"label": _("Transaction No."),
	"fieldtype": "Dynamic Link",
	"options": "transaction_type",
	"width": 180
	},
	{
	"fieldname": "ge_party",
	"label": _("Party Type"),
	"fieldtype": "Data",
	"width": 80
	},
	{
	"fieldname": "ge_party_name",
	"label": _("Party Name"),
	"fieldtype": "Data",
	"width": 180
	},
	{
	"fieldname": "ge_against_account",
	"label": _("Against Account"),
	"fieldtype": "Data",
	"width": 180
	}]
	return columns
