import frappe

def get_context(contex):
    data = frappe.db.sql("select name,name1,gender, date_of_birth, mobile_number, address,email,cgpa from `tabCandidate` where user='{usr}'".format(usr=frappe.session.user), as_dict=1)
    if len(data) > 0:
        contex.profile = data[0]
    else:
        contex.profile = {}
    return contex

