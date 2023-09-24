
document.getElementById('editButton').addEventListener('click', function (event) {
    event.preventDefault();
    const inputFields = document.querySelectorAll('input[readonly]');
    inputFields.forEach(function (input) {
        input.readOnly = false;
    });
    document.getElementById('address').readOnly = false;
    document.getElementById('pdf').disabled = false;
    document.getElementById('gender').disabled = false;
    document.getElementById('editButton').style.display = 'none';
    document.getElementById('saveButton').style.display = 'block';
});

document.getElementById('saveButton').addEventListener('click', function (event) {
    event.preventDefault();
    const docname = document.getElementById('docname').value;
    const inputFields = document.querySelectorAll('#profileForm input');

    inputFields.forEach(function (input) {
        input.setAttribute('readonly', 'readonly'); 
    });
    document.getElementById('address').readOnly = true;
    document.getElementById('pdf').disabled = true;
    document.getElementById('gender').disabled = true;
    document.getElementById('saveButton').style.display = 'none';
    document.getElementById('editButton').style.display = 'block';

    const fileData = new FormData();
    const fileInput = document.getElementById('pdf');
    if(fileInput.files.length > 0){
        fileData.append('file', fileInput.files[0], fileInput.files[0].name);
        fileData.append('doctype', 'candidate');
        fileData.append('docname', docname)
        fetch('/api/method/upload_file', {
            method: 'POST',
            headers: {
               'X-Frappe-CSRF-Token' : frappe.csrf_token
            },
            method: 'POST',
            body: fileData,
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Something went wrong');
            }
        })
        .catch(error => {
            console.error('Error: ', error);
        });
    }

    // document.getElementById('profileForm')
    const formData = new FormData()
    formData.append('docname', docname)
    formData.append('name', document.getElementById('name').value)
    formData.append('email', document.getElementById('email').value)
    formData.append('mobile', document.getElementById('contact').value)
    formData.append('dob', document.getElementById('dob').value)
    formData.append('address', document.getElementById('address').value)
    formData.append('gender', document.getElementById('gender').value)
    formData.append('cgpa', document.getElementById('cgpa').value)
    makeApicall('/api/method/recruitment_app.api.update_profile', formData)
});

document.getElementById('pdf').addEventListener('change', function () {
    const fileInput = this;
    const fileNameContainer = document.querySelector('.file-name');
    const selectedFile = fileInput.files[0];

    if (selectedFile) {
        fileNameContainer.textContent = selectedFile.name;
    } else {
        fileNameContainer.textContent = 'No file chosen';
    }
});

const makeApicall = (url, formData) => {
    fetch(url, {
        method: 'POST',
        headers: {
           'X-Frappe-CSRF-Token' : frappe.csrf_token
        },
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            frappe.msgprint(__('Document updated successfully'));
            return response.json();
        } else {
            frappe.msgprint(__('Something went wrong'));
        }
    })
    .catch(error => {
        console.error('Error: ', error);
    });
}




