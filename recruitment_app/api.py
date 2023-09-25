

import frappe
from frappe.utils import add_days, today
import json
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

@frappe.whitelist()
def create_job_application(user,job_id):
    candidate = frappe.db.sql("select name from `tabCandidate` where user = '{user}'".format(user=user), as_dict=True)[0]
    job_application = frappe.new_doc('Job Application')
    job_application.job = job_id
    job_application.candidate = candidate.get('name')
    job_application.status = 'Applied'
    job_application.applied_on = frappe.utils.nowdate()
    job_application.insert()
    return job_application

@frappe.whitelist()
def schedule_interview_in_bg(docList):
    frappe.enqueue("recruitment_app.api.schedule_interview",docList = docList)
    return True

def schedule_interview(docList):
    for doc in json.loads(docList):
        job_application = frappe.get_doc('Job Application', doc)
        if job_application.status != 'Interview Scheduled':
            job_application.status = 'Interview Scheduled'
            # add 2 days from now for interview date
            job_application.interview_date = add_days(today(), 2)
            job_application.save()
    return True

def on_user_create(doc, method):
    candidate = frappe.new_doc('Candidate')
    candidate.user = doc.name
    candidate.email = doc.email
    candidate.insert(ignore_permissions = True)
    print(doc.email)






    


