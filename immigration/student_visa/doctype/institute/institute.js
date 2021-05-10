// Copyright (c) 2021, FinByz Tech Pvt Ltd and contributors
// For license information, please see license.txt

cur_frm.fields_dict.state.get_query = function (doc) {
    return {
        filters: {
            "country": doc.country
        }
    }
};
cur_frm.fields_dict.city.get_query = function (doc) {
    return {
        filters: {
            "state_name": doc.state
        }
    }
};
cur_frm.fields_dict.institute_type.get_query = function (doc) {
    return {
        filters: [
            ['country', 'in', ['', doc.country]] 
        ]     
    }
};
cur_frm.fields_dict.recruitment_rights.get_query = function (doc) {
    return {
        filters: [
            ['recruitment_category', 'in', ['', doc.recruitment_category]] 
        ]     
    }
};

cur_frm.fields_dict.degree_awarded_by.get_query = function(doc) {
	return{
		query: "immigration.controllers.queries.degree_query",
		filters: {
			'state': doc.state
		}
	}
}

frappe.ui.form.on('Institute', {
	refresh: function(frm) {
		frappe.dynamic_link = {doc: frm.doc, fieldname: 'name', doctype: 'Institute'}
		frm.toggle_display(['address_html','contact_html'], !frm.doc.__islocal);
		if(!frm.doc.__islocal) {
			frappe.contacts.render_address_and_contact(frm);
		}
	}
});