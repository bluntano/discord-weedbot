function checkSubmit() {
    var textline = document.getElementById('textline').value;
    var sets = document.getElementById('sets').value;
    var status = document.querySelector('.submitStatus');
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