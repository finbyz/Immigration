# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Student visa"),
			"items": [
				{
					"type": "doctype",
					"name": "Institute",
				},
				{
					"type": "doctype",
					"name": "Program",
				},
				{
					"type": "doctype",
					"name": "Branch",
				},
				{
					"type": "doctype",
					"name": "Exam",
				},
			]
		},
		{
			"label": _("General"),
			"items": [
				{
					"type": "doctype",
					"name": "City",
				},
				{
					"type": "doctype",
					"name": "State",
				},
				{
					"type": "doctype",
					"name": "License",
				},
				{
					"type": "doctype",
					"name": "Company Work Area",
				},
				{
					"type": "doctype",
					"name": "Visa Catagory",
				},
			]
		},
		
	]