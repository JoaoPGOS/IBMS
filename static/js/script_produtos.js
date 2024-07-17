localStorageCarrinho = 'Carrinho'

document.getElementById('downloadExcel').addEventListener('click', function() {
    // Substitua 'caminho/para/sua/planilha.xlsx' pelo caminho real do seu arquivo Excel
    var planilhaUrl = '/static/archives/Nuance.pdf';
    downloadFile(planilhaUrl);

});

document.getElementById('downloadPDF').addEventListener('click', function() {
    // Substitua 'caminho/para/seu/arquivo.pdf' pelo caminho real do seu arquivo PDF
    var pdfUrl = '/static/archives/Prohair.pdf';
    downloadFile(pdfUrl);
});

document.getElementById('downloadExcelFluence').addEventListener('click', function() {
    // Substitua 'caminho/para/seu/arquivo.pdf' pelo caminho real do seu arquivo PDF
    var fluenceUrl = '/static/archives/Fluence.pdf';
    downloadFile(fluenceUrl);
    downloadFile('/static/archives/Fluence2.pdf');
});

document.getElementById('downloadBurana').addEventListener('click', function() {

    var url = '/static/archives/Burana.pdf';
    downloadFile(url);
});


function downloadFile(fileUrl) {
    // Cria um elemento de link temporário
    var link = document.createElement('a');
    link.href = fileUrl;

    // Define o atributo 'download' para baixar o arquivo com o nome original
    link.download = fileUrl.substr(fileUrl.lastIndexOf('/') + 1);

    // Adiciona o link ao corpo do documento
    document.body.appendChild(link);

    // Aciona o clique no link
    link.click();

    // Remove o link do corpo do documento
    document.body.removeChild(link);
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
function send(name){
    textopadrao = `Bom dia, eu me interessei no produto ${name} e gostaria de fazer um orçamento.`
    window.open(` https://wa.me/553197486420?text=${textopadrao}`, '_blank');
}
function inserecarrinho(nome){
    let item = JSON.parse(localStorage.getItem(localStorageCarrinho) || "[]")

    item.push({
        name: nome
    });

    localStorage.setItem(localStorageCarrinho,JSON.stringify(item))
    displaycarrinho();
}

function abrecarrinho(){
    document.getElementById('prodcarrinho').style.width = '200px'
    document.getElementById('prodcarrinho').style.height = '400px'
    document.getElementById('prodcarrinho').style.color = '#111'
}
function closecarrinho(){
    document.getElementById('prodcarrinho').style.width = '0px'
    document.getElementById('prodcarrinho').style.height = '0px'
    document.getElementById('prodcarrinho').style.color = 'transparent'
}

function sendcarrinho(){
    let produtos = JSON.parse(localStorage.getItem(localStorageCarrinho) || "[]")
    localStorage.setItem(localStorageCarrinho,JSON.stringify(produtos))
    carrinho = ''
    for(j=0;j != produtos.length;j++){
        carrinho+= `${produtos[j]['name']}%0A`
    }
    textopadrao = `Bom dia, eu me interessei nos produtos:%0A${carrinho} e gostaria de fazer um orçamento.`
    window.open(` https://wa.me/553197486420?text=${textopadrao}`, '_blank');
}


function search(value){
    creury = document.querySelectorAll('.searched')
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

function filtroProhair(){
    var proHairElements = document.querySelectorAll('.ProHair');
    var nuanceElements = document.querySelectorAll('.Nuance');
    var fluenceElements = document.querySelectorAll('.Fluence');
    var BuranaElements = document.querySelectorAll('.Burana');

    if (BuranaElements.length > 0) {
        for (var i = 0; i < BuranaElements.length; i++) {
            BuranaElements[i].style.display = 'none';
        }
    }
    if (proHairElements.length > 0) {
        for (var i = 0; i < proHairElements.length; i++) {
            proHairElements[i].style.display = 'block';
        }
    }
    if (fluenceElements.length > 0) {
        for (var i = 0; i < fluenceElements.length; i++) {
            fluenceElements[i].style.display = 'none';
        }
    }

    if (nuanceElements.length > 0) {
        for (var i = 0; i < nuanceElements.length; i++) {
            nuanceElements[i].style.display = 'none';
        }
    }
    document.getElementById('fluence_bt').style.border = 'none'
    document.getElementById('pro_hair').style.border = '1px var(--color-primary) solid'
    document.getElementById('nuance_bt').style.border = 'none'
    document.getElementById('Burana_bt').style.border = 'none'
}

function filtroFluence(){
    var proHairElements = document.querySelectorAll('.ProHair');
    var nuanceElements = document.querySelectorAll('.Nuance');
    var fluenceElements = document.querySelectorAll('.Fluence');
    var BuranaElements = document.querySelectorAll('.Burana');

    if (BuranaElements.length > 0) {
        for (var i = 0; i < BuranaElements.length; i++) {
            BuranaElements[i].style.display = 'none';
        }
    }
    if (fluenceElements.length > 0) {
        for (var i = 0; i < fluenceElements.length; i++) {
            fluenceElements[i].style.display = 'block';
        }
    }

    if (nuanceElements.length > 0) {
        for (var i = 0; i < nuanceElements.length; i++) {
            nuanceElements[i].style.display = 'none';
        }
    }
    if (proHairElements.length > 0) {
        for (var i = 0; i < proHairElements.length; i++) {
            proHairElements[i].style.display = 'none';
        }
    }
    
    document.getElementById('fluence_bt').style.border = '1px var(--color-primary) solid'
    document.getElementById('nuance_bt').style.border = 'none'
    document.getElementById('pro_hair').style.border = 'none'
    document.getElementById('Burana_bt').style.border = 'none'
}

function filtroNuance(){
    var proHairElements = document.querySelectorAll('.ProHair');
    var nuanceElements = document.querySelectorAll('.Nuance');
    var fluenceElements = document.querySelectorAll('.Fluence');
    var BuranaElements = document.querySelectorAll('.Burana');

    if (BuranaElements.length > 0) {
        for (var i = 0; i < BuranaElements.length; i++) {
            BuranaElements[i].style.display = 'none';
        }
    }
    if (proHairElements.length > 0) {
        for (var i = 0; i < proHairElements.length; i++) {
            proHairElements[i].style.display = 'none';
        }
    }

    if (nuanceElements.length > 0) {
        for (var i = 0; i < nuanceElements.length; i++) {
            nuanceElements[i].style.display = 'block';
        }
    }
    if (fluenceElements.length > 0) {
        for (var i = 0; i < fluenceElements.length; i++) {
            fluenceElements[i].style.display = 'none';
        }
    }
    document.getElementById('pro_hair').style.border = 'none'
    document.getElementById('nuance_bt').style.border = '1px var(--color-primary) solid'
    document.getElementById('fluence_bt').style.border = 'none'
    document.getElementById('Burana_bt').style.border = 'none'
}

function filtroBurana(){
    var proHairElements = document.querySelectorAll('.ProHair');
    var nuanceElements = document.querySelectorAll('.Nuance');
    var fluenceElements = document.querySelectorAll('.Fluence');
    var BuranaElements = document.querySelectorAll('.Burana');

    
    if (BuranaElements.length > 0) {
        for (var i = 0; i < BuranaElements.length; i++) {
            BuranaElements[i].style.display = 'block';
        }
    }
    if (proHairElements.length > 0) {
        for (var i = 0; i < proHairElements.length; i++) {
            proHairElements[i].style.display = 'none';
        }
    }

    if (nuanceElements.length > 0) {
        for (var i = 0; i < nuanceElements.length; i++) {
            nuanceElements[i].style.display = 'none';
        }
    }
    if (fluenceElements.length > 0) {
        for (var i = 0; i < fluenceElements.length; i++) {
            fluenceElements[i].style.display = 'none';
        }
    }
    document.getElementById('pro_hair').style.border = 'none'
    document.getElementById('Burana_bt').style.border = '1px var(--color-primary) solid'
    document.getElementById('fluence_bt').style.border = 'none'
    document.getElementById('nuance_bt').style.border = 'none'
}

function displaydesc(id){
    index = id + '_d'
    document.getElementById(index).style.display = 'flex'
    document.getElementById(id).style.width = '100%'
    
}
function closeitem(id){
    index = id + '_d'
    document.getElementById(index).style.display = 'none'
    document.getElementById(id).style.width = 'fit-content'
}
