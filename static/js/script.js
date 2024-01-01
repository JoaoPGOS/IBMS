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

window.addEventListener('scroll', function() {
    if (window.scrollY > 100) {
        document.querySelector('.navbar').style.background = '#111';
    }else if(window.scrollY < 100){
        document.querySelector('.navbar').style.background = 'transparent';
    }
});


div.addEventListener('mouseover', pararRolagem);
div.addEventListener('mouseout', iniciarRolagem);

function contatoslink(){
    document.getElementById('Contato').click();
}

function produtoslink(){
    document.getElementById('produtos').click();
}


document.getElementById("Contato").addEventListener("click", function() {
    window.scrollTo({top:document.body.scrollHeight - 1050,
        behavior: 'smooth'});
});

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





checagem();
iniciarRolagem();