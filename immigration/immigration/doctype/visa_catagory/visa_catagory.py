# -*- coding: utf-8 -*-
# Copyright (c) 2021, FinByz Tech Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class VisaCatagory(Document):
	def validate(self):

		if not self.parent_visa_catagory and not frappe.flags.in_test:
			if frappe.db.exists("Visa Catagory", _('All Visa Catagory')):
				self.parent_visa_catagory = _('All Visa Catagory')