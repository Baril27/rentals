// Copyright (c) 2018, Eric Baril and contributors
// For license information, please see license.txt

frappe.ui.form.on('Contract', {
  refresh: function(frm) {
    // Delivery Ticket
    frm.add_custom_button(__('Delivery'), function() {
      frappe.model.open_mapped_doc({
        method: "rentals.rentals.doctype.contract.contract.make_delivery_note",
        frm: frm
      })
    }, __("Make"));

    // Pickup Ticket
    frm.add_custom_button(__('Pickup'), function() {
      frappe.model.open_mapped_doc({
        method: "rentals.rentals.doctype.contract.contract.make_pickup_note",
        frm: frm
      })
    }, __("Make"));
    frm.page.set_inner_btn_group_as_primary(__("Make"));
  }
});
