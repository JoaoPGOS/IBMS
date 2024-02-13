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


function galerialink(){
    window.location.replace('/galeria')
}

function downloadslink(){
        window.location.replace('/downloads')
}
function produtoslink(){
    document.getElementById('produtos').click();
}

function servicoslink(){
    document.getElementById('servicos').click();
}

function portlink(){
    window.location.replace('/portifolio')
}



function promo(p){
    if(p == 'S'){
        document.getElementById('promocao').value = '1'
        S = document.getElementById('S')
        S.style.background = 'var(--color-primary)'
        S.style.color = 'var(--color-1)'

        N = document.getElementById('N')
        N.style.color = 'var(--color-primary)'
        N.style.background = 'var(--color-1)'
    }else{
        document.getElementById('promocao').value = '0'
        S = document.getElementById('S')
        S.style.color = 'var(--color-primary)'
        S.style.background = 'var(--color-1)'

        N = document.getElementById('N')
        N.style.background = 'var(--color-primary)'
        N.style.color = 'var(--color-1)'
    }
}


function search(value){
    creury = document.querySelectorAll('.pesquisa')
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

