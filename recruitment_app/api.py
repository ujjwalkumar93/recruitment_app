

import frappe
# from frappe.utils.file_manager import save_file

@frappe.whitelist()
def update_profile(docname, name, email, mobile,dob, gender, cgpa, address):
    doc = frappe.get_doc('Candidate', docname)
    doc.name1 = name
    if gender != 'select':
        doc.gender = gender
    doc.mobile_number = mobile
    doc.email = email
    doc.address = address
    doc.date_of_birth = dob
    doc.cgpa = cgpa
    doc.save()
    return doc

def create_job_application()


    


