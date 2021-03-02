# -*- coding: utf-8 -*-
# Copyright (c) 2021, FinByz Tech Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class CompanyWorkArea(Document):
	def validate(self):

		if not self.parent_company_work_area and not frappe.flags.in_test:
			if frappe.db.exists("Company Work Area", _('All Company Work Areas')):
				self.parent_company_work_area = _('All Company Work Areas')
