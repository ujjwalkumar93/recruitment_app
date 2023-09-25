frappe.listview_settings['Job Application'] = {
    onload: function(listview) {
        listview.page.add_action_item('Schedule Interview', () => {
            const docNames = [];
            $.each(listview.get_checked_items(), function(key, value) {
                docNames.push(value.name);
            });
            frappe.call({
                method: 'recruitment_app.api.schedule_interview_in_bg', 
                args:{
                    docList : JSON.stringify(docNames)
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.msgprint(`Interview will be scheduled in background job`);
                    }
                }
            });
        });
    },
    
};
