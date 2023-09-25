import frappe

def get_context(contex):

    data = frappe.db.sql("select name,name1,gender, date_of_birth, mobile_number, address,email,cgpa from `tabCandidate` where user='{usr}'".format(usr=frappe.session.user), as_dict=1)
    candidate = frappe.db.sql("select name from `tabCandidate` where user = '{user}'".format(user = frappe.session.user), as_dict = True)
    if len(candidate) > 0:
        applied_jobs = frappe.db.sql("select name, job, status, applied_on, interview_date from `tabJob Application` where candidate = '{candidate}'".format(candidate=candidate[0].name), as_dict=1)
        application_details = []
        for job in applied_jobs:
            job_opening = frappe.get_doc('Job Opening', job.job)
            job.company_name = job_opening.get('organization_name')
            job.location = job_opening.get('location')
            job.posted_on = job_opening.get('posted_on')
            job.job_title = job_opening.get('job_title')
            job.job_id = job_opening.get('name')
            application_details.append(job)
        
        if len(data) > 0:
            prepared_data = data[0]
            prepared_data.applied_jobs = application_details
            contex.profile = prepared_data
        # else:
        #     contex.profile = {}
    return contex

