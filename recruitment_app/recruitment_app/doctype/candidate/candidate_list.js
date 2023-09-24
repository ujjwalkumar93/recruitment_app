// frappe.listview_settings['Candidate'] = {
//     onload: function(listview) {
//         // Customize the ListView here
//         // listview.page.add_menu_item('Custom Action', function() {
//         //     // Perform a custom action when the menu item is clicked
//         //     frappe.msgprint('Custom Action Clicked');
//         // });
//     },
//     filters: [
//         // Add custom filters here
//         ["Candidate", "owner", "=", frappe.session.user]

//     ],
//     get_indicator: function(doc) {
//         // Customize indicator colors
//         if (doc.status === 'Pending') {
//             return [__("Pending"), 'orange', 'status,=,Pending'];
//         } else if (doc.status === 'Completed') {
//             return [__("Completed"), 'green', 'status,=,Completed'];
//         }
//     },
// };

// frappe.listview_settings['Candidate'].refresh = function(listview) {
// 	$('.btn-primary').hide();
// };
