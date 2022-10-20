var div = document.getElementById("target");
        div.onload = function() {
            div.style.height =
              div.contentWindow.document.body.scrollHeight +'px';
        }