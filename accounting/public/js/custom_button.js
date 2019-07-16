function custom_button(frm){
    frm.add_custom_button("Go to General Ledger",function(){
        frappe.set_route("query-report","General Ledger Report",{'transaction_no':frm.doc.name});
        // frappe.query_report.load();
        
    });
     if (frm.doc.docstatus == 1 && (frm.doc.doctype == 'Sales Invoice'|| frm.doc.name == 'Purchase Invoice')) {
        frm.add_custom_button("Payment Entry",function(){
            frappe.call({
                method : 'accounting.api.make_payment_entry',
                args: {
                    'invoice_no': frm.doc.name,
                    'transaction_type': frm.doc.doctype,
                },
                callback: (result) => {
                    frappe.route_options = result.message;
                    frappe.set_route("Form","Payment Entry","New Payment Entry");
                }
            });
            
        });

    }
}