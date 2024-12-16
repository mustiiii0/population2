// Main JavaScript file for common functionality

document.addEventListener('DOMContentLoaded', function() {
    // Handle flash messages
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });

    // Handle mobile navigation
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });

            if (!isValid) {
                event.preventDefault();
                alert('الرجاء ملء جميع الحقول المطلوبة');
            }
        });
    });
});

// Utility functions
function formatDate(date) {
    return new Date(date).toLocaleDateString('ar-SA');
}

function confirmDelete(message = 'هل أنت متأكد من الحذف؟') {
    return confirm(message);
}