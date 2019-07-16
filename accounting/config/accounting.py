from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label":_("Primary"),
            "icon": "octicon octicon-graph",
            "items":
            [
                {
                  "type": "doctype",
                  "name": "Item",
                  "label": _("Item"),
                  "description": _("Items which members buy and sell"),
                },
                {
                  "type": "doctype",
                  "name": "Party",
                  "label": _("Party"),
                  "description": _("Customers or Suppliers involved "),
                },
                {
                  "type": "doctype",
                  "name": "Account",
                  "label": _("Chart of Accounts"),
                  "route": "#Tree/Account",
                  "description": _("Various accounts that participate in transactions"),
                },

            ]
        },
        {
            "label":_("Transactions"),
            "icon": "octicon octicon-graph",
            "items":
            [
                {
                  "type": "doctype",
                  "name": "Purchase Invoice",
                  "label": _("Purchase Invoice"),
                  "description": _("Invoice received against a purchase order"),
                },
                {
                  "type": "doctype",
                  "name": "Sales Invoice",
                  "label": _("Sales Invoice"),
                  "description": _("Invoice sent for a sales order "),
                },
                {
                  "type": "doctype",
                  "name": "Payment Entry",
                  "label": _("Payment Entry"),
                  "description": _("Tracking Paid transactions "),
                },
                {
                  "type": "doctype",
                  "name": "Journal Entry",
                  "label": _("Journal Entry"),
                  "description": _("Internal Transactions"),
                }
            ]
        },
        {
            "label":_("Reports"),
            "icon": "octicon octicon-graph",
            "items":
            [
                {
                  "type": "report",
                  "name": "General Ledger Report",
                  "label": _("General Ledger Report"),
                  "doctype": "General Ledger",
                  "route": "#query-report/General Ledger Report"

                },
                {
                  "type": "report",
                  "name": "Trial Balance Statement",
                  "label": _("Trial Balance Statement"),
                  "doctype": "General Ledger",
                  "route": "#query-report/Trial Balance Statement"
                }

            ]
        }


    ]
