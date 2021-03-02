// Copyright (c) 2021, FinByz Tech Pvt Ltd and contributors
// For license information, please see license.txt

cur_frm.fields_dict.state_name.get_query = function (doc) {
    return {
        filters: {
            "country": doc.country
        }
    }
};
cur_frm.fields_dict.city_name.get_query = function (doc) {
    return {
        filters: {
            "state_name": doc.state_name
        }
    }
};

frappe.ui.form.on('Branch', { 
	refresh: function(frm) {
		frappe.dynamic_link = {doc: frm.doc, fieldname: 'name', doctype: 'Branch'}
		frm.toggle_display(['address_html','contact_html'], !frm.doc.__islocal);
		if(!frm.doc.__islocal) {
			frappe.contacts.render_address_and_contact(frm);
		}
	}
});
