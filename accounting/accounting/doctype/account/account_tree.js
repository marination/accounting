{% include 'accounting/public/js/custom_button.js' %}

frappe.provide("frappe.treeview_settings")
frappe.treeview_settings['Account']= {
    ignore_fields : ["parent_account"],
    toolbar: [
		{
			condition: function(node) {
				return !node.root && frappe.boot.user.can_read.indexOf("General Ledger") !== -1
			},
			label: __("View Ledger"),
			click: function(node, btn) {
				frappe.route_options = {
					"account": node.label,
					"from_date": frappe.datetime.add_months(frappe.datetime.now_datetime(), -12) ,  //frappe.sys_defaults.year_start_date,
					"to_date": frappe.datetime.now_datetime(),
				};
				frappe.set_route("query-report", "General Ledger Report");
			},
			btnClass: "hidden-xs"
		}
	],
	extend_toolbar: true
}
