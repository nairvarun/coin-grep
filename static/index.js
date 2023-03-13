document.getElementById('searchbar').onkeydown = function (e) {
    if (e.key == 'Enter') {
        location.href = `items/${document.getElementById('searchbar').value}`
    }
};
