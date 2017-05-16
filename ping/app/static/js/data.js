var ip =/^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$/i;
window.check = function() {
    var value = document.getElementById('ip').value;
    if (ip.test(value)) {
        document.getElementById('ip').setAttribute('class', 'good');
        return true;
    } else {
        document.getElementById('ip').setAttribute('class', 'bad');
        return false;
    }
};

window.onload = function() {
    document.getElementById('send').onclick = window.check;
    document.getElementById('ip').onblur = window.check;
    document.getElementById('ip').onkeyup = window.check;
}
