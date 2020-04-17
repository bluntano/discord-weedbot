function checkSubmit() {
    var textline = document.getElementById('textline').value;
    var sets = document.getElementById('sets').value;
    var status = document.querySelector('.submitStatus');
    //var finalButton = document.querySelector('.finalBtn')
    if (!textline) {
        status.innerHTML = "<p>Please insert text to bot to say!</p>";
    } else if (!textline.includes('{}%')) {
        status.innerHTML = "<p>Please insert '{}%' as well to the text!</p>";
    } else if (!sets) {
        status.innerHTML = "<p>Please pick a proper set to submit!</p>";
    } else {
        status.innerHTML = "<button type=\"submit\">Submit!</button>";
    };
};

function post(path, params=' ', method='post') {
    const containerElem = document.querySelector('.container');
    containerElem.classList.add('animated', 'bounceOutLeft');
    setTimeout(function() {
        const form = document.createElement('form');
        form.method = method;
        form.action = path;
        for (const key in params) {
            if (params.hasOwnProperty(key)) {
                const hiddenField = document.createElement('input');
                hiddenField.type = 'hidden';
                hiddenField.name = key;
                hiddenField.value = params[key];
                form.appendChild(hiddenField);
            };
        };
        document.body.appendChild(form);
        form.submit();
    }, 1000);
};