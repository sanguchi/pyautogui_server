function send_key(textbox) {
    var value = textbox.value;
    console.log('You pressed ' + textbox.value);
    jQuery.get('/keypress/' + value, function(data) {
        //alert(data);
        textbox.value = '';
    })
}

function send_hotkey(button) {
    var value = button.value;
    console.log('You pressed ' + value);
    jQuery.get('/keypress/' + value, function(data) {
        //alert(data);
    })
}