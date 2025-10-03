let userRole = null; // global user role

function showSection(sectionId, parentId) {
    document.querySelectorAll(`#${parentId} > .span-section`).forEach(s => s.classList.remove('active'));
    document.getElementById(sectionId).classList.add('active');
    switch(sectionId) {
        case 'student_grades_section': loadStudentGrades(); break;
        case 'student_timetable_section': loadStudyHours(); break;
        case 'student_subjects_section': loadSubjectRecommendations(); break;
        case 'admin_students_section': loadStudentList(); break;
        case 'admin_upload_section': resetUploadSection(); break;
        case 'admin_add_grade_section': resetAddGradeSection(); break;
    }
}

async function login() {
    const username = document.getElementById('login_username').value.trim();
    const password = document.getElementById('login_password').value.trim();
    const loginMsg = document.getElementById('login_message');
    loginMsg.textContent = '';

    if (!username || !password) {
        loginMsg.textContent = 'Please enter username and password.';
        return;
    }

    try {
        const res = await fetch('/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username, password})
        });
        const data = await res.json();
        if (res.ok) {
            userRole = data.role;
            document.getElementById('login_section').style.display = 'none';
            if (userRole === 'admin') {
                document.getElementById('admin_dashboard').style.display = 'block';
                document.getElementById('student_dashboard').style.display = 'none';
                showSection('admin_students_section', 'admin_dashboard');
            } else {
                document.getElementById('student_dashboard').style.display = 'block';
                document.getElementById('admin_dashboard').style.display = 'none';
                showSection('student_grades_section', 'student_dashboard');
            }
        } else {
            loginMsg.textContent = data.message || 'Login failed.';
        }
    } catch {
        loginMsg.textContent = 'Network or server error occurred.';
    }
}

async function logout() {
    try {
        await fetch('/logout');
        location.reload();
    } catch {
        alert('Logout failed.');
    }
}

async function loadStudentGrades() {
    const container = document.getElementById('grades_table_container');
    container.innerHTML = '<div class="spinner"></div>';
    try {
        const res = await fetch('/student/grades');
        const data = await res.json();
        if (!res.ok) throw new Error(data.message || 'Failed to load grades');
        if (!data.grades.length) {
            container.innerHTML = '<p>No grades available.</p>';
            return;
        }
        let html = `<table class="grades-table"><thead><tr><th>Subject</th><th>Mark</th><th>Grade</th><th>Date</th></tr></thead><tbody>`;
        data.grades.forEach(g => {
            html += `<tr><td>${g.subject}</td><td>${g.mark}</td><td>${g.grade}</td><td>${g.exam_date}</td></tr>`;
        });
        html += `</tbody></table>`;
        container.innerHTML = html;
    } catch (e) {
        container.innerHTML = `<p style="color:red;">Error: ${e.message}</p>`;
    }
}

async function loadStudyHours() {
    const container = document.getElementById('study_hours_container');
    container.innerHTML = '<div class="spinner"></div>';
    try {
        const res = await fetch('/hours');
        const data = await res.json();
        if (!res.ok) throw new Error(data.message || 'Failed to fetch study hours');
        if (!data.predicted_hours || Object.keys(data.predicted_hours).length === 0) {
            container.innerHTML = 'No study hour predictions available.';
            return;
        }
        let table = '<table><thead><tr><th>Subject</th><th>Predicted Study Hours</th></tr></thead><tbody>';
        for (const [subject, hours] of Object.entries(data.predicted_hours)) {
            table += `<tr><td>${subject}</td><td>${hours} hours</td></tr>`;
        }
        table += '</tbody></table>';
        container.innerHTML = table;
    } catch (e) {
        container.innerHTML = '<p>Failed to load study hours. Please try again later.</p>';
    }
}

// Placeholder for subject recommendations
function loadSubjectRecommendations() {
    const container = document.getElementById('student_subjects_section');
    container.innerHTML = '<p>Subject recommendations feature yet to be developed.</p>';
}

async function loadStudentList() {
    const res = await fetch('/students');
    const students = await res.json();
    const list = document.getElementById('student_list');
    list.innerHTML = '';
    if (students.length === 0) {
        list.innerHTML = '<li>No students registered yet.</li>';
        return;
    }
    students.forEach(s => {
        const li = document.createElement('li');
        li.innerHTML = `<span>${s.name} (${s.admission_number})</span> <button onclick="viewStudentDashboard('${s.admission_number}')">View Dashboard</button>`;
        list.appendChild(li);
    });
}

async function viewStudentDashboard(adm) {
    showSection('admin_student_dashboard_view', 'admin_dashboard');
    const res = await fetch(`/admin/student/${adm}`);
    const data = await res.json();
    if (!res.ok) {
        alert(data.message || 'Error fetching student data.');
        return;
    }
    document.getElementById('admin_student_name_display').textContent = data.name;
    document.getElementById('admin_student_adm_display').textContent = data.admission_number;
    document.getElementById('admin_class_position').textContent = data.class_position || 'N/A';
    document.getElementById('admin_overall_position').textContent = data.overall_position || 'N/A';
    const gradesList = document.getElementById('admin_student_grades_list');
    gradesList.innerHTML = '';
    if (data.grades && data.grades.length > 0) {
        data.grades.forEach(g => {
            const li = document.createElement('li');
            li.textContent = `Subject: ${g.subject}, Mark: ${g.mark}, Grade: ${g.grade} (Date: ${g.exam_date})`;
            gradesList.appendChild(li);
        });
    } else {
        gradesList.innerHTML = '<li>No grades available for this student.</li>';
    }
}

async function uploadGrades() {
    const fileInput = document.getElementById('grades_file');
    const spinner = document.getElementById('upload_spinner');
    if (!fileInput.files || fileInput.files.length === 0) {
        alert('Please select a file to upload.');
        return;
    }
    spinner.style.display = 'block';
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    try {
        const res = await fetch('/upload_grades', { method: 'POST', body: formData });
        const data = await res.json();
        alert(data.message);
        loadStudentList();
    } catch (e) {
        alert("Upload failed: " + e.message);
    } finally {
        spinner.style.display = 'none';
    }
}

async function addStudent() {
    const name = document.getElementById('student_name').value;
    const admission_number = document.getElementById('student_adm').value;
    const password = document.getElementById('student_password').value;
    const res = await fetch('/students', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, admission_number, password})
    });
    alert((await res.json()).message);
    document.getElementById('student_name').value = '';
    document.getElementById('student_adm').value = '';
    document.getElementById('student_password').value = '';
    loadStudentList();
}

function resetUploadSection() {
    document.getElementById('grades_file').value = '';
    document.getElementById('upload_spinner').style.display = 'none';
}

function resetAddGradeSection() {
    document.getElementById('single_grade_adm_number').value = '';
    document.getElementById('single_grade_subject').value = '';
    document.getElementById('single_grade_mark').value = '';
}

// Initial page setup
window.onload = function() {
    document.getElementById('student_dashboard').style.display = 'none';
    document.getElementById('admin_dashboard').style.display = 'none';
    document.getElementById('login_section').style.display = 'block';
};
