# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Accounting",
			"color": "grey",
			"icon": "octicon octicon-graph",
			"type": "module",
			"label": _("Accounting")
		}
	]
