# -*- coding: utf-8 -*-
# Copyright (c) 2018, Eric Baril and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class Contract(Document): pass

@frappe.whitelist()
def make_delivery_note(source_name, target_doc=None):
  target_doc = get_mapped_doc("Contract", source_name, {
    "Contract": {
      "doctype": "Delivery Note",
      "validation": {
        "docstatus": ["=", 1]
      }
    }
  }, target_doc, None)

  return target_doc

def make_pickup_note(source_name, target_doc=None):
  target_doc = get_mapped_doc("Contract", source_name, {
    "Contract": {
      "doctype": "Delivery Note",
      "validation": {
        "docstatus": ["=", 1]
      }
    }
  }, target_doc, None)

  return target_doc
