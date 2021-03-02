// Copyright (c) 2021, FinByz Tech Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Company Work Area', {
	onload: function(frm) {
		frm.list_route = "Tree/Company Work Area";

		//get query select item group
		frm.fields_dict['parent_company_work_area'].get_query = function(doc,cdt,cdn) {
			return{
				filters:[
					['Company Work Area', 'is_group', '=', 1],
					['Company Work Area', 'name', '!=', doc.company_work_area_name]
				]
			}
		}
	},
	refresh: function(frm) {
		frm.trigger("set_root_readonly");
		frm.add_custom_button(__("Company Work Area Tree"), function() {
			frappe.set_route("Tree", "Company Work Area");
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
