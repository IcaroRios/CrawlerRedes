const puppeteer = require('puppeteer');
const cheerio = require('cheerio');
const ora = require('ora');

const escapeXpathString = str => {
    const splitedQuotes = str.replace(/'/g, `', "'", '`);
    return `concat('${splitedQuotes}', '')`;
};

const clickByText = async (page,element, text) => {
    const escapedText = escapeXpathString(text);
    const linkHandlers = await page.$x(`//${element}[contains(text(), ${escapedText})]`);
    
    if (linkHandlers.length > 0) {
      await linkHandlers[0].click();
    } else {
      throw new Error('não Encontrado: ${text}');
    }
};

const rodarCrawler = async() => {
    console.log('aaa');
    const chromeOptions = { 
        args: ['--no-sandbox'],
        headless: false,  // FALSE MOSTRA A TELA, TRUE NÃO MOSTRA
        defaultViewport: null, 
        slowMo: 10,
    };

    const browser = await puppeteer.launch(chromeOptions);//({headless: false}); 
    const page = await browser.newPage();

    // await page.setViewport({ width: 1080, height: 720 });
    await page.goto('https://www.buscape.com.br/geladeira?resultsperpage=200&unavailable=0&resultorder=2');
    await page.close();
    await browser.close();

    return { 'result': 1 };

    // await clickByText(page,'label', 'Renavam');

    // const selector = '#renavam';
    // await page.waitForSelector(selector);
    // // await page.type(selector, renavam);

    // try {
    //     console.log('clicado no botao pesquisar')
    //     await clickByText(page, 'button','Pesquisar')

    //     //buscar msg de erro
    //     await page.waitFor(3000);
    //     // se desse para colocar timeout no esperando pela situaçaoVeiculo seria bom seria bom
    //     // await page.waitFor(() => !!document.querySelector("#situaçãoVeiculo > script")); 
    //     let bodyHTML = await page.evaluate(() => document.body.innerHTML);
    //     let $ = await cheerio.load(bodyHTML);// permite manipular como jquery
    //     const erroMsg = $('.alert, .alert-danger , .alert-dismissible , .fade').eq(9).find('#erroMsg').text();
    //     if( erroMsg != ''){ 
    //         return {
    //             status:0,
    //             erro: erroMsg
    //         };
    //     }

    // } catch (error) {
    //     return {
    //         status:0,
    //         erro: error
    //     };
    // }

    // try {
    //     // await clickByText(page, 'button','Mostar');
    //     console.log('pegando multas')
    //     const buttonsMostrarMultas = await page.$x('//*[@id="sectionBusca"]/div/div/div[5]/div/p[2]/button');
    
    //     if (buttonsMostrarMultas.length > 0) {
    //         await buttonsMostrarMultas[0].click();
    //         await page.waitFor(() => !!document.querySelector('#impressaoForm'));
    //     } 
    // } catch (error) {
    //     console.log('não tem multas ')
    // }
    // // await page.screenshot({ path: 'fotos/informacoes2.png' ,fullPage: true});// tempo suficiente para carregar as multas :/...
    // bodyHTML = await page.evaluate(() => document.body.innerHTML);

    // $ = await cheerio.load(bodyHTML);// permite manipular como jquery

    // let debitos =  [];
    // $('.results-row').each(function(index){ // PEGANDO AS INFORMAÇÕES GERAIS
    //     if(index < 6 ){//ultima linha é a das multas que só tem 2 colunas
    //         const descricao = $(this).children('.results-row td:nth-child('+1+')').text();
    //         const valor     = $(this).children('.results-row td:nth-child('+5+')').text().replace(/[^0-9|,]/g, "").replace(',', ".");
    //         if(valor != '0.00' && valor != '0.0000')
    //             debitos.push([descricao,valor]);
    //     }
    // });
    
    // // / PEGANDO AS MULTAS A PAGAR
    // $('#impressaoForm').find('tbody').eq(0).find('tr').each(function(){
    //         const descricao =  $(this).children('tr td:nth-child('+2+')').text();
    //         const valor     =  $(this).children('tr td:nth-child('+6+')').text().replace(/[^0-9|,]/g, "").replace(',', ".");
    //         debitos.push([descricao,valor]);
    // });

    // // removendo caracteres especiais
    // // valor total a pagar
    // valorTotal = await page.evaluate(() => 
    //     document.querySelector("#list > tfoot > tr > th:nth-child(5)").textContent.replace(',', ".")
    // );
    // //------------PARANDO CRAWLER------------
    // await page.close();
    // await browser.close();
    // //------------VALORES CONSEGUIDOS---------------// 
    // return {
    //     status:1,
    //     debitos:debitos,
    //     total:valorTotal,
    //     renavam:renavam
    // };
};

console.log(rodarCrawler());
