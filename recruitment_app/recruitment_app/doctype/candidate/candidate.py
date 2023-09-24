# Copyright (c) 2023, Ujjwal Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Candidate(Document):
	def on_change(self):
		# compare and update the data to the user doctype
		doc = frappe.get_doc('User', self.user)
		if self.mobile_number != doc.mobile_no:
			doc.mobile_no = self.mobile_number
		if self.date_of_birth != doc.birth_date:
			doc.birth_date = self.date_of_birth
		doc.save()
