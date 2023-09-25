document.getElementById("login").addEventListener("click", function(event) {
    event.preventDefault();
    window.location.href = "/login";
});

// apply-btn
// document.getElementById("apply-btn").addEventListener("click", function(event) {
//     event.preventDefault();
    
// });
function submitJobApplication () {
    const formData = new FormData()
    formData.append('user', frappe.session.user)
    formData.append('job_id', document.getElementById('job-id').value)
    fetch('/api/method/recruitment_app.api.create_job_application', {
        method: 'POST',
        headers: {
           'X-Frappe-CSRF-Token' : frappe.csrf_token
        },
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('apply-btn').hidden = true
            const badge = document.getElementById('badge')
            badge.hidden = false
            badge.innerHTML = `Applied on ${frappe.datetime.get_today()}`
            frappe.msgprint(__('application submitted successfully'));
            return response.json();
        } else {
            frappe.msgprint(__('Something went wrong'));
        }
    })
    .catch(error => {
        console.error('Error: ', error);
    });
}

// const makeApicall = (url, formData) => {
    
// }