
var botonIngreso = document.getElementById("botonIngreso");
botonIngreso.addEventListener("click", ingreso);
var botonRegistro = document.getElementById("botonRegistro");
botonRegistro.addEventListener("click", registro);

function ingreso(){
    var correoIngreso = document.getElementById("correoIngreso").value;
    var contraseniaIngreso = document.getElementById("contraseniaIngreso").value;
// -------------------------------------------------- 
    // const fs = require("fs");

    // fs.open("usuarios.txt", "r", (err, file) => {
    // if (err) throw err;
    // fs.readFile(file, (err, data) => {
    //     if (err) throw err;
    //     console.log(data.toString());
    // });
    // }); 
// --------------------------------------------------     
    if (correoIngreso == localStorage.correo && contraseniaIngreso == localStorage.contrasenia){
        alert('Vienbenido: ' + correoIngreso);
    }
    else{
        alert('No funciono, volver a intentar');
    }
}

function registro(){
    var correoRegistro = document.getElementById("correoRegistro").value;
    var contraseniaRegistro = document.getElementById("contraseniaRegistro").value;
    var contraseniaRegistroRepetir = document.getElementById("contraseniaRegistroRepetir").value;
    
    if (contraseniaRegistro == contraseniaRegistroRepetir){
        guardarDatos(correoRegistro, contraseniaRegistro);
        // alert('Las contraseñas son iguales');
    }
    else{
        alert('Las contraseñas ingresadas son distintas!');
    }
}

function guardarDatos(correo, contrasenia){
    localStorage.correo = correo;
    localStorage.contrasenia = contrasenia;
    // alert(localStorage.correo + ' ' + localStorage.contrasenia);
    // const fs = require("fs");

    // fs.open("usuarios.txt", "a+", (err, file) => {
    //     if (err) throw err;
    //     alert(file);
    //  });
    // appendFile("usuarios.txt", "String(correo) + ' ' + String(contrasenia) + '\n'", (err) => {
    //    if (err) throw err;
    //    alert("Completed!");
    // });
}