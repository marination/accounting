# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Item(Document):
	def validate(self):
		if self.opening_stock <= 0 :
			frappe.throw(_("Please enter an appropriate opening stock"))
