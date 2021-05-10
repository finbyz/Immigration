from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def degree_query(doctype, txt, searchfield, start, page_len, filters):
	cond = ""
	args = {
		'state': filters.get("state"),
	}
	degree_awarded_by = None
	
	degree_awarded_by = frappe.db.sql("""select ca.certificate_awarded_by
			from `tabCertificate Awarded By` ca
				where ca.state = %(state)s
			""",args)
	if degree_awarded_by:
		return degree_awarded_by
	# else:
	# 	frappe.throw(_('Grade not Found. Please define the grade in Item <strong>{}</strong>'))