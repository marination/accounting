import frappe


@frappe.whitelist()
def make_payment_entry(invoice_no,transaction_type):
    doc = frappe.get_doc(transaction_type,invoice_no)
    if transaction_type == "Purchase Invoice":
        result = {
            'type':'Pay',
            'party_type':'Supplier',
            'party':doc.supplier,
            'amount':doc.total_amount,
            'transaction':transaction_type,
            'transaction_name':invoice_no
        }
    else:
        result ={
            'type':'Receive',
            'party_type':'Customer',
            'party': doc.customer,
            'amount':doc.total_amount,
            'transaction':transaction_type,
            'transaction_name':invoice_no
        }
    return result