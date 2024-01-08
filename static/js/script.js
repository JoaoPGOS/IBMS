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
function insert_to(name,valor){
    document.getElementById('nome').value = name
    document.getElementById('valor').value = valor
    changedisplayall();
} 
