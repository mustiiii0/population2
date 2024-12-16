document.addEventListener('DOMContentLoaded', function() {
    const hasChildrenSelect = document.getElementById('has_children');
    const childrenCountDiv = document.querySelector('.children-count');
    
    // Handle children count visibility
    hasChildrenSelect.addEventListener('change', function() {
        childrenCountDiv.style.display = 
            this.value === 'true' ? 'block' : 'none';
    });

    // Handle file upload preview
    const photoInput = document.getElementById('photo');
    const photoPreview = document.createElement('div');
    photoPreview.className = 'photo-preview';
    photoInput.parentNode.appendChild(photoPreview);

    photoInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                photoPreview.innerHTML = `
                    <img src="${e.target.result}" alt="Preview">
                    <button type="button" class="remove-photo">إزالة</button>
                `;
            };
            reader.readAsDataURL(file);
        }
    });

    // Handle photo removal
    photoPreview.addEventListener('click', function(event) {
        if (event.target.classList.contains('remove-photo')) {
            photoInput.value = '';
            photoPreview.innerHTML = '';
        }
    });

    // Form validation
    const form = document.querySelector('.person-form');
    form.addEventListener('submit', function(event) {
        const birthDate = new Date(document.getElementById('birth_date').value);
        const today = new Date();

        if (birthDate > today) {
            event.preventDefault();
            alert('تاريخ الميلاد لا يمكن أن يكون في المستقبل');
        }
    });
});
