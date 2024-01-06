localStorageCarrinho = 'Carrinho'

document.getElementById('downloadExcel').addEventListener('click', function() {
    // Substitua 'caminho/para/sua/planilha.xlsx' pelo caminho real do seu arquivo Excel
    var planilhaUrl = '/static/archives/Nuance.xlsx';
    downloadFile(planilhaUrl);
});

document.getElementById('downloadPDF').addEventListener('click', function() {
    // Substitua 'caminho/para/seu/arquivo.pdf' pelo caminho real do seu arquivo PDF
    var pdfUrl = '/static/archives/Prohair.pdf';
    downloadFile(pdfUrl);
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




function send(name,value){
    textopadrao = `Bom dia, eu me interessei no produto ${name}, no valor de R$${value} e gostaria de fazer um orçamento.`
    window.open(` https://wa.me/553197486420?text=${textopadrao}`, '_blank');
}
function inserecarrinho(nome, valor){
    let item = JSON.parse(localStorage.getItem(localStorageCarrinho) || "[]")

    item.push({
        name: nome,
        value: valor
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
        carrinho+= `${produtos[j]['name']} - R$${produtos[j]['value']}%0A`
    }
    textopadrao = `Bom dia, eu me interessei nos produtos:%0A${carrinho}no valor total de ${document.getElementById('total').innerHTML} e gostaria de fazer um orçamento.`
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

    if (proHairElements.length > 0) {
        for (var i = 0; i < proHairElements.length; i++) {
            proHairElements[i].style.display = 'block';
        }
    }

    if (nuanceElements.length > 0) {
        for (var i = 0; i < nuanceElements.length; i++) {
            nuanceElements[i].style.display = 'none';
        }
    }
    document.getElementById('pro_hair').style.border = '2px green solid'
    document.getElementById('nuance_bt').style.border = 'none'
}

function filtroNuance(){
    var proHairElements = document.querySelectorAll('.ProHair');
    var nuanceElements = document.querySelectorAll('.Nuance');

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
    document.getElementById('pro_hair').style.border = 'none'
    document.getElementById('nuance_bt').style.border = '2px green solid'
}

function limparfiltro(){
    var proHairElements = document.querySelectorAll('.ProHair');
    var nuanceElements = document.querySelectorAll('.Nuance');

    if (proHairElements.length > 0) {
        for (var i = 0; i < proHairElements.length; i++) {
            proHairElements[i].style.display = 'block';
        }
    }

    if (nuanceElements.length > 0) {
        for (var i = 0; i < nuanceElements.length; i++) {
            nuanceElements[i].style.display = 'block';
        }
    }
    document.getElementById('pro_hair').style.border = 'none'
    document.getElementById('nuance_bt').style.border = 'none'
}