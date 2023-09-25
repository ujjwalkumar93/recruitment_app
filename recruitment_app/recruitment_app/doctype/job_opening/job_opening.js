// Copyright (c) 2023, Ujjwal Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Opening', {
	before_save : function(frm){
		frm.doc.publish ? frm.doc.posted_on = frappe.datetime.nowdate() : null;
	}
});
