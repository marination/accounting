// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["General Ledger Report"] = {
	"filters": [
		{
				"fieldname":"from_date",
				"label": __("From Date"),
				"fieldtype": "Date",
				"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
				"reqd": 1,
				"width": "180px"
				},
				{
				"fieldname":"to_date",
				"label": __("To Date"),
				"fieldtype": "Date",
				"default": frappe.datetime.get_today(),
				"reqd": 1,
				"width": "60px"
				},
				{
				"fieldname":"account",
				"label": __("Account"),
				"fieldtype": "Link",
				"options": "Account",
				},
				{
				"fieldname":"transaction_no",
				"label": __("Transaction No."),
				"fieldtype": "Data"
				},
				{
				"fieldname":"party",
				"label": __("Party"),
				"fieldtype": "Link",
				"options": "Party",
},
	]
};
