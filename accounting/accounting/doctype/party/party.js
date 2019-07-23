// Copyright (c) 2019, frappe and contributors
// For license information, please see license.txt
{% include 'accounting/public/js/custom_button.js' %}

frappe.ui.form.on('Party', {
	refresh: function(frm) {
		custom_button(frm);
	}
});
