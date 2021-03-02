from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import load_address_and_contact, delete_contact_and_address


def onload(self,method):
    """Load address and contacts in `__onload`"""
    load_address_and_contact(self)

def on_trash(self,method):
    delete_contact_and_address('Institute', self.name)