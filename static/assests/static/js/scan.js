async function scanWebsite() {
    openModal('addTargetModal');
    const target = $('#target').val()
    const tags = $('#tags').val()
    const label = $('#label').val()
    $('#target').val('')
    $('#tags').val('')
    $('#label').val('')

    if (target === '') {
        showToastr('Error', "Please enter a target", "red")
        return;
    }

    const result = await fetch(scanUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ target, tags, label })
    }).then(response => response.json());
    console.log('=====', result)
}