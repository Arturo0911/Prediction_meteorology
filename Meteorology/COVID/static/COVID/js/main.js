$(document).ready(function(){

    let valor = [];
    
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:8000/covid/rate/EC/",
        success: function (data){
            valor.push(data)
        }
    });

    const button = document.getElementById('uwu');

    button.addEventListener('click',function(e){
        //alert("te quiero mi vida uwu");
        //saludo.name();

        console.log(valor);
    })


})