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
		{
		//code
		}
	},
	account : function(frm,index,row){
		let child  = locals[index][row];
		if (frm.doc.difference > 0){
			child.credit = flt(frm.doc.difference);
			child.debit = 0.0 ;
		}
		else if (frm.doc.difference < 0) {
			child.debit = flt(frm.doc.difference) * -1;
			child.credit = flt(0.0) ;
		}
		total_amount(frm);
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
	refresh: function (frm) {
		custom_button(frm);
		frm.set_value("date",frappe.datetime.now_date());
	}
});
