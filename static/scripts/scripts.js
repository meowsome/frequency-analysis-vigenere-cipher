window.addEventListener("load",function(){
    document.getElementById("decipherForm").addEventListener("click", formSubmit);
});

function formSubmit(event) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 || this.status == 200) {
            console.log(this.responseText);
        }
    }

    var formCiphertext = document.getElementById("ciphertext").value;
    var formKeylength = document.getElementById("keylength").value;
    var params = "ciphertext=" + formCiphertext + "&keylength=" + formKeylength;

    xhr.open("POST", "/decrypt", true);
    xhr.setRequestHeader("Content-type","application/json");

    xhr.send(params);

    event.preventDefault();
}