window.addEventListener("load",function(){
    document.getElementById("decipherForm").addEventListener("submit", formSubmit);
});

function formSubmit(event) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 || this.status == 200) {
            if (this.responseText) {
                var response = JSON.parse(this.responseText);
                console.log(response);

                if (response.error) {
                    document.getElementById("resultContainer").classList.add("hidden");
                    document.getElementById("errorContainer").classList.remove("hidden");
                    document.getElementById("resultPlaintext").innerText = "";
                    document.getElementById("resultKey").innerText = "";
                    document.getElementById("resultError").innerText = response.message;
                } else {
                    document.getElementById("resultContainer").classList.remove("hidden");
                    document.getElementById("errorContainer").classList.add("hidden");
                    document.getElementById("resultPlaintext").innerText = response.message;
                    document.getElementById("resultKey").innerText = response.key;
                    document.getElementById("resultError").innerText = "";
                }
            }
        }
    }

    var formCiphertext = document.getElementById("ciphertext").value;
    var formKeylength = document.getElementById("keylength").value;
    var params = "ciphertext=" + formCiphertext + "&keylength=" + formKeylength;

    xhr.open("POST", "/decrypt", true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    xhr.send(params);

    event.preventDefault();
}