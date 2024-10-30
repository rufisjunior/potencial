
let vehicle;
let tipoSeguro;
let uso;
let menor25;
let condutorEMesmo;
let garagem;
let garagemTrabalho = '3'; //não uso para trabalhar
let utilizacao = '1'; //particular
let relacaoConductor = 6 //OUTRO
let relacaoSegurado;
let seguradora;
let placaEntrada;


function formatPlate(input) {
    let placa = input.value.replace(/[^a-zA-Z0-9]/g, '');

    if (placa.length > 3) {
        placa = placa.substring(0, 3) + '-' + placa.substring(3, 7);
    }

    input.value = placa;
};

function formatData(input){
    let data = input.value;

    if( data.length == 2){
        data = data.substring(0, 2) + '/';
    }
    else if(data.length == 5){
        data = data.substring(0, 7) + '/';
    }

    input.value = data;
}

function formatCep(input){
   let cep = input.value;

   if (cep.length == 5){
    cep = cep.substring(0, 5) + '-';
   }
   input.value = cep;
}

function formatTelefone(input){

    let telefoneFormatada;
    let telefone = input.value;

    if(telefone.length >= 11) {
        telefoneFormatada = telefone.replace(/(\d{2})(\d{5})(\d{4})/,
                        function( regex, arg1, arg2, arg3) {
                        return '(' + arg1 + ')' + ' ' + arg2 + '-' + arg3;
                        });
        input.value = telefoneFormatada;
    }else if(telefone.length === 10){
        telefoneFormatada = telefone.replace(/(\d{2})(\d{4})(\d{4})/,
                        function( regex, arg1, arg2, arg3) {
                        return '(' + arg1 + ')' + ' ' + arg2 + '-' + arg3;
                        });
        input.value = telefoneFormatada;
    }
}

async function validaCPF(input){

    var cpf= input.value; 
    var cpfValido = /^(([0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}))$/;     
    if (cpfValido.test(cpf) == false)    { 
         
       cpf = cpf.replace( /\D/g , ""); 
                
       if (cpf.length==11){
          const person = await getPerson(cpf);

          if(person.cpf != undefined){
            document.getElementById('seguradoNome').value = person.nome;
            document.getElementById('seguradoDataNascimento').value = person.data_nascimento;
          }

          cpf = cpf.replace( /(\d{3})(\d)/ , "$1.$2"); 
          cpf = cpf.replace( /(\d{3})(\d)/ , "$1.$2"); 
          cpf = cpf.replace( /(\d{3})(\d{1,2})$/ , "$1-$2");
                    
           input.value = cpf;
        }
    }
}

async function getPerson(cpf){

    const person = {
        cpf: cpf,
        typePerson:"1" //fisica
    }

    const result = await fetch('/person', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(person)
    });

    const response = await result.json()

    return response;
}


async function buscarPlaca() {
    const placaVeiculo = document.getElementById('inputPlaca').value;
    const placa = placaVeiculo.replace(/[^\w\s]/gi, '');

    placaEntrada = placa;

    vehicle = await getVehicle(placa);

    
    if(vehicle.DESCRICAO === undefined){
        Mudarestado('divEmail','divPlaca');
    }

    document.getElementById('lblCarro').innerText = vehicle.DESCRICAO;
    document.getElementById('lblAnoMod').innerText = vehicle.ANOMODELO;

    Mudarestado('divDadosCarro','')
};


async function getVehicle(placa) {
    const apiUrl ='/vehicle/auto-complete/placa?placa=' + encodeURIComponent(placa);

    const result = await fetch(apiUrl)
        .then(response => response.json())
        .then(data => {

            return  data;
        })
        .catch(error => {
            return null;
    });

    return result;
}

async function getAdress(cep) {

    const apiUrl ='/address/cep?cep=' + encodeURIComponent(cep);

    const result = await fetch(apiUrl)
        .then(response => response.json())
        .then(data => {

            return  data;
        })

    return result;
}

function setTipoSeguro(value){
tipoSeguro = value;
}

function setUso(value){
    uso = value;

    if(value == 2){
        garagemTrabalho = '5'
    }

    if(value == 4){
        utilizacao = '3';
    }

}

function setMenor25(value){
    menor25 = value;
}

function setCondutor(value){
    condutorEMesmo = value
}


// document.addEventListener('click', function(e) {
//     debugger;
//         if (e.target.id === "divSeguradora") {
//           seguradora = e.target.firstChild.textContent;
//         }
// });

async function buscarCep(){

    const cep = document.getElementById('inputCep').value;
   
    //const address = await getAdress(cep);
}


async function tracking(){
    
    const nomeSegurado = document.getElementById('seguradoNome').value;
    const email = document.getElementById('email').value;
    const telefoneEntrada = document.getElementById('telefone').value;
    const telefonePuro = telefoneEntrada.replace(/[^\w\s]/gi, '');


    const data = {
        name: nomeSegurado,
        email: email,
        phone: telefonePuro.replace(' ', '')
    }

    const result = await fetch('/tracking', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const response = await result.json()

    return response;
}


 async function submit(){

    const cep = document.getElementById('inputCep').value.replace('-', '');
    const cpfsegurado = document.getElementById('SeguradoCpf').value;
    const nomeSegurado = document.getElementById('seguradoNome').value;
    const email = document.getElementById('email').value;
    const telefoneEntrada = document.getElementById('telefone').value;
    const telefonePuro = telefoneEntrada.replace(/[^\w\s]/gi, '');
    const ddd = telefonePuro.substring(0,2);
    const telefone = telefonePuro.replace(' ', '').substring(2,11);

    const dataNascimento = document.getElementById('seguradoDataNascimento').value;

    const veiculoZeroKm = document.getElementById('zeroKm').value.checked === true? "1": "0";

    const estadoCivil = document.getElementById('estadoCivil');
    const estadocivil = estadoCivil.options[estadoCivil.selectedIndex].value;
    const sexo = document.getElementById('sexo');
    const seguradoSexo = sexo.options[sexo.selectedIndex].value;

    const tipoResidencia = document.getElementById('tipoResidencia');
    const residencia = tipoResidencia.options[tipoResidencia.selectedIndex].value;
    const codigoPromocao = document.getElementById('codigoPromocao').value;


    switch(residencia)
    {
        case '1':
            garagem = '1';
            break;
        case '2':
            garagem = '3';
            break;
        case '3':
            garagem = '3';
            break;
        default:
            garagem = '1'
    }
    
    let condutorNome;
    let condutorCpf;
    let condutorNascimento;
    let condutorSexo;
    let condutorEstadoCivil;

    if(condutorEMesmo === 1){
        condutorNome = nomeSegurado;
        condutorCpf = cpfsegurado;
        condutorNascimento = dataNascimento;
        condutorEstadoCivil = estadocivil
        condutorSexo = seguradoSexo
        relacaoConductor = '1' //proprio
        relacaoSegurado = '7'

    }
    else{
        condutorNome = document.getElementById('CondutorNome').value;;
        condutorCpf = document.getElementById('CondutorCpf').value;;
        condutorNascimento = document.getElementById('CondutorDataNascimento').value;

        const estadoCivil = document.getElementById('estadoCivilCondutor');
        const estadocivil = estadoCivil.options[estadoCivil.selectedIndex].value;
        const sexo = document.getElementById('sexoCondutor');
        const condutorsexo = sexo.options[sexo.selectedIndex].value;

        condutorEstadoCivil = estadocivil;
        condutorSexo = condutorsexo;
    }


    let pessoaFisica = "F";

    if(cpfsegurado.length > 14){
        pessoaFisica = "J"
    }

    const cambioAuto = vehicle.CAMBIOAUTO === true? "1": "0"


    const calculo = 
    {
        COTACAO: {
          TIPOSEG: tipoSeguro,
          SEGURADO: {
            NOMESEG: nomeSegurado,
            PESSOASEG: pessoaFisica,
            CGCSEG: cpfsegurado,
            NASCSEG: dataNascimento,
            SEXOSEG: seguradoSexo,
            ESTCIVILSEG: estadocivil,
            EMAILPES: email,
            DDDCEL: ddd,
            CEL: telefone,
            RELAPROPR: relacaoSegurado,
            CONTATO: codigoPromocao
          },
          PROPRIETARIO: {
            NOMEPROP: nomeSegurado,
            PESSOAPROP: pessoaFisica,
            CGCPROP: cpfsegurado,
            SEXOPROP: seguradoSexo,
            ESTCIVILPROP: estadocivil,
            NASCPROP: dataNascimento
          },
          CONDUTORP: {
            CPFCOND: condutorCpf,
            NOMECOND: condutorNome,
            SEXOCOND: condutorSexo,
            NASCCOND: condutorNascimento,
            ESTCIVILCOND: condutorEstadoCivil,
            RESIDEEM: residencia,
            RELASEG: relacaoConductor,
            CONDS17A25: {
                EXISTE17A25:menor25
            }
          },
          VEICULO: {
            CODCAR:  vehicle.CODCAR ?? 1,
            MARCA: vehicle.MARCA ?? null,
            ANOFABR: vehicle.ANOFABR ?? 0,
            ANOMODELO: vehicle.ANOMODELO ?? 1,
            COMBUSTIVEL: vehicle.COMBUSTIVEL ?? 1,
            CHASSI: vehicle.CHASSI ?? null,
            ZEROKM: veiculoZeroKm,
            UTILIZACAO: utilizacao,
            PERFILUSOVEIC: {
              USO:uso
            },
            CEPPERNOITE: cep,
            CEPCIRC: cep,
            CEPRESID: cep,
            PLACANUM: placaEntrada,
            CAMBIOAUTO: cambioAuto,
            GARAGRESID: garagem,
            GARAGTRAB: garagemTrabalho,
            LOCALPERNOITE: 20 //Residência como padrão 
          }
        }
    };

    const result = await fetch('/cotar', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(calculo)
    });

    return result.json()
}


function Mudarestado(el, el2) {
    var display = document.getElementById(el);
    var display2 = document.getElementById(el2);
    display.classList.toggle("hide");

    if (el2 != '') {
        display2.classList.toggle("hide");
    }
}