// Copyright (c) 2019, frappe and contributors
// For license information, please see license.txt
{% include 'accounting/public/js/custom_button.js' %}

function total(frm){
  let total_amount = 0;
  frm.doc.items.forEach(function(d){
      total_amount += flt(d.amount);
  });
  frm.set_value('total_amount', total_amount);
  frm.refresh_fields();
}

frappe.ui.form.on('Sales Invoice', {
  refresh: function(frm) {
    custom_button(frm);
    frm.set_query("customer",function(){
        return{
               filters:{
                  party_type: 'Customer'
                }
            };
       });
    frm.set_query("debit_to",function(){
        return{
               filters:{
                 parent_account: 'Accounts Receivable'
               }
             }
           });
    frm.set_query("asset_account",function(){
        return{
             filters:{
               parent_account: ["in",["Stock Assets","Fixed Assets"]]
             }
           }
         });
  }
  
});

frappe.ui.form.on('Sales Invoice Item',{
  rate:function(frm,index,row){
      let child_row = locals[index][row];
      child_row.amount = (child_row.rate) * (child_row.quantity);
      total(frm);
      frm.refresh_fields();

    },
  quantity:function(frm,index,row){
      let child_row = locals[index][row];
      child_row.amount = (child_row.rate) * (child_row.quantity);
      total(frm);
      frm.refresh_fields();
    },
  items_remove: function(frm){
    total(frm);
    frm.refresh_fields();
}
});
