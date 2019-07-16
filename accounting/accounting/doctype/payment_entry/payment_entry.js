// Copyright (c) 2019, frappe and contributors
// For license information, please see license.txt
{% include 'accounting/public/js/custom_button.js' %}

frappe.ui.form.on('Payment Entry', {
	 party_type: function(frm) {
     if (frm.doc.party_type == 'Customer') {
       frm.set_value("pay_from",'Debtors');
       }
     else {
        frm.set_value("pay_from",'Cash');
      }

   },
   refresh: function(frm){
    custom_button(frm);
   }
});