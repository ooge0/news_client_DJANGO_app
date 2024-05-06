function changeRecordsPerPage(value) {
    window.localStorage.setItem('recordsPerPage', value);
    window.location.href = "?page=1&records_per_page=" + value;
}

function `saveRecordsPerPage`() {
    var recordsPerPage = document.getElementById('recordsPerPage').value;
    window.localStorage.setItem('recordsPerPage', recordsPerPage);
}

document.addEventListener('DOMContentLoaded', function() {
    var recordsPerPage = window.localStorage.getItem('recordsPerPage');
    if (recordsPerPage) {
        document.getElementById('recordsPerPage').value = recordsPerPage;
    }
});
