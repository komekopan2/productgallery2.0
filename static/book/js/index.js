function viewChange() {
    if (document.getElementById('sample')) {
        id = document.getElementById('sample').value;
        if (id == 'select1') {
            document.getElementById('Box1').style.display = "";
            document.getElementById('Box2').style.display = "none";
            document.getElementById('Box3').style.display = "none";
        } else if (id == 'select2') {
            document.getElementById('Box1').style.display = "none";
            document.getElementById('Box2').style.display = "";
            document.getElementById('Box3').style.display = "none";
        }
        else if (id == 'select3') {
            document.getElementById('Box1').style.display = "none";
            document.getElementById('Box2').style.display = "none";
            document.getElementById('Box3').style.display = "";
        }
    }

    window.onload = viewChange;
}