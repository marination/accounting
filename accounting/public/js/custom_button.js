function custom_button(frm,amount) {
    if (frm.doc.docstatus == 1 && (frm.doc.doctype == 'Sales Invoice' || frm.doc.doctype == 'Purchase Invoice')) {
        frm.add_custom_button("Payment Entry", function () {
            frappe.model.with_doctype("Payment Entry",function(){
                let doc = frappe.model.get_new_doc("Payment Entry");
                if (frm.doc.doctype == 'Purchase Invoice'){
                    doc.pay_from = 'Cash';
                    doc.pay_to = 'Creditors';
                    doc.type = 'Pay';
                    doc.party_type = 'Supplier';
                    doc.party  = frm.doc.supplier;
                    doc.amount = amount.toString();
                    doc.transaction = frm.doc.doctype;
                    doc.transaction_name = frm.doc.name;
                }
                else{
                    doc.pay_from = 'Debtors';
                    doc.pay_to = 'Cash';
                    doc.type = 'Receive';
                    doc.party_type = 'Customer';
                    doc.party  = frm.doc.customer;
                    doc.amount = amount.toString();
                    doc.transaction = frm.doc.doctype;
                    doc.transaction_name = frm.doc.name;
                }
                frappe.set_route("Form", doc.doctype, doc.name);

            }) 
        });
        frm.add_custom_button("Go to General Ledger", function () {
            frappe.set_route("query-report", "General Ledger Report", { 'transaction_no': frm.doc.name });

        });

    }
    
}
