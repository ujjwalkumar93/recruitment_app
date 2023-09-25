import frappe

def get_context(contex):
    candidate = frappe.db.sql("select name from `tabCandidate` where user = '{user}'".format(user = frappe.session.user), as_dict = True)
    query = "select name, organization_name,location,posted_on, job_title, logo, minimum_cgpa, total_opening, budget_from, budget_to, description from `tabJob Opening` where publish = 1 and name='{name}';".format(name = frappe.form_dict.get('id'))
    job_description = frappe.db.sql(query, as_dict = True)[0]
    if len(candidate) > 0:
        isApplied = frappe.db.sql("select applied_on from `tabJob Application` where candidate = '{candidate}' and job = '{job_id}'".format(candidate=candidate[0].name, job_id=frappe.form_dict.get('id')), as_dict= True)
        if len(isApplied) > 0:
            job_description.applied_on = isApplied[0].applied_on
    contex.job_description = job_description
    return contex