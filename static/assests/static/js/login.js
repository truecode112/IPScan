async function loginWithEmail() {
    const email = $('#email').val();
    const password = $('#password').val();
    if (!email || !password) {
        showToastr('Error', "Please enter correct information", "red")
        return;
    }

    $('#loginWithEmailButton').addClass('hidden');
    $('#emailLoginLoadingButton').removeClass('hidden');
    
    try {
        const result = await fetch(loginUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ email, password })
        }).then(response => response.json());

        if (result.success) {
            window.location.href = '/dashboard/';
        }
        else {
            showToastr('Error', result.message, "red")
            $('#loginWithEmailButton').removeClass('hidden');
            $('#emailLoginLoadingButton').addClass('hidden');
        }
    } catch (error) {
        showToastr('Error', error.message, "red")
        $('#loginWithEmailButton').removeClass('hidden');
        $('#emailLoginLoadingButton').addClass('hidden');
    }
}
