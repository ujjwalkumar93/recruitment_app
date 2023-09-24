import frappe

def get_context(contex):
    query = "select organization_name,location,creation, job_title, logo, minimum_cgpa, total_opening, budget_from, budget_to, description from `tabJob Opening` where publish = 1 and name='{name}';".format(name = frappe.form_dict.get('id'))
    contex.job_description = frappe.db.sql(query, as_dict = True)[0]
    # context.add_breadcrumbs = True
    return contex