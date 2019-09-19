var gplay = require('google-play-scraper');
const fs = require('fs');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

function adicionaAplicativoCategoria(array, app, categoria) {     
    array.forEach(element => {
        element.aplicativo = app;
        element.categoria = categoria;
    });
}

function filtraJson(jsonObj, i) {
    var str = 'Photomath';
    jsonObj.aplicativo = 'Photomath';
    jsonObj.categoria = 'Ação';
    adicionaAplicativoCategoria(jsonObj, 'Photomath', 'Education');
    const csvWriter = createCsvWriter({
        path: str.concat(i, '.csv'),
        header: [
            { id: 'userName', title: 'USUARIO' },
            { id: 'text', title: 'COMENTARIO' },
            { id: 'date', title: 'DATACOMENTARIO' },
            { id: 'aplicativo', title: 'APLICATIVO' },
            { id: 'categoria', title: 'CATEGORIA' }
        ]
    });
    csvWriter.writeRecords(jsonObj)       // returns a promise
        .then(() => {
            console.log('...Done');
        });
}
function coletadorDeComentarios(i) {
    gplay.reviews({
        appId: 'com.microblink.photomath',
        page: i,
        lang: 'en'
    }).then(function (comentarios) { filtraJson(comentarios, i) }, console.log);
}

function rodaNvezes(n) {
    for (var i = 0; i < n; i++) {
        coletadorDeComentarios(i);
    }
}
rodaNvezes(20);


