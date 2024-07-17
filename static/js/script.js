var div = document.querySelector('.sideimagescontainer');
var speed = 1;

function rolarDiv() {
    if(div.scrollLeft < (div.scrollWidth - div.offsetWidth)) {
        div.scrollLeft += speed;
    } else {
        div.scrollLeft = 0;
    }
}

function iniciarRolagem() {
    intervalo = setInterval(rolarDiv, 20); // Ajuste o intervalo para controlar a velocidade de rolagem
}

function pararRolagem() {
    clearInterval(intervalo);
}



function produtoslink(){
    document.getElementById('produtos').click();
}

function servicoslink(){
    document.getElementById('servicos').click();
}



function filtrar_esgotados(param){
    var elementos = document.querySelectorAll('.pesquisa_N');

    if(param == 0){
        elementos.forEach(function(elemento) {
            elemento.style.display = 'none';
        });
        document.getElementById("produtos_e_filtro").innerHTML = `Produto: <input type="text" name="nome" id="nome" onkeyup="search_esgotados(this.value)" onfocus="displayall()">Descrição: <input type="text" name="descricao" id="desc"><button onclick="filtrar_esgotados(1)" style="margin-left: 1rem; color:var(--color-blue_1); background-color:var(--color-blue_3); border: none; font-weight: bold; cursor:pointer; border-radius: 0px;">Filtrar por esgotados</button>`
    }else{
        elementos.forEach(function(elemento) {
            elemento.style.display = 'block';
        });
        document.getElementById("produtos_e_filtro").innerHTML = `Produto: <input type="text" name="nome" id="nome" onkeyup="search(this.value)" onfocus="displayall()">Descrição: <input type="text" name="descricao" id="desc"><button onclick="filtrar_esgotados(0)" style="margin-left: 1rem; color:var(--color-blue_3); background-color:var(--color-blue_1); border: none; font-weight: bold; cursor:pointer; border-radius: 0px;">Filtrar por esgotados</button>`
    }

    
}

function search_esgotados(value){
    creury = document.querySelectorAll('.pesquisa_S')
    value = value.toUpperCase()
    for(i=0;i != creury.length;i++){
        creu = creury[i].id
        if(creu.toUpperCase().includes(value)==false){
            document.getElementById(creu).style.display = 'none';
        }else{
            document.getElementById(creu).style.display = 'block'
        }
    }
}

function search(value){
    creury = document.querySelectorAll('.pesquisa_N')
    value = value.toUpperCase()
    for(i=0;i != creury.length;i++){
        creu = creury[i].id
        if(creu.toUpperCase().includes(value)==false){
            document.getElementById(creu).style.display = 'none';
        }else{
            document.getElementById(creu).style.display = 'block'
        }
    }
    creury = document.querySelectorAll('.pesquisa_S')
    value = value.toUpperCase()
    for(i=0;i != creury.length;i++){
        creu = creury[i].id
        if(creu.toUpperCase().includes(value)==false){
            document.getElementById(creu).style.display = 'none';
        }else{
            document.getElementById(creu).style.display = 'block'
        }
    }
}

function displayall(){
    document.getElementById('searched').style.width = 'fit-content'
    document.getElementById('searched').style.height = '400px'
    document.getElementById('searched').style.transition = '.5s'
    document.getElementById('searched').style.border = 'var(--color-primary) 1px solid'
}
function changedisplayall(){
    document.getElementById('searched').style.width = '0px'
    document.getElementById('searched').style.height = '0px'
    document.getElementById('searched').style.transition = '.5s'
    document.getElementById('searched').style.border = 'none'
}
function insert_to(name,desc){
    document.getElementById('nome').value = name
    document.getElementById('desc').value = desc
    changedisplayall();
} 

function updateimg(id) {
    var imgInput = document.getElementById(`imgupdate_${id}`);
    var imgFile = imgInput.files[0];
    var selectCarrossel = document.getElementById(`carrossel_${id}`);
    var carrossel = selectCarrossel.value; // Obtém o valor selecionado no select

    var reader = new FileReader();

    reader.onloadend = function() {
        var base64Img = '';

        if (reader.result) {
            base64Img = reader.result.split(',')[1];
        }

        var data = {
            img: base64Img, 
            carrossel: carrossel,
            id: id
        };

        // Enviar os dados para o endpoint /atualizagaleria
        fetch('/atualizagaleria', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                window.location.reload();
            } else {
                console.error('Erro ao atualizar a galeria');
            }
        })
        .catch(error => {
            console.error('Erro na solicitação:', error);
        });
    };

    if (imgFile) {
        reader.readAsDataURL(imgFile);
    } else {
        reader.onloadend();
    }
}



function deleteimg(id) {

    var data = {
        id: id
    };

    fetch('/deleteimg', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {

            window.location.href = window.location.href;
        } else {
            console.error('Erro ao excluir a imagem');
        }
    })
    .catch(error => {
        console.error('Erro na solicitação:', error);
    });
}

function deletedicas(id){
    var data = {
        id: id
    };
    fetch('/deletevideo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {

            window.location.href = window.location.href;
        } else {
            console.error('Erro ao excluir a imagem');
        }
    })
    .catch(error => {
        console.error('Erro na solicitação:', error);
    });
}

function deletepromo(id) {
     
       var xhr = new XMLHttpRequest();

       xhr.open("POST", "/deletepromo", true);

       xhr.setRequestHeader("Content-Type", "application/json");

       xhr.onreadystatechange = function () {
           if (xhr.readyState === XMLHttpRequest.DONE) {
      
               if (xhr.status === 200) {
                   window.location.href = '/inserepromo'
               } else {
                   console.error("Ocorreu um erro:", xhr.statusText);
               }
           }
       };
       
      
       var data = JSON.stringify(id);
       
       
       xhr.send(data);
}


function rollOutMobileNav(){
    var nav = document.querySelector('.navbardown');
    if (nav.style.top != '10vh') {
        nav.style.top = '10vh'
        document.getElementById('mobile').innerHTML = '<path fill-rule="evenodd" d="M3.5 10a.5.5 0 0 1-.5-.5v-8a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 0 0 1h2A1.5 1.5 0 0 0 14 9.5v-8A1.5 1.5 0 0 0 12.5 0h-9A1.5 1.5 0 0 0 2 1.5v8A1.5 1.5 0 0 0 3.5 11h2a.5.5 0 0 0 0-1z"/>\n' +
            '  <path fill-rule="evenodd" d="M7.646 4.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707V14.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708z"/>'
    }else {
        nav.style.top = '-10vh'
        document.getElementById('mobile').innerHTML = '<path fill-rule="evenodd" d="M3.5 10a.5.5 0 0 1-.5-.5v-8a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 0 0 1h2A1.5 1.5 0 0 0 14 9.5v-8A1.5 1.5 0 0 0 12.5 0h-9A1.5 1.5 0 0 0 2 1.5v8A1.5 1.5 0 0 0 3.5 11h2a.5.5 0 0 0 0-1z"/>\n' +
            '  <path fill-rule="evenodd" d="M7.646 15.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 14.293V5.5a.5.5 0 0 0-1 0v8.793l-2.146-2.147a.5.5 0 0 0-.708.708z"/>';
    }

}