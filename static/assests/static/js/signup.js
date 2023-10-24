async function SignupWithEmail() {
    const email = $('#email').val();
    if (!email) {
        showToastr('Error', "Please enter valid Email", "red")
        return;
    }

    $('#SignupWithEmailButton').addClass('hidden');
    $('#emailSendLoadingButton').removeClass('hidden');

    try {
        const result = await fetch(sendMailUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ to: email })
        }).then(response => response.json());

        if (result.success) {
            $('#emailSendLoadingButton').addClass('hidden');
            $('#emailSentSuccessButton').removeClass('hidden');
            $('#emailSentSuccessInfo').removeClass('hidden');
        }
        else {
            showToastr('Error', result.message, "red")
            $('#emailSendLoadingButton').addClass('hidden');
            $('#SignupWithEmailButton').removeClass('hidden');
        }
    } catch (error) {
        showToastr('Error', error.message, "red")
        $('#emailSendLoadingButton').addClass('hidden');
        $('#SignupWithEmailButton').removeClass('hidden');
    }
}

async function signUp() {
    const email = $('#email').val();
    const password = $('#password').val();
    const confirmPassword = $('#confirmPassword').val();
    const token = $('#token').val();

    if (!email || !password || !confirmPassword) {
        showToastr('Error', "Please enter correct information", "red")
        return;
    }
    if (password !== confirmPassword) {
        showToastr('Error', "Passwords do not match", "red")
        return;
    }
    $('#signupButton').addClass('hidden');
    $('#signupLoadingButton').removeClass('hidden');

    try {
        const result = await fetch(signupUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ email: email, password: password, token: token })
        }).then(response => response.json());
        $('#signupLoadingButton').addClass('hidden');
        $('#signupButton').removeClass('hidden');
        if (result.success) {
            window.location.href = result.redirectUrl;
        }
        else {
            showToastr('Error', result.message, "red")
        }
    } catch (error) {
        showToastr('Error', error.message, "red")
    }
}