import frappe
def get_context(contex):
    contex.job_opening_list = frappe.db.sql('select name,organization_name,location,posted_on, job_title, logo, minimum_cgpa, total_opening, budget_from, budget_to, description from `tabJob Opening` where publish = 1;', as_dict = True)
    return contex
