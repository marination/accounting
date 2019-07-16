// Copyright (c) 2019, frappe and contributors
// For license information, please see license.txt
{% include 'accounting/public/js/custom_button.js' %}

function total_amount(frm) {
	var total_debit = 0, total_credit = 0;
	var total_diff = 0;
	frm.doc.transaction.forEach(function (d) {
		total_debit += flt(d.debit);
		total_credit += flt(d.credit);
	});
	frm.set_value("total_db", total_debit);
	frm.set_value("total_cr", total_credit);
	total_diff = flt(frm.doc.total_db) - flt(frm.doc.total_cr);
	frm.set_value("difference", total_diff);
	frm.refresh_fields();
}

frappe.ui.form.on('Journal Entry Table', {
	refresh: function (frm) {
		let child = locals[index][row];
		if (child.party_type == "Customer") {
			frm.set_query("party", function () {
				return {
					filters: {
						party_type: 'Customer'
					}
				};
			});
		}
	},
	debit: function (frm) {
		total_amount(frm);
	},
	credit: function (frm) {
		total_amount(frm);
	},
	transaction_remove: function (frm) {
		total_amount(frm);
	},

});


frappe.ui.form.on('Journal Entry', {
	refresh: function (frm, index, row) {
		custom_button(frm);
	}
});
