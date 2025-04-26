import frappe
from frappe.website.path_resolver import resolve_path as original_resolve_path

def path_resolver(path: str):
    # if we want to handle the short link
    if frappe.db.exists("Short Link", {"short_link": path}):
        # we want to redirect
        destination = frappe.db.get_value("Short Link", {"short_link": path}, "destination_url")
        frappe.redirect(destination)

    # else pass it on!
    return original_resolve_path(path)