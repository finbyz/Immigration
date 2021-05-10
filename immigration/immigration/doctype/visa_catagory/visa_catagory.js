// Copyright (c) 2021, FinByz Tech Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Visa Catagory', {
	onload: function(frm) {
		frm.list_route = "Tree/Visa Catagory";

		//get query select item group
		frm.fields_dict['parent_visa_catagory'].get_query = function(doc,cdt,cdn) {
			return{
				filters:[
					['Visa Catagory', 'is_group', '=', 1],
					['Visa Catagory', 'name', '!=', doc.visa_catagory_name]
				]
			}
		}
	},
	refresh: function(frm) {
		frm.trigger("set_root_readonly");
		frm.add_custom_button(__("Visa Catagory Tree"), function() {
			frappe.set_route("Tree", "Visa Catagory");
		});

		// if(!frm.is_new()) {
		// 	frm.add_custom_button(__("Items"), function() {
		// 		frappe.set_route("List", "Item", {"item_group": frm.doc.name});
		// 	});
		// }
	},
	
	set_root_readonly: function(frm) {
		// read-only for root item group
		frm.set_intro("");
		if(!frm.doc.parent_item_group && !frm.doc.__islocal) {
			frm.set_read_only();
			frm.set_intro(__("This is a root work area and cannot be edited."), true);
		}
	},
	page_name: frappe.utils.warn_page_name_change
});
