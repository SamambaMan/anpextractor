# -*- coding: utf-8 -*-
import pytest

@pytest.fixture
def stations_list():
    return """
<HTML>
<head>
	<title>:: ANP - Agência Nacional de Petróleo ::</title>
	<link rel="STYLESHEET" type="text/css" href="/css/default.css">
	<meta http-equiv=pragma content=no-cache><meta http-equiv=expires content="Mon, 06 Jan 1990 00:00:01 GMT">
	<META http-equiv=Content-Type content="text/html; charset=iso-8859-1">
</head>
<style type="text/css">
	@import "/SITE/extras/css/default.css";
</style>

<body leftmargin=0 topmargin=0 marginheight="0" marginwidth="0" bgcolor="#ffffff">
<!-- tabela moldura principal -->
<table width="740" border="0" cellspacing="3" cellpadding="0">
<tr>
<td width="126" height="100%" bgcolor="#D7D7D7" valign="top">
<script language="JAVASCRIPT">

    function Submeter()
    {
		if (ValidaFormulario())
		{
		document.frmPesquisa.hPesquisar.value  = "PESQUISAR";
		document.frmPesquisa.submit();
		}
    }

	function jogaform(pcod_inst)
	{
		document.frmResultado.Cod_inst.value = pcod_inst;
		document.frmResultado.estado.value = document.frmPesquisa.sEstado.value;
		document.frmResultado.municipio.value = document.frmPesquisa.sMunicipio.value;
		document.frmResultado.submit();
	}

    function limpaCnpj() 
    {
        document.frmPesquisa.sCnpj.value = ""
    }
    function VerificaEstado() 
    {
        if (document.frmPesquisa.sEstado.selectedIndex == 0) {
            alert('Informe o Estado.')
            document.frmPesquisa.sEstado.focus()
            document.frmPesquisa.sMunicipio.selectedIndex = 0
            return false
        }
        document.frmPesquisa.sCnpj.value = ""
    }

    function limpaRazaoSocial() 
    {
        document.frmPesquisa.sRazaoSocial.value = ""
        document.frmPesquisa.sEstado.selectedIndex = 0
        document.frmPesquisa.sMunicipio.selectedIndex = 0
        document.frmPesquisa.sMunicipio.length = 1
        document.frmPesquisa.sBandeira.selectedIndex = 0
        document.frmPesquisa.sBandeira.value = 0
        document.frmPesquisa.sProduto.selectedIndex = 0
        document.frmPesquisa.sProduto.value = 0
        document.frmPesquisa.sTipodePosto.selectedIndex = 0
        document.frmPesquisa.sTipodePosto.value = 0
    }

    function ValidaFormulario() 
    {
        if ((document.frmPesquisa.sCnpj.value == "") &&
            (document.frmPesquisa.sRazaoSocial.value == "") &&
            (document.frmPesquisa.sEstado.options[document.frmPesquisa.sEstado.selectedIndex].value == 0) && 
            (document.frmPesquisa.sMunicipio.options[document.frmPesquisa.sMunicipio.selectedIndex].value == 0) &&
            (document.frmPesquisa.sBandeira.options[document.frmPesquisa.sBandeira.selectedIndex].value == 0) &&
            (document.frmPesquisa.sProduto.options[document.frmPesquisa.sProduto.selectedIndex].value == 0)) 
        {
            alert('Informar ao menos mais de um campo para pesquisa.' )
            return false
        }
        else
        {
            return true
        }

        if (document.frmPesquisa.sCnpj.value.length > 0) 
        {
            return VerificaCnpj()
        } 
        else if (document.frmPesquisa.sRazaoSocial.value.length > 0) 
        {
            return VerificaNome()
        }
    }

    function VerificaNome() 
    {
        for (i = 0; i <= document.frmPesquisa.sRazaoSocial.value.length; i++) 
        {
            if ("0123456789aAbBcCdDEefFgGHhIiJjkKlLMmNnOoPpQqRrSsTtUuVvxXYyZz".indexOf(document.frmPesquisa.sRazaoSocial.value.charAt(i)) == -1) {
				alert('Caracter Inválido no campo Nome!!!!!!!!!')
				return false
            } 
            else 
            {
				return true
            }
        }
    }

    function VerificaCnpj() 
    {
        var ls_cnpj
        var lsDigitoCnpj
        ls_cnpj = LimpaValor(document.frmPesquisa.sCnpj.value)

        if ((ls_cnpj.length != 14) && (ls_cnpj.length != 11)) 
        {
            alert('CNPJ/CPF inválido!')
            document.frmPesquisa.sCnpj.focus()
            return false
        }
        lsDigitoCnpj = DigitoCnpj(ls_cnpj.substring(0, 12))
        if (lsDigitoCnpj != ls_cnpj.substring(12, 14)) 
        {
            alert('CNPJ inválido!')
            document.frmPesquisa.sCnpj.focus()
            return false
        }
        document.frmPesquisa.sCnpj.value = ls_cnpj
        return true
    }

    function DigitoCnpj(as_cgc) 
    {
        var li_Multi = new Array(13)
        li_Multi[0] = 2
        li_Multi[1] = 3
        li_Multi[2] = 4
        li_Multi[3] = 5
        li_Multi[4] = 6
        li_Multi[5] = 7
        li_Multi[6] = 8
        li_Multi[7] = 9
        li_Multi[8] = 2
        li_Multi[9] = 3
        li_Multi[10] = 4
        li_Multi[11] = 5
        li_Multi[12] = 6

        // Reseta contadores
        li_sum = 0
        ls_CGC = as_cgc

        // Se nao tiver doze caracteres nao e CGC
        if (as_cgc.length == 12) 
        {
            // Calcula o primeiro digito(fazendo 11 - Mod11 da somatoria do produtorio)
            for (i = 0; i < 12; i++) 
            {
                li_sum += parseInt(ls_CGC.substring(ls_CGC.length - 1, ls_CGC.length)) * li_Multi[i]
                ls_CGC = ls_CGC.substring(0, ls_CGC.length - 1)
            }

            // Se o Mod for maior que 9(10 ou 11), retornara 0
            ls_First = String(11 - (li_sum % 11))
            if (ls_First.length > 1) 
            {
                ls_First = '0'
            }

            li_sum = 0
            ls_CGC = as_cgc + ls_First

            // Calcula o segundo digito do CGC que agora tem 13 caracteres(CGC + 1. digito)
            for (i = 0; i < 13; i++) 
            {
                li_sum += parseInt(ls_CGC.substring(ls_CGC.length-1, ls_CGC.length)) * li_Multi[i]
                ls_CGC = ls_CGC.substring(0, ls_CGC.length - 1)
            }

            ls_Second = String(11 - (li_sum % 11))
            // Se o Mod for maior que 9(10 ou 11), retornara 0
            if (ls_Second.length > 1) 
            {
                ls_Second = '0'
            }

            // Retorna os dois digitos
            return ls_First + ls_Second
        } 
        else 
        {
            return ''
        }
    }

    function FormataCnpj(campo,tammax,teclapres) 
    {
        var tecla = teclapres.keyCode;
        vr = LimpaValor(campo.value);
        tam = vr.length;

        if (tam < tammax && tecla != 8){ tam = vr.length + 1 ; }

        if (tecla == 8 ){	tam = tam - 1 ; }

        if ( tecla == 8 || tecla >= 48 && tecla <= 57 || tecla >= 96 && tecla <= 105 )
        {
            if ( tam <= 2 ){
                campo.value = vr ; }
            if ( (tam > 2) && (tam <= 6) ){
                campo.value = vr.substr( 0, tam - 2 ) + '-' + vr.substr( tam - 2, tam ) ; }
            if ( (tam >= 7) && (tam <= 9) ){
                campo.value = vr.substr( 0, tam - 6 ) + '/' + vr.substr( tam - 6, 4 ) + '-' + vr.substr( tam - 2, tam ) ; }
            if ( (tam >= 10) && (tam <= 12) ){
                campo.value = vr.substr( 0, tam - 9 ) + '.' + vr.substr( tam - 9, 3 ) + '/' + vr.substr( tam - 6, 4 ) + '-' + vr.substr( tam - 2, tam ) ; }
            if ( (tam >= 13) && (tam <= 14) ){
                campo.value = vr.substr( 0, tam - 12 ) + '.' + vr.substr( tam - 12, 3 ) + '.' + vr.substr( tam - 9, 3 ) + '/' + vr.substr( tam - 6, 4 ) + '-' + vr.substr( tam - 2, tam ) ; }
            if ( (tam >= 15) && (tam <= 17) ){
                campo.value = vr.substr( 0, tam - 14 ) + '.' + vr.substr( tam - 14, 3 ) + '.' + vr.substr( tam - 11, 3 ) + '.' + vr.substr( tam - 8, 3 ) + '.' + vr.substr( tam - 5, 3 ) + '-' + vr.substr( tam - 2, tam ) ;}
        }
    }

    function FormataCnpjNs() 
    {
        vr = LimpaValor(document.frmPesquisa.sCnpj.value)
        if (vr.length == 14) 
        {
            document.frmPesquisa.sCnpj.value = vr.substr(0, 2) + "." + vr.substr(2, 3) + "." + vr.substr(5, 3) + "/" + vr.substr(8, 4) + "-" + vr.substr(12, 2)
        }
    }

    function LimpaValor(asValor) 
    {
        var vr
        vr = ""
        for (i = 0; i <= asValor.length; i++) 
        {
            if ("0123456789 ".indexOf(asValor.charAt(i)) != -1) 
            {
               vr += asValor.charAt(i)
            }
        }
        return vr
    }

    function selecionaEstado() 
    {
        document.frmPesquisa.submit();
        //document.location.href = "consulta.asp?sPesquisar=1&sRazaoSocial=" + document.frmPesquisa.sRazaoSocial.value + "&sEstado=" + document.frmPesquisa.sEstado.options[document.frmPesquisa.sEstado.selectedIndex].value + "&sBandeira=" + document.frmPesquisa.sBandeira.options[document.frmPesquisa.sBandeira.selectedIndex].value + "&sProduto=" + document.frmPesquisa.sProduto.options[document.frmPesquisa.sProduto.selectedIndex].value + "&sTipodePosto=" + document.frmPesquisa.sTipodePosto.options[document.frmPesquisa.sTipodePosto.selectedIndex].value
    }
    
</script>
<script language="JAVASCRIPT">

function ShowHours() 
{
	TodaysHour = new Date()
	horas = TodaysHour.getHours()
	minutos = TodaysHour.getMinutes()
	segundos = TodaysHour.getSeconds()
	if (horas < 10)
		horas= "0" + horas

	if (minutos < 10)
		minutos = "0" + minutos

	if (segundos < 10)
		segundos = "0" + segundos

    document.write(horas+":"+minutos+":"+segundos)
}

function ShowTodayDate() 
{
	now = new Date()
	dia = now.getDate()
	mes = now.getMonth() + 1
	ano = now.getYear()

	if (dia < 10)
		dia = "0" + dia
	
	if (mes < 10)
		mes = "0" + mes
	
	if (ano < 2000)
		ano = "19" + ano

        if (navigator.appName == "Netscape") 
        {
             if (ano > 1999)
                ano = "200" + (now.getYear()-100)
 	    }
        if (navigator.appName == "Netscape") 
        {
             if (ano > 2009)
	            ano = "20" + (now.getYear()-100)  
	    }

	document.write(dia+"/" +mes+ "/" +ano)
}
</script>
</td>
<td valign="left" width="628">
<!-- fim da tabela moldura principal e inicio do corpo do consulta de postos -->
<TABLE>
        <span class="txtcinza2"><b>Data: </b>26/10/2017&nbsp;&nbsp; <b>Hora:</b> 18:44:04</span>
</TABLE>
<table width="100%"  align="Top" border="0" bgcolor="E7E7E7">
          <td width="33%"></td>
          <td width="67%"><td>
       <!--height=352-->
<TABLE  height="100%" cols=2 width="97%" border=0>
    <table  border="0" align="top" cellspacing="1">
      <tr>
        <td width="97%"  align="top" bgcolor="E7E7E7">
		<form method="Post" action="consulta.asp" name="frmPesquisa" onSubmit="">
          <table  valign="top" border="0">
            <tr>
				<td colspan="2" class="titazulesc1"></td>
			</tr>
           <tr>
              <td align="right" valign="middle">
                <p align="right"><span class="txtcinza2b">CNPJ/CPF:</span></td>
					<td><input class=busca value="" tabindex=1 type="text" name="sCnpj" size="18" maxlength="14" >
                            <font face="Verdana" color="#666666" size="1"><b>
                            Digite apenas números. Ex: 99999999999999</b></font></td>

              <td></td>
            </tr>
            <tr>
              <td nowrap align="right"><span class="txtcinza2b">Nome do Posto:</span></td>
				<td><input class=busca value="" tabindex=2 type="text" name="sRazaoSocial" size="40">
				 </td>
              <td></td>
            </tr>
            <tr>
               <td nowrap align="right">
                  <span class="txtcinza2b">Estado:</span></td>
               <td nowrap>
                  <select name="sEstado" class="busca" onChange="selecionaEstado()">
                      <option value="0"></option>
					  <option value="AC">AC</option><option value="AL">AL</option><option value="AM">AM</option><option value="AP">AP</option><option value="BA">BA</option><option value="CE">CE</option><option value="DF">DF</option><option value="ES">ES</option><option value="GO">GO</option><option value="MA">MA</option><option value="MG">MG</option><option value="MS">MS</option><option value="MT">MT</option><option value="PA">PA</option><option value="PB">PB</option><option value="PE">PE</option><option value="PI">PI</option><option value="PR">PR</option><option value="RJ">RJ</option><option value="RN">RN</option><option value="RO">RO</option><option value="RR">RR</option><option value="RS">RS</option><option value="SC">SC</option><option value="SE">SE</option><option value="SP" selected>SP</option><option value="TO">TO</option>
                  </select>
                  <span class="txtcinza2b">Município:</span>
                  <select name="sMunicipio" class="busca" onChange="VerificaEstado()">
                      <option value="0" >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option>
					  
				<option value="8853">ADAMANTINA</option>
				
				<option value="8854">ADOLFO</option>
				
				<option value="8857">AGUAI</option>
				
				<option value="8858">AGUAS DA PRATA</option>
				
				<option value="8859">AGUAS DE LINDOIA</option>
				
				<option value="8860">AGUAS DE SANTA BARBARA</option>
				
				<option value="8861">AGUAS DE SAO PEDRO</option>
				
				<option value="8862">AGUDOS</option>
				
				<option value="8865">ALAMBARI</option>
				
				<option value="8870">ALFREDO MARCONDES</option>
				
				<option value="8871">ALTAIR</option>
				
				<option value="8872">ALTINOPOLIS</option>
				
				<option value="8873">ALTO ALEGRE</option>
				
				<option value="8875">ALUMINIO</option>
				
				<option value="8876">ALVARES FLORENCE</option>
				
				<option value="8877">ALVARES MACHADO</option>
				
				<option value="8878">ALVARO DE CARVALHO</option>
				
				<option value="8879">ALVINLANDIA</option>
				
				<option value="8883">AMERICANA</option>
				
				<option value="8884">AMERICO BRASILIENSE</option>
				
				<option value="8885">AMERICO DE CAMPOS</option>
				
				<option value="8886">AMPARO</option>
				
				<option value="8888">ANALANDIA</option>
				
				<option value="8891">ANDRADINA</option>
				
				<option value="8892">ANGATUBA</option>
				
				<option value="8893">ANHEMBI</option>
				
				<option value="8894">ANHUMAS</option>
				
				<option value="8896">APARECIDA</option>
				
				<option value="8897">APARECIDA D'OESTE</option>
				
				<option value="8901">APIAI</option>
				
				<option value="8906">ARACARIGUAMA</option>
				
				<option value="8907">ARACATUBA</option>
				
				<option value="8908">ARACOIABA DA SERRA</option>
				
				<option value="8909">ARAMINA</option>
				
				<option value="8910">ARANDU</option>
				
				<option value="8911">ARAPEI</option>
				
				<option value="8912">ARARAQUARA</option>
				
				<option value="8913">ARARAS</option>
				
				<option value="8916">ARCO-IRIS</option>
				
				<option value="8917">AREALVA</option>
				
				<option value="8918">AREIAS</option>
				
				<option value="8919">AREIOPOLIS</option>
				
				<option value="8920">ARIRANHA</option>
				
				<option value="8923">ARTUR NOGUEIRA</option>
				
				<option value="8924">ARUJA</option>
				
				<option value="8925">ASPASIA</option>
				
				<option value="8926">ASSIS</option>
				
				<option value="8928">ATIBAIA</option>
				
				<option value="8930">AURIFLAMA</option>
				
				<option value="8931">AVAI</option>
				
				<option value="8932">AVANHANDAVA</option>
				
				<option value="8933">AVARE</option>
				
				<option value="8937">BADY BASSITT</option>
				
				<option value="8940">BALBINOS</option>
				
				<option value="8941">BALSAMO</option>
				
				<option value="8942">BANANAL</option>
				
				<option value="8945">BARAO DE ANTONINA</option>
				
				<option value="8947">BARBOSA</option>
				
				<option value="8948">BARIRI</option>
				
				<option value="8949">BARRA BONITA</option>
				
				<option value="8950">BARRA DO CHAPEU</option>
				
				<option value="8951">BARRA DO TURVO</option>
				
				<option value="8954">BARRETOS</option>
				
				<option value="8955">BARRINHA</option>
				
				<option value="8956">BARUERI</option>
				
				<option value="8957">BASTOS</option>
				
				<option value="8958">BATATAIS</option>
				
				<option value="8961">BAURU</option>
				
				<option value="8962">BEBEDOURO</option>
				
				<option value="8965">BENTO DE ABREU</option>
				
				<option value="8966">BERNARDINO DE CAMPOS</option>
				
				<option value="8967">BERTIOGA</option>
				
				<option value="8968">BILAC</option>
				
				<option value="8969">BIRIGUI</option>
				
				<option value="8970">BIRITIBA-MIRIM</option>
				
				<option value="8972">BOA ESPERANCA DO SUL</option>
				
				<option value="8975">BOCAINA</option>
				
				<option value="8976">BOFETE</option>
				
				<option value="8977">BOITUVA</option>
				
				<option value="8979">BOM JESUS DOS PERDOES</option>
				
				<option value="8981">BOM SUCESSO DE ITARARE</option>
				
				<option value="8983">BORA</option>
				
				<option value="8984">BORACEIA</option>
				
				<option value="8985">BORBOREMA</option>
				
				<option value="8986">BOREBI</option>
				
				<option value="8989">BOTUCATU</option>
				
				<option value="8992">BRAGANCA PAULISTA</option>
				
				<option value="8995">BRAUNA</option>
				
				<option value="8996">BREJO ALEGRE</option>
				
				<option value="8997">BRODOWSKI</option>
				
				<option value="8998">BROTAS</option>
				
				<option value="9000">BURI</option>
				
				<option value="9001">BURITAMA</option>
				
				<option value="9002">BURITIZAL</option>
				
				<option value="9003">CABRALIA PAULISTA</option>
				
				<option value="9004">CABREUVA</option>
				
				<option value="9005">CACAPAVA</option>
				
				<option value="9007">CACHOEIRA PAULISTA</option>
				
				<option value="9008">CACONDE</option>
				
				<option value="9009">CAFELANDIA</option>
				
				<option value="9011">CAIABU</option>
				
				<option value="9013">CAIEIRAS</option>
				
				<option value="9014">CAIUA</option>
				
				<option value="9015">CAJAMAR</option>
				
				<option value="9016">CAJATI</option>
				
				<option value="9017">CAJOBI</option>
				
				<option value="9018">CAJURU</option>
				
				<option value="9023">CAMPINA DO MONTE ALEGRE</option>
				
				<option value="9025">CAMPINAS</option>
				
				<option value="9026">CAMPO LIMPO PAULISTA</option>
				
				<option value="9028">CAMPOS DO JORDAO</option>
				
				<option value="9029">CAMPOS NOVOS PAULISTA</option>
				
				<option value="9030">CANANEIA</option>
				
				<option value="9031">CANAS</option>
				
				<option value="9033">CANDIDO MOTA</option>
				
				<option value="9034">CANDIDO RODRIGUES</option>
				
				<option value="9036">CANITAR</option>
				
				<option value="9037">CAPAO BONITO</option>
				
				<option value="9038">CAPELA DO ALTO</option>
				
				<option value="9039">CAPIVARI</option>
				
				<option value="9043">CARAGUATATUBA</option>
				
				<option value="9044">CARAPICUIBA</option>
				
				<option value="9046">CARDOSO</option>
				
				<option value="9049">CASA BRANCA</option>
				
				<option value="9050">CASSIA DOS COQUEIROS</option>
				
				<option value="9051">CASTILHO</option>
				
				<option value="9052">CATANDUVA</option>
				
				<option value="9053">CATIGUA</option>
				
				<option value="9056">CEDRAL</option>
				
				<option value="9057">CERQUEIRA CESAR</option>
				
				<option value="9058">CERQUILHO</option>
				
				<option value="9059">CESARIO LANGE</option>
				
				<option value="9061">CHARQUEADA</option>
				
				<option value="9062">CHAVANTES</option>
				
				<option value="9065">CLEMENTINA</option>
				
				<option value="9067">COLINA</option>
				
				<option value="9068">COLOMBIA</option>
				
				<option value="9070">CONCHAL</option>
				
				<option value="9071">CONCHAS</option>
				
				<option value="9072">CORDEIROPOLIS</option>
				
				<option value="9073">COROADOS</option>
				
				<option value="9075">CORONEL MACEDO</option>
				
				<option value="9078">CORUMBATAI</option>
				
				<option value="9079">COSMOPOLIS</option>
				
				<option value="9080">COSMORAMA</option>
				
				<option value="9082">COTIA</option>
				
				<option value="9083">CRAVINHOS</option>
				
				<option value="9084">CRISTAIS PAULISTA</option>
				
				<option value="9086">CRUZALIA</option>
				
				<option value="9087">CRUZEIRO</option>
				
				<option value="9088">CUBATAO</option>
				
				<option value="9090">CUNHA</option>
				
				<option value="9093">DESCALVADO</option>
				
				<option value="9094">DIADEMA</option>
				
				<option value="9095">DIRCE REIS</option>
				
				<option value="9097">DIVINOLANDIA</option>
				
				<option value="9098">DOBRADA</option>
				
				<option value="9099">DOIS CORREGOS</option>
				
				<option value="9100">DOLCINOPOLIS</option>
				
				<option value="9102">DOURADO</option>
				
				<option value="9103">DRACENA</option>
				
				<option value="9104">DUARTINA</option>
				
				<option value="9105">DUMONT</option>
				
				<option value="9107">ECHAPORA</option>
				
				<option value="9108">ELDORADO</option>
				
				<option value="9110">ELIAS FAUSTO</option>
				
				<option value="9111">ELISIARIO</option>
				
				<option value="9112">EMBAUBA</option>
				
				<option value="9113">EMBU DAS ARTES</option>
				
				<option value="9114">EMBU-GUACU</option>
				
				<option value="9115">EMILIANOPOLIS</option>
				
				<option value="9118">ENGENHEIRO COELHO</option>
				
				<option value="9124">ESPIRITO SANTO DO PINHAL</option>
				
				<option value="9125">ESPIRITO SANTO DO TURVO</option>
				
				<option value="9126">ESTIVA GERBI</option>
				
				<option value="9128">ESTRELA DO NORTE</option>
				
				<option value="9127">ESTRELA D'OESTE</option>
				
				<option value="9129">EUCLIDES DA CUNHA PAULISTA</option>
				
				<option value="9131">FARTURA</option>
				
				<option value="9135">FERNANDO PRESTES</option>
				
				<option value="9136">FERNANDOPOLIS</option>
				
				<option value="9137">FERNAO</option>
				
				<option value="9138">FERRAZ DE VASCONCELOS</option>
				
				<option value="9139">FLORA RICA</option>
				
				<option value="9140">FLOREAL</option>
				
				<option value="9142">FLORIDA PAULISTA</option>
				
				<option value="9143">FLORINIA</option>
				
				<option value="9144">FRANCA</option>
				
				<option value="9145">FRANCISCO MORATO</option>
				
				<option value="9146">FRANCO DA ROCHA</option>
				
				<option value="9148">GABRIEL MONTEIRO</option>
				
				<option value="9149">GALIA</option>
				
				<option value="9150">GARCA</option>
				
				<option value="9152">GASTAO VIDIGAL</option>
				
				<option value="9153">GAVIAO PEIXOTO</option>
				
				<option value="9154">GENERAL SALGADO</option>
				
				<option value="9155">GETULINA</option>
				
				<option value="9156">GLICERIO</option>
				
				<option value="9160">GUAICARA</option>
				
				<option value="9161">GUAIMBE</option>
				
				<option value="9162">GUAIRA</option>
				
				<option value="9164">GUAPIACU</option>
				
				<option value="9165">GUAPIARA</option>
				
				<option value="9167">GUARA</option>
				
				<option value="9168">GUARACAI</option>
				
				<option value="9169">GUARACI</option>
				
				<option value="9171">GUARANI D'OESTE</option>
				
				<option value="9172">GUARANTA</option>
				
				<option value="9175">GUARARAPES</option>
				
				<option value="9176">GUARAREMA</option>
				
				<option value="9177">GUARATINGUETA</option>
				
				<option value="9178">GUAREI</option>
				
				<option value="9179">GUARIBA</option>
				
				<option value="9182">GUARUJA</option>
				
				<option value="9183">GUARULHOS</option>
				
				<option value="9184">GUATAPARA</option>
				
				<option value="9185">GUZOLANDIA</option>
				
				<option value="9186">HERCULANDIA</option>
				
				<option value="9187">HOLAMBRA</option>
				
				<option value="9189">HORTOLANDIA</option>
				
				<option value="9190">IACANGA</option>
				
				<option value="9191">IACRI</option>
				
				<option value="9192">IARAS</option>
				
				<option value="9193">IBATE</option>
				
				<option value="9195">IBIRA</option>
				
				<option value="9196">IBIRAREMA</option>
				
				<option value="9197">IBITINGA</option>
				
				<option value="9201">IBIUNA</option>
				
				<option value="9202">ICEM</option>
				
				<option value="9204">IEPE</option>
				
				<option value="9206">IGARACU DO TIETE</option>
				
				<option value="9208">IGARAPAVA</option>
				
				<option value="9209">IGARATA</option>
				
				<option value="9210">IGUAPE</option>
				
				<option value="9211">ILHA COMPRIDA</option>
				
				<option value="9213">ILHA SOLTEIRA</option>
				
				<option value="9214">ILHABELA</option>
				
				<option value="9216">INDAIATUBA</option>
				
				<option value="9217">INDIANA</option>
				
				<option value="9218">INDIAPORA</option>
				
				<option value="9220">INUBIA PAULISTA</option>
				
				<option value="9221">IPAUSSU</option>
				
				<option value="9222">IPERO</option>
				
				<option value="9223">IPEUNA</option>
				
				<option value="9224">IPIGUA</option>
				
				<option value="9225">IPORANGA</option>
				
				<option value="9226">IPUA</option>
				
				<option value="9227">IRACEMAPOLIS</option>
				
				<option value="9229">IRAPUA</option>
				
				<option value="9230">IRAPURU</option>
				
				<option value="9231">ITABERA</option>
				
				<option value="9233">ITAI</option>
				
				<option value="9235">ITAJOBI</option>
				
				<option value="9236">ITAJU</option>
				
				<option value="9237">ITANHAEM</option>
				
				<option value="9238">ITAOCA</option>
				
				<option value="9239">ITAPECERICA DA SERRA</option>
				
				<option value="9240">ITAPETININGA</option>
				
				<option value="9242">ITAPEVA</option>
				
				<option value="9243">ITAPEVI</option>
				
				<option value="9244">ITAPIRA</option>
				
				<option value="9245">ITAPIRAPUA PAULISTA</option>
				
				<option value="9246">ITAPOLIS</option>
				
				<option value="9247">ITAPORANGA</option>
				
				<option value="9248">ITAPUI</option>
				
				<option value="9249">ITAPURA</option>
				
				<option value="9250">ITAQUAQUECETUBA</option>
				
				<option value="9252">ITARARE</option>
				
				<option value="9253">ITARIRI</option>
				
				<option value="9254">ITATIBA</option>
				
				<option value="9255">ITATINGA</option>
				
				<option value="9256">ITIRAPINA</option>
				
				<option value="9257">ITIRAPUA</option>
				
				<option value="9258">ITOBI</option>
				
				<option value="9260">ITU</option>
				
				<option value="9261">ITUPEVA</option>
				
				<option value="9262">ITUVERAVA</option>
				
				<option value="9264">JABORANDI</option>
				
				<option value="9265">JABOTICABAL</option>
				
				<option value="9267">JACAREI</option>
				
				<option value="9268">JACI</option>
				
				<option value="9271">JACUPIRANGA</option>
				
				<option value="9273">JAGUARIUNA</option>
				
				<option value="9274">JALES</option>
				
				<option value="9276">JAMBEIRO</option>
				
				<option value="9277">JANDIRA</option>
				
				<option value="9282">JARDINOPOLIS</option>
				
				<option value="9283">JARINU</option>
				
				<option value="9285">JAU</option>
				
				<option value="9286">JERIQUARA</option>
				
				<option value="9287">JOANOPOLIS</option>
				
				<option value="9288">JOAO RAMALHO</option>
				
				<option value="9291">JOSE BONIFACIO</option>
				
				<option value="9293">JULIO MESQUITA</option>
				
				<option value="9294">JUMIRIM</option>
				
				<option value="9295">JUNDIAI</option>
				
				<option value="9298">JUNQUEIROPOLIS</option>
				
				<option value="9299">JUQUIA</option>
				
				<option value="9301">JUQUITIBA</option>
				
				<option value="9309">LAGOINHA</option>
				
				<option value="9310">LARANJAL PAULISTA</option>
				
				<option value="9313">LAVINIA</option>
				
				<option value="9314">LAVRINHAS</option>
				
				<option value="9315">LEME</option>
				
				<option value="9316">LENCOIS PAULISTA</option>
				
				<option value="9317">LIMEIRA</option>
				
				<option value="9318">LINDOIA</option>
				
				<option value="9319">LINS</option>
				
				<option value="9321">LORENA</option>
				
				<option value="9322">LOURDES</option>
				
				<option value="9323">LOUVEIRA</option>
				
				<option value="9324">LUCELIA</option>
				
				<option value="9325">LUCIANOPOLIS</option>
				
				<option value="9326">LUIS ANTONIO</option>
				
				<option value="9327">LUIZIANIA</option>
				
				<option value="9328">LUPERCIO</option>
				
				<option value="9330">LUTECIA</option>
				
				<option value="9331">MACATUBA</option>
				
				<option value="9332">MACAUBAL</option>
				
				<option value="9333">MACEDONIA</option>
				
				<option value="9335">MAGDA</option>
				
				<option value="9337">MAIRINQUE</option>
				
				<option value="9338">MAIRIPORA</option>
				
				<option value="9340">MANDURI</option>
				
				<option value="9342">MARABA PAULISTA</option>
				
				<option value="9343">MARACAI</option>
				
				<option value="9344">MARAPOAMA</option>
				
				<option value="9347">MARIAPOLIS</option>
				
				<option value="9348">MARILIA</option>
				
				<option value="9349">MARINOPOLIS</option>
				
				<option value="9353">MARTINOPOLIS</option>
				
				<option value="9354">MATAO</option>
				
				<option value="9355">MAUA</option>
				
				<option value="9356">MENDONCA</option>
				
				<option value="9357">MERIDIANO</option>
				
				<option value="9358">MESOPOLIS</option>
				
				<option value="9359">MIGUELOPOLIS</option>
				
				<option value="9360">MINEIROS DO TIETE</option>
				
				<option value="9361">MIRA ESTRELA</option>
				
				<option value="9362">MIRACATU</option>
				
				<option value="9364">MIRANDOPOLIS</option>
				
				<option value="9365">MIRANTE DO PARANAPANEMA</option>
				
				<option value="9366">MIRASSOL</option>
				
				<option value="9367">MIRASSOLANDIA</option>
				
				<option value="9368">MOCOCA</option>
				
				<option value="9369">MOGI DAS CRUZES</option>
				
				<option value="9370">MOGI GUACU</option>
				
				<option value="9371">MOGI MIRIM</option>
				
				<option value="9372">MOMBUCA</option>
				
				<option value="9373">MONCOES</option>
				
				<option value="9374">MONGAGUA</option>
				
				<option value="9376">MONTE ALEGRE DO SUL</option>
				
				<option value="9377">MONTE ALTO</option>
				
				<option value="9378">MONTE APRAZIVEL</option>
				
				<option value="9379">MONTE AZUL PAULISTA</option>
				
				<option value="9381">MONTE CASTELO</option>
				
				<option value="9382">MONTE MOR</option>
				
				<option value="9384">MONTEIRO LOBATO</option>
				
				<option value="9386">MORRO AGUDO</option>
				
				<option value="9388">MORUNGABA</option>
				
				<option value="9390">MOTUCA</option>
				
				<option value="9392">MURUTINGA DO SUL</option>
				
				<option value="9393">NANTES</option>
				
				<option value="9394">NARANDIBA</option>
				
				<option value="9395">NATIVIDADE DA SERRA</option>
				
				<option value="9396">NAZARE PAULISTA</option>
				
				<option value="9397">NEVES PAULISTA</option>
				
				<option value="9398">NHANDEARA</option>
				
				<option value="9399">NIPOA</option>
				
				<option value="9403">NOVA ALIANCA</option>
				
				<option value="9406">NOVA CAMPINA</option>
				
				<option value="9407">NOVA CANAA PAULISTA</option>
				
				<option value="9408">NOVA CASTILHO</option>
				
				<option value="9409">NOVA EUROPA</option>
				
				<option value="9410">NOVA GRANADA</option>
				
				<option value="9411">NOVA GUATAPORANGA</option>
				
				<option value="9412">NOVA INDEPENDENCIA</option>
				
				<option value="9414">NOVA LUZITANIA</option>
				
				<option value="9415">NOVA ODESSA</option>
				
				<option value="9418">NOVAIS</option>
				
				<option value="9420">NOVO HORIZONTE</option>
				
				<option value="9421">NUPORANGA</option>
				
				<option value="9423">OCAUCU</option>
				
				<option value="9424">OLEO</option>
				
				<option value="9425">OLIMPIA</option>
				
				<option value="9428">ONDA VERDE</option>
				
				<option value="9429">ORIENTE</option>
				
				<option value="9430">ORINDIUVA</option>
				
				<option value="9431">ORLANDIA</option>
				
				<option value="9432">OSASCO</option>
				
				<option value="9433">OSCAR BRESSANE</option>
				
				<option value="9434">OSVALDO CRUZ</option>
				
				<option value="9435">OURINHOS</option>
				
				<option value="9437">OURO VERDE</option>
				
				<option value="9438">OUROESTE</option>
				
				<option value="9439">PACAEMBU</option>
				
				<option value="9441">PALESTINA</option>
				
				<option value="9442">PALMARES PAULISTA</option>
				
				<option value="9443">PALMEIRA D'OESTE</option>
				
				<option value="9445">PALMITAL</option>
				
				<option value="9446">PANORAMA</option>
				
				<option value="9447">PARAGUACU PAULISTA</option>
				
				<option value="9448">PARAIBUNA</option>
				
				<option value="9449">PARAISO</option>
				
				<option value="9452">PARANAPANEMA</option>
				
				<option value="9454">PARANAPUA</option>
				
				<option value="9455">PARAPUA</option>
				
				<option value="9456">PARDINHO</option>
				
				<option value="9457">PARIQUERA-ACU</option>
				
				<option value="9458">PARISI</option>
				
				<option value="9462">PATROCINIO PAULISTA</option>
				
				<option value="9463">PAULICEIA</option>
				
				<option value="9464">PAULINIA</option>
				
				<option value="9465">PAULISTANIA</option>
				
				<option value="9466">PAULO DE FARIA</option>
				
				<option value="9468">PEDERNEIRAS</option>
				
				<option value="9469">PEDRA BELA</option>
				
				<option value="9471">PEDRANOPOLIS</option>
				
				<option value="9472">PEDREGULHO</option>
				
				<option value="9473">PEDREIRA</option>
				
				<option value="9474">PEDRINHAS PAULISTA</option>
				
				<option value="9476">PEDRO DE TOLEDO</option>
				
				<option value="9477">PENAPOLIS</option>
				
				<option value="9478">PEREIRA BARRETO</option>
				
				<option value="9479">PEREIRAS</option>
				
				<option value="9480">PERUIBE</option>
				
				<option value="9481">PIACATU</option>
				
				<option value="9483">PIEDADE</option>
				
				<option value="9484">PILAR DO SUL</option>
				
				<option value="9485">PINDAMONHANGABA</option>
				
				<option value="9486">PINDORAMA</option>
				
				<option value="9487">PINHALZINHO</option>
				
				<option value="9490">PIQUEROBI</option>
				
				<option value="9491">PIQUETE</option>
				
				<option value="9492">PIRACAIA</option>
				
				<option value="9493">PIRACICABA</option>
				
				<option value="9494">PIRAJU</option>
				
				<option value="9495">PIRAJUI</option>
				
				<option value="9497">PIRANGI</option>
				
				<option value="9499">PIRAPORA DO BOM JESUS</option>
				
				<option value="9500">PIRAPOZINHO</option>
				
				<option value="9501">PIRASSUNUNGA</option>
				
				<option value="9502">PIRATININGA</option>
				
				<option value="9503">PITANGUEIRAS</option>
				
				<option value="9504">PLANALTO</option>
				
				<option value="9507">PLATINA</option>
				
				<option value="9508">POA</option>
				
				<option value="9509">POLONI</option>
				
				<option value="9511">POMPEIA</option>
				
				<option value="9512">PONGAI</option>
				
				<option value="9513">PONTAL</option>
				
				<option value="9514">PONTALINDA</option>
				
				<option value="9515">PONTES GESTAL</option>
				
				<option value="9516">POPULINA</option>
				
				<option value="9517">PORANGABA</option>
				
				<option value="9518">PORTO FELIZ</option>
				
				<option value="9519">PORTO FERREIRA</option>
				
				<option value="9521">POTIM</option>
				
				<option value="9522">POTIRENDABA</option>
				
				<option value="9524">PRACINHA</option>
				
				<option value="9526">PRADOPOLIS</option>
				
				<option value="9527">PRAIA GRANDE</option>
				
				<option value="9528">PRATANIA</option>
				
				<option value="9529">PRESIDENTE ALVES</option>
				
				<option value="9530">PRESIDENTE BERNARDES</option>
				
				<option value="9531">PRESIDENTE EPITACIO</option>
				
				<option value="9532">PRESIDENTE PRUDENTE</option>
				
				<option value="9533">PRESIDENTE VENCESLAU</option>
				
				<option value="9535">PROMISSAO</option>
				
				<option value="9537">QUADRA</option>
				
				<option value="9538">QUATA</option>
				
				<option value="9539">QUEIROZ</option>
				
				<option value="9540">QUELUZ</option>
				
				<option value="9541">QUINTANA</option>
				
				<option value="9543">RAFARD</option>
				
				<option value="9544">RANCHARIA</option>
				
				<option value="9546">REDENCAO DA SERRA</option>
				
				<option value="9547">REGENTE FEIJO</option>
				
				<option value="9548">REGINOPOLIS</option>
				
				<option value="9549">REGISTRO</option>
				
				<option value="9550">RESTINGA</option>
				
				<option value="9552">RIBEIRA</option>
				
				<option value="9553">RIBEIRAO BONITO</option>
				
				<option value="9554">RIBEIRAO BRANCO</option>
				
				<option value="9555">RIBEIRAO CORRENTE</option>
				
				<option value="9556">RIBEIRAO DO SUL</option>
				
				<option value="9557">RIBEIRAO DOS INDIOS</option>
				
				<option value="9558">RIBEIRAO GRANDE</option>
				
				<option value="9559">RIBEIRAO PIRES</option>
				
				<option value="9560">RIBEIRAO PRETO</option>
				
				<option value="9563">RIFAINA</option>
				
				<option value="9564">RINCAO</option>
				
				<option value="9565">RINOPOLIS</option>
				
				<option value="9566">RIO CLARO</option>
				
				<option value="9567">RIO DAS PEDRAS</option>
				
				<option value="9568">RIO GRANDE DA SERRA</option>
				
				<option value="9569">RIOLANDIA</option>
				
				<option value="9570">RIVERSUL</option>
				
				<option value="9573">ROSANA</option>
				
				<option value="9574">ROSEIRA</option>
				
				<option value="9575">RUBIACEA</option>
				
				<option value="9577">RUBINEIA</option>
				
				<option value="9580">SABINO</option>
				
				<option value="9581">SAGRES</option>
				
				<option value="9582">SALES</option>
				
				<option value="9583">SALES OLIVEIRA</option>
				
				<option value="9584">SALESOPOLIS</option>
				
				<option value="9585">SALMOURAO</option>
				
				<option value="9586">SALTINHO</option>
				
				<option value="9587">SALTO</option>
				
				<option value="9588">SALTO DE PIRAPORA</option>
				
				<option value="9590">SALTO GRANDE</option>
				
				<option value="9591">SANDOVALINA</option>
				
				<option value="9592">SANTA ADELIA</option>
				
				<option value="9593">SANTA ALBERTINA</option>
				
				<option value="9595">SANTA BARBARA D'OESTE</option>
				
				<option value="9596">SANTA BRANCA</option>
				
				<option value="9597">SANTA CLARA D'OESTE</option>
				
				<option value="9598">SANTA CRUZ DA CONCEICAO</option>
				
				<option value="9599">SANTA CRUZ DA ESPERANCA</option>
				
				<option value="9601">SANTA CRUZ DAS PALMEIRAS</option>
				
				<option value="9602">SANTA CRUZ DO RIO PARDO</option>
				
				<option value="9604">SANTA ERNESTINA</option>
				
				<option value="9606">SANTA FE DO SUL</option>
				
				<option value="9607">SANTA GERTRUDES</option>
				
				<option value="9608">SANTA ISABEL</option>
				
				<option value="9610">SANTA LUCIA</option>
				
				<option value="9612">SANTA MARIA DA SERRA</option>
				
				<option value="9614">SANTA MERCEDES</option>
				
				<option value="9616">SANTA RITA DO PASSA QUATRO</option>
				
				<option value="9615">SANTA RITA D'OESTE</option>
				
				<option value="9618">SANTA ROSA DE VITERBO</option>
				
				<option value="9619">SANTA SALETE</option>
				
				<option value="9621">SANTANA DA PONTE PENSA</option>
				
				<option value="9622">SANTANA DE PARNAIBA</option>
				
				<option value="9624">SANTO ANASTACIO</option>
				
				<option value="9625">SANTO ANDRE</option>
				
				<option value="9626">SANTO ANTONIO DA ALEGRIA</option>
				
				<option value="9628">SANTO ANTONIO DE POSSE</option>
				
				<option value="9629">SANTO ANTONIO DO ARACANGUA</option>
				
				<option value="9630">SANTO ANTONIO DO JARDIM</option>
				
				<option value="9632">SANTO ANTONIO DO PINHAL</option>
				
				<option value="9634">SANTO EXPEDITO</option>
				
				<option value="9635">SANTOPOLIS DO AGUAPEI</option>
				
				<option value="9636">SANTOS</option>
				
				<option value="9639">SAO BENTO DO SAPUCAI</option>
				
				<option value="9640">SAO BERNARDO DO CAMPO</option>
				
				<option value="9642">SAO CAETANO DO SUL</option>
				
				<option value="9643">SAO CARLOS</option>
				
				<option value="9644">SAO FRANCISCO</option>
				
				<option value="9647">SAO JOAO DA BOA VISTA</option>
				
				<option value="9648">SAO JOAO DAS DUAS PONTES</option>
				
				<option value="9649">SAO JOAO DE IRACEMA</option>
				
				<option value="9652">SAO JOAO DO PAU D'ALHO</option>
				
				<option value="9654">SAO JOAQUIM DA BARRA</option>
				
				<option value="9655">SAO JOSE DA BELA VISTA</option>
				
				<option value="9657">SAO JOSE DO BARREIRO</option>
				
				<option value="9658">SAO JOSE DO RIO PARDO</option>
				
				<option value="9659">SAO JOSE DO RIO PRETO</option>
				
				<option value="9660">SAO JOSE DOS CAMPOS</option>
				
				<option value="9661">SAO LOURENCO DA SERRA</option>
				
				<option value="9663">SAO LUIZ DO PARAITINGA</option>
				
				<option value="9665">SAO MANUEL</option>
				
				<option value="9667">SAO MIGUEL ARCANJO</option>
				
				<option value="9668">SAO PAULO</option>
				
				<option value="9669">SAO PEDRO</option>
				
				<option value="9670">SAO PEDRO DO TURVO</option>
				
				<option value="9671">SAO ROQUE</option>
				
				<option value="9673">SAO SEBASTIAO</option>
				
				<option value="9674">SAO SEBASTIAO DA GRAMA</option>
				
				<option value="9677">SAO SIMAO</option>
				
				<option value="9678">SAO VICENTE</option>
				
				<option value="9680">SARAPUI</option>
				
				<option value="9681">SARUTAIA</option>
				
				<option value="9682">SEBASTIANOPOLIS DO SUL</option>
				
				<option value="9683">SERRA AZUL</option>
				
				<option value="9684">SERRA NEGRA</option>
				
				<option value="9685">SERRANA</option>
				
				<option value="9686">SERTAOZINHO</option>
				
				<option value="9687">SETE BARRAS</option>
				
				<option value="9688">SEVERINIA</option>
				
				<option value="9690">SILVEIRAS</option>
				
				<option value="9693">SOCORRO</option>
				
				<option value="9696">SOROCABA</option>
				
				<option value="9698">SUD MENNUCCI</option>
				
				<option value="9700">SUMARE</option>
				
				<option value="9702">SUZANAPOLIS</option>
				
				<option value="9703">SUZANO</option>
				
				<option value="9705">TABAPUA</option>
				
				<option value="9706">TABATINGA</option>
				
				<option value="9707">TABOAO DA SERRA</option>
				
				<option value="9708">TACIBA</option>
				
				<option value="9709">TAGUAI</option>
				
				<option value="9710">TAIACU</option>
				
				<option value="9712">TAIUVA</option>
				
				<option value="9714">TAMBAU</option>
				
				<option value="9715">TANABI</option>
				
				<option value="9717">TAPIRAI</option>
				
				<option value="9718">TAPIRATIBA</option>
				
				<option value="9719">TAQUARAL</option>
				
				<option value="9720">TAQUARITINGA</option>
				
				<option value="9721">TAQUARITUBA</option>
				
				<option value="9722">TAQUARIVAI</option>
				
				<option value="9723">TARABAI</option>
				
				<option value="9724">TARUMA</option>
				
				<option value="9725">TATUI</option>
				
				<option value="9726">TAUBATE</option>
				
				<option value="9728">TEJUPA</option>
				
				<option value="9729">TEODORO SAMPAIO</option>
				
				<option value="9732">TERRA ROXA</option>
				
				<option value="9735">TIETE</option>
				
				<option value="9736">TIMBURI</option>
				
				<option value="9738">TORRE DE PEDRA</option>
				
				<option value="9739">TORRINHA</option>
				
				<option value="9740">TRABIJU</option>
				
				<option value="9741">TREMEMBE</option>
				
				<option value="9743">TRES FRONTEIRAS</option>
				
				<option value="9746">TUIUTI</option>
				
				<option value="9748">TUPA</option>
				
				<option value="9750">TUPI PAULISTA</option>
				
				<option value="9752">TURIUBA</option>
				
				<option value="9753">TURMALINA</option>
				
				<option value="9755">UBARANA</option>
				
				<option value="9756">UBATUBA</option>
				
				<option value="9757">UBIRAJARA</option>
				
				<option value="9758">UCHOA</option>
				
				<option value="9759">UNIAO PAULISTA</option>
				
				<option value="9761">URANIA</option>
				
				<option value="9762">URU</option>
				
				<option value="9763">URUPES</option>
				
				<option value="9767">VALENTIM GENTIL</option>
				
				<option value="9768">VALINHOS</option>
				
				<option value="9769">VALPARAISO</option>
				
				<option value="9771">VARGEM</option>
				
				<option value="9772">VARGEM GRANDE DO SUL</option>
				
				<option value="9773">VARGEM GRANDE PAULISTA</option>
				
				<option value="9775">VARZEA PAULISTA</option>
				
				<option value="9777">VERA CRUZ</option>
				
				<option value="9783">VINHEDO</option>
				
				<option value="9784">VIRADOURO</option>
				
				<option value="9785">VISTA ALEGRE DO ALTO</option>
				
				<option value="9786">VITORIA BRASIL</option>
				
				<option value="9788">VOTORANTIM</option>
				
				<option value="9789">VOTUPORANGA</option>
				
				<option value="9790">ZACARIAS</option>
				
                  </select>
               </td>
               <td></td>
            </tr>
            <tr>
               <td align="right"><span class="txtcinza2b">Bandeira:</span></td>
               <td>
                  <select name="sBandeira" class="busca" onChange="limpaCnpj()">
                      <option value="0"></option>
                      
							<option value="Bandeira Branca">BRANCA</option>
					  
			<option value="ABENGOA - SÃO JOÃO">ABENGOA - SÃO JOÃO</option>
			
			<option value="ACOL">ACOL</option>
			
			<option value="AÇOS VILLARES">AÇOS VILLARES</option>
			
			<option value="AGECOM">AGECOM</option>
			
			<option value="AGILE">AGILE</option>
			
			<option value="AGIP DISTRIBUIDORA">AGIP DISTRIBUIDORA</option>
			
			<option value="AGRO INDUSTRIAL TABU">AGRO INDUSTRIAL TABU</option>
			
			<option value="AGRO VISTA ALEGRE">AGRO VISTA ALEGRE</option>
			
			<option value="AGUIA DISTRIBUIDORA">AGUIA DISTRIBUIDORA</option>
			
			<option value="AIR BP">AIR BP</option>
			
			<option value="ALAMO">ALAMO</option>
			
			<option value="ALBATROZ">ALBATROZ</option>
			
			<option value="ALCOM">ALCOM</option>
			
			<option value="ALCOOL MANDU">ALCOOL MANDU</option>
			
			<option value="ALCOOLBRAS">ALCOOLBRAS</option>
			
			<option value="ALCOOLPETRO">ALCOOLPETRO</option>
			
			<option value="ALE COMBUSTÍVEIS">ALE COMBUSTÍVEIS</option>
			
			<option value="ALESAT">ALESAT</option>
			
			<option value="ALFA">ALFA</option>
			
			<option value="ALFA PETRÓLEO">ALFA PETRÓLEO</option>
			
			<option value="ALIANÇA">ALIANÇA</option>
			
			<option value="ALPES">ALPES</option>
			
			<option value="ALPHA">ALPHA</option>
			
			<option value="ALVO">ALVO</option>
			
			<option value="ALVORADA">ALVORADA</option>
			
			<option value="A.M.">A.M.</option>
			
			<option value="AMAZONIA">AMAZONIA</option>
			
			<option value="AMBIENTAL">AMBIENTAL</option>
			
			<option value="AMERICA LATINA">AMERICA LATINA</option>
			
			<option value="AMERICAN">AMERICAN</option>
			
			<option value="AMERICANOIL">AMERICANOIL</option>
			
			<option value="AM2">AM2</option>
			
			<option value="AQUARIUS">AQUARIUS</option>
			
			<option value="ARAGUAIA">ARAGUAIA</option>
			
			<option value="ARAPETRO">ARAPETRO</option>
			
			<option value="ARCO">ARCO</option>
			
			<option value="ARNOPETRO">ARNOPETRO</option>
			
			<option value="AROGAS">AROGAS</option>
			
			<option value="ARROWS">ARROWS</option>
			
			<option value="ART PETRO">ART PETRO</option>
			
			<option value="ASA DELTA">ASA DELTA</option>
			
			<option value="ASADIESEL">ASADIESEL</option>
			
			<option value="ASK">ASK</option>
			
			<option value="ASPEN">ASPEN</option>
			
			<option value="ASTER">ASTER</option>
			
			<option value="ATEM' S">ATEM' S</option>
			
			<option value="ATLANTA">ATLANTA</option>
			
			<option value="ATLÂNTICA">ATLÂNTICA</option>
			
			<option value="ATLANTIQUE">ATLANTIQUE</option>
			
			<option value="ATLAS">ATLAS</option>
			
			<option value="ATON">ATON</option>
			
			<option value="AUDAX">AUDAX</option>
			
			<option value="AUXILIAR">AUXILIAR</option>
			
			<option value="AVAN">AVAN</option>
			
			<option value="B & V">B & V</option>
			
			<option value="BAND PROD PET">BAND PROD PET</option>
			
			<option value="BARDAN">BARDAN</option>
			
			<option value="BARREIRA">BARREIRA</option>
			
			<option value="BASE-PETRO">BASE-PETRO</option>
			
			<option value="BASILE">BASILE</option>
			
			<option value="BATUVY">BATUVY</option>
			
			<option value="B.D. DISTRIBUIDORA">B.D. DISTRIBUIDORA</option>
			
			<option value="BELLS">BELLS</option>
			
			<option value="BENZ OIL">BENZ OIL</option>
			
			<option value="BENZINA">BENZINA</option>
			
			<option value="BETA DISTRIBUIDORA">BETA DISTRIBUIDORA</option>
			
			<option value="BETA TRANSPORTADORA">BETA TRANSPORTADORA</option>
			
			<option value="BETEL">BETEL</option>
			
			<option value="BETUNEL">BETUNEL</option>
			
			<option value="BG GNV">BG GNV</option>
			
			<option value="B.GRECA">B.GRECA</option>
			
			<option value="BIG PETRO">BIG PETRO</option>
			
			<option value="BIOPETRÓLEO">BIOPETRÓLEO</option>
			
			<option value="BIOSTRATUM">BIOSTRATUM</option>
			
			<option value="BISPO">BISPO</option>
			
			<option value="BIZUNGÃO">BIZUNGÃO</option>
			
			<option value="BLACK GOLD">BLACK GOLD</option>
			
			<option value="BOMM-PETRO">BOMM-PETRO</option>
			
			<option value="BRASIL OIL">BRASIL OIL</option>
			
			<option value="BRASILAMER">BRASILAMER</option>
			
			<option value="BRASILPETRO">BRASILPETRO</option>
			
			<option value="BRASKEM">BRASKEM</option>
			
			<option value="BRASOIL">BRASOIL</option>
			
			<option value="BRAXPETRO">BRAXPETRO</option>
			
			<option value="BRECAR">BRECAR</option>
			
			<option value="BREMEN">BREMEN</option>
			
			<option value="BUD">BUD</option>
			
			<option value="BUFFALO">BUFFALO</option>
			
			<option value="BULLS">BULLS</option>
			
			<option value="CAIÇARA">CAIÇARA</option>
			
			<option value="CAMACUA">CAMACUA</option>
			
			<option value="CAMPO">CAMPO</option>
			
			<option value="CANA">CANA</option>
			
			<option value="CANIDE">CANIDE</option>
			
			<option value="CAOME">CAOME</option>
			
			<option value="CARAJAS">CARAJAS</option>
			
			<option value="CARBOMIX">CARBOMIX</option>
			
			<option value="CARBONO QUÍMICA">CARBONO QUÍMICA</option>
			
			<option value="CARBOPETRO">CARBOPETRO</option>
			
			<option value="CARIBEAN">CARIBEAN</option>
			
			<option value="CASQUEL">CASQUEL</option>
			
			<option value="CBPI">CBPI</option>
			
			<option value="CENTRAL">CENTRAL</option>
			
			<option value="CENTRO">CENTRO</option>
			
			<option value="CENTRO AMERICA">CENTRO AMERICA</option>
			
			<option value="CENTRO OESTE">CENTRO OESTE</option>
			
			<option value="CENTRO OESTE 0494">CENTRO OESTE 0494</option>
			
			<option value="CENTRO SUL">CENTRO SUL</option>
			
			<option value="CERBA">CERBA</option>
			
			<option value="CERRE">CERRE</option>
			
			<option value="CHARRUA">CHARRUA</option>
			
			<option value="CHICAGO">CHICAGO</option>
			
			<option value="CHUY">CHUY</option>
			
			<option value="CIA NIQUEL T">CIA NIQUEL T</option>
			
			<option value="CIAPETRO">CIAPETRO</option>
			
			<option value="CIAX">CIAX</option>
			
			<option value="CILLOS">CILLOS</option>
			
			<option value="COBERPOSTO 0344">COBERPOSTO 0344</option>
			
			<option value="COBRADIS-COMPANHIA">COBRADIS-COMPANHIA</option>
			
			<option value="CODIPETROS">CODIPETROS</option>
			
			<option value="COINBRA">COINBRA</option>
			
			<option value="COLOMBO">COLOMBO</option>
			
			<option value="COMBUSPEVA">COMBUSPEVA</option>
			
			<option value="COMBUSTEC">COMBUSTEC</option>
			
			<option value="COMELLI">COMELLI</option>
			
			<option value="COMERCIAL">COMERCIAL</option>
			
			<option value="COMERCIAL 0068">COMERCIAL 0068</option>
			
			<option value="COMLUB">COMLUB</option>
			
			<option value="COMO">COMO</option>
			
			<option value="COMPANHIA">COMPANHIA</option>
			
			<option value="COMPANHIA ASTRA">COMPANHIA ASTRA</option>
			
			<option value="COMPETRO">COMPETRO</option>
			
			<option value="CONTATTO DISTRIBUIDORA">CONTATTO DISTRIBUIDORA</option>
			
			<option value="CONTINENTAL">CONTINENTAL</option>
			
			<option value="COOPEBRAS-COOPERATIVA">COOPEBRAS-COOPERATIVA</option>
			
			<option value="COOPERATIVA">COOPERATIVA</option>
			
			<option value="COOPERATIVA DE ALAGOAS">COOPERATIVA DE ALAGOAS</option>
			
			<option value="COPACESP-COOPERATIVA">COPACESP-COOPERATIVA</option>
			
			<option value="COPERCANA">COPERCANA</option>
			
			<option value="COPERSUCAR">COPERSUCAR</option>
			
			<option value="COROL">COROL</option>
			
			<option value="CORPORATE">CORPORATE</option>
			
			<option value="CORREA & CORREA">CORREA & CORREA</option>
			
			<option value="COSAN">COSAN</option>
			
			<option value="COSAN LUBRIFICANTES">COSAN LUBRIFICANTES</option>
			
			<option value="COSMOS">COSMOS</option>
			
			<option value="CRISTO REI">CRISTO REI</option>
			
			<option value="CRUZ DE MALTA">CRUZ DE MALTA</option>
			
			<option value="CRUZEIRO DO SUL">CRUZEIRO DO SUL</option>
			
			<option value="DALCOQUIO">DALCOQUIO</option>
			
			<option value="DANPETRO">DANPETRO</option>
			
			<option value="DARK">DARK</option>
			
			<option value="D.C.">D.C.</option>
			
			<option value="DCP DISTRIBUIDORA">DCP DISTRIBUIDORA</option>
			
			<option value="DELTA">DELTA</option>
			
			<option value="DELTA BRASIL">DELTA BRASIL</option>
			
			<option value="DETROIT">DETROIT</option>
			
			<option value="DIAL">DIAL</option>
			
			<option value="DIAMANTE">DIAMANTE</option>
			
			<option value="DIBRAPE">DIBRAPE</option>
			
			<option value="DIC">DIC</option>
			
			<option value="DICOPA">DICOPA</option>
			
			<option value="DINAMICA">DINAMICA</option>
			
			<option value="DINAMO">DINAMO</option>
			
			<option value="DIPALCOOL">DIPALCOOL</option>
			
			<option value="DIPALUB-DISTRIBUIDORA">DIPALUB-DISTRIBUIDORA</option>
			
			<option value="DIRECIONAL">DIRECIONAL</option>
			
			<option value="DISBRASPETRO">DISBRASPETRO</option>
			
			<option value="DISCAPEL">DISCAPEL</option>
			
			<option value="DISLUB">DISLUB</option>
			
			<option value="DISMAX">DISMAX</option>
			
			<option value="DISPETRO">DISPETRO</option>
			
			<option value="DISPETRO DISTRIBUIDORA">DISPETRO DISTRIBUIDORA</option>
			
			<option value="DISTROPAR">DISTROPAR</option>
			
			<option value="D`MAIS">D`MAIS</option>
			
			<option value="DNP">DNP</option>
			
			<option value="DNP CANCELADA">DNP CANCELADA</option>
			
			<option value="DOMINIUM">DOMINIUM</option>
			
			<option value="DON">DON</option>
			
			<option value="DPPI">DPPI</option>
			
			<option value="DPX">DPX</option>
			
			<option value="DRP">DRP</option>
			
			<option value="DUVALE">DUVALE</option>
			
			<option value="EBT">EBT</option>
			
			<option value="ECCO">ECCO</option>
			
			<option value="ECCO PETRO">ECCO PETRO</option>
			
			<option value="ECO BRASIL">ECO BRASIL</option>
			
			<option value="ECOLOGICA">ECOLOGICA</option>
			
			<option value="ECOMAT">ECOMAT</option>
			
			<option value="ECOVERDE">ECOVERDE</option>
			
			<option value="EDENGAS">EDENGAS</option>
			
			<option value="ELDORADO">ELDORADO</option>
			
			<option value="ELIAS">ELIAS</option>
			
			<option value="ELLO">ELLO</option>
			
			<option value="ELLO-PUMA">ELLO-PUMA</option>
			
			<option value="ELLO¿S">ELLO¿S</option>
			
			<option value="ENERGI">ENERGI</option>
			
			<option value="ENERGY">ENERGY</option>
			
			<option value="ENRON">ENRON</option>
			
			<option value="EQUADOR">EQUADOR</option>
			
			<option value="ESCADA">ESCADA</option>
			
			<option value="ESTACAO">ESTACAO</option>
			
			<option value="ESTRADA">ESTRADA</option>
			
			<option value="EURO COMBUSTÍVEIS">EURO COMBUSTÍVEIS</option>
			
			<option value="EURO PETRO">EURO PETRO</option>
			
			<option value="EURO PETRÓLEO">EURO PETRÓLEO</option>
			
			<option value="EXXEL">EXXEL</option>
			
			<option value="EXXONMOBIL">EXXONMOBIL</option>
			
			<option value="FAN">FAN</option>
			
			<option value="FARO PETRO">FARO PETRO</option>
			
			<option value="FAST">FAST</option>
			
			<option value="F.C. DISTRIBUIDORA">F.C. DISTRIBUIDORA</option>
			
			<option value="FEDERAL">FEDERAL</option>
			
			<option value="FELINQUE">FELINQUE</option>
			
			<option value="FÉLIX">FÉLIX</option>
			
			<option value="FERA">FERA</option>
			
			<option value="FERREIRA">FERREIRA</option>
			
			<option value="FERREIRA 0093">FERREIRA 0093</option>
			
			<option value="FIRST DO BRASIL">FIRST DO BRASIL</option>
			
			<option value="FIX">FIX</option>
			
			<option value="FLAG">FLAG</option>
			
			<option value="FLEX DISTRIBUIDORA">FLEX DISTRIBUIDORA</option>
			
			<option value="FLEXCOM">FLEXCOM</option>
			
			<option value="FLEXPETRO">FLEXPETRO</option>
			
			<option value="FLORIDA">FLORIDA</option>
			
			<option value="FORMULA">FORMULA</option>
			
			<option value="FOX">FOX</option>
			
			<option value="FRANNEL">FRANNEL</option>
			
			<option value="FROLLETT">FROLLETT</option>
			
			<option value="GALATICA">GALATICA</option>
			
			<option value="GARRA">GARRA</option>
			
			<option value="GASDIESEL DISTRIBUIDORA">GASDIESEL DISTRIBUIDORA</option>
			
			<option value="GASFORTE">GASFORTE</option>
			
			<option value="GASOIL">GASOIL</option>
			
			<option value="GASOL">GASOL</option>
			
			<option value="GENWA 0347">GENWA 0347</option>
			
			<option value="GERAES">GERAES</option>
			
			<option value="GIANPETRO">GIANPETRO</option>
			
			<option value="GIDPETRO">GIDPETRO</option>
			
			<option value="GIGANTE">GIGANTE</option>
			
			<option value="GLOBAL DISTRIBUIDORA">GLOBAL DISTRIBUIDORA</option>
			
			<option value="GLORIA">GLORIA</option>
			
			<option value="GOIAS">GOIAS</option>
			
			<option value="GOIASPETRO">GOIASPETRO</option>
			
			<option value="GOL COMBUSTÍVEIS">GOL COMBUSTÍVEIS</option>
			
			<option value="GOLD">GOLD</option>
			
			<option value="GOLFO">GOLFO</option>
			
			<option value="GOMES">GOMES</option>
			
			<option value="GP">GP</option>
			
			<option value="GP">GP</option>
			
			<option value="GPETRO">GPETRO</option>
			
			<option value="GRAN PETRO">GRAN PETRO</option>
			
			<option value="GRANEL">GRANEL</option>
			
			<option value="GRANEL QUÍMICA">GRANEL QUÍMICA</option>
			
			<option value="GREEN">GREEN</option>
			
			<option value="GRM">GRM</option>
			
			<option value="GT 0355">GT 0355</option>
			
			<option value="GUAICUI">GUAICUI</option>
			
			<option value="GUAIRA">GUAIRA</option>
			
			<option value="HEDIC">HEDIC</option>
			
			<option value="HELISUL">HELISUL</option>
			
			<option value="HELMAR">HELMAR</option>
			
			<option value="HOOK">HOOK</option>
			
			<option value="HORA">HORA</option>
			
			<option value="HOUSTON">HOUSTON</option>
			
			<option value="HUSTON 0394">HUSTON 0394</option>
			
			<option value="HYPER">HYPER</option>
			
			<option value="IBIDIESEL">IBIDIESEL</option>
			
			<option value="IDAZA">IDAZA</option>
			
			<option value="IMPERIAL">IMPERIAL</option>
			
			<option value="INCA">INCA</option>
			
			<option value="INDUSTRIA">INDUSTRIA</option>
			
			<option value="INTER">INTER</option>
			
			<option value="INTEROIL">INTEROIL</option>
			
			<option value="IPE">IPE</option>
			
			<option value="IPIRANGA">IPIRANGA</option>
			
			<option value="ISABELLA">ISABELLA</option>
			
			<option value="ITAPOA">ITAPOA</option>
			
			<option value="JACAR">JACAR</option>
			
			<option value="JACARANDA">JACARANDA</option>
			
			<option value="JAGUAR">JAGUAR</option>
			
			<option value="JAN PETRO">JAN PETRO</option>
			
			<option value="JATOBA">JATOBA</option>
			
			<option value="J.C.">J.C.</option>
			
			<option value="JETGAS">JETGAS</option>
			
			<option value="JOAPI">JOAPI</option>
			
			<option value="J.OLIVEIRA">J.OLIVEIRA</option>
			
			<option value="JOMAP">JOMAP</option>
			
			<option value="JPJ">JPJ</option>
			
			<option value="J.R DISTRIBUIDORA">J.R DISTRIBUIDORA</option>
			
			<option value="JUMBO">JUMBO</option>
			
			<option value="JUVICOL">JUVICOL</option>
			
			<option value="KANSAS">KANSAS</option>
			
			<option value="KING OIL">KING OIL</option>
			
			<option value="K8">K8</option>
			
			<option value="LAKAR">LAKAR</option>
			
			<option value="LARCO">LARCO</option>
			
			<option value="LATINA">LATINA</option>
			
			<option value="LEADING">LEADING</option>
			
			<option value="LIDER DISTRIBUIDORA">LIDER DISTRIBUIDORA</option>
			
			<option value="LIDERPETRO">LIDERPETRO</option>
			
			<option value="LINCE">LINCE</option>
			
			<option value="LIQUIGÁS">LIQUIGÁS</option>
			
			<option value="LITORAL">LITORAL</option>
			
			<option value="L.M.">L.M.</option>
			
			<option value="L.M. BRASILEIRA">L.M. BRASILEIRA</option>
			
			<option value="LOTUS">LOTUS</option>
			
			<option value="LUBCOM">LUBCOM</option>
			
			<option value="LUBRAS">LUBRAS</option>
			
			<option value="LUBRIFICA">LUBRIFICA</option>
			
			<option value="LUBRIVILA">LUBRIVILA</option>
			
			<option value="MACHADO">MACHADO</option>
			
			<option value="MACOM">MACOM</option>
			
			<option value="MAGNUM">MAGNUM</option>
			
			<option value="MANANCIAL">MANANCIAL</option>
			
			<option value="MANCHESTER">MANCHESTER</option>
			
			<option value="MANGUARY">MANGUARY</option>
			
			<option value="MANGUINHOS">MANGUINHOS</option>
			
			<option value="MANHATAN">MANHATAN</option>
			
			<option value="MARAPATA">MARAPATA</option>
			
			<option value="MASTER">MASTER</option>
			
			<option value="MASTER 0330">MASTER 0330</option>
			
			<option value="MASUT DISTRIBUIDORA">MASUT DISTRIBUIDORA</option>
			
			<option value="MAX">MAX</option>
			
			<option value="MAX DISTRIBUIDORA">MAX DISTRIBUIDORA</option>
			
			<option value="MAXIMA (EX EXTRA)">MAXIMA (EX EXTRA)</option>
			
			<option value="MAXSOLV">MAXSOLV</option>
			
			<option value="MAXSUL">MAXSUL</option>
			
			<option value="MAXXI">MAXXI</option>
			
			<option value="MAZP DISTRIBUIDORA">MAZP DISTRIBUIDORA</option>
			
			<option value="MEG UNION">MEG UNION</option>
			
			<option value="MEGA BRASILEIRA">MEGA BRASILEIRA</option>
			
			<option value="MEGA OIL">MEGA OIL</option>
			
			<option value="MEGAPETRO">MEGAPETRO</option>
			
			<option value="MERCOIL">MERCOIL</option>
			
			<option value="MERCOSUL">MERCOSUL</option>
			
			<option value="MERCOSUL PETROLEO">MERCOSUL PETROLEO</option>
			
			<option value="MERIDIAN">MERIDIAN</option>
			
			<option value="META">META</option>
			
			<option value="METRON SA">METRON SA</option>
			
			<option value="MIDWESCO">MIDWESCO</option>
			
			<option value="MIG">MIG</option>
			
			<option value="MILLENIUM">MILLENIUM</option>
			
			<option value="MINAS DISTRIBUIDORA">MINAS DISTRIBUIDORA</option>
			
			<option value="MINAS OIL">MINAS OIL</option>
			
			<option value="MINUANO">MINUANO</option>
			
			<option value="MISTER OIL">MISTER OIL</option>
			
			<option value="MM ORIGINAL">MM ORIGINAL</option>
			
			<option value="MODIPEL">MODIPEL</option>
			
			<option value="MONTE">MONTE</option>
			
			<option value="MONTE CABRAL">MONTE CABRAL</option>
			
			<option value="MONTEPETRO">MONTEPETRO</option>
			
			<option value="MONTES CLAROS">MONTES CLAROS</option>
			
			<option value="MONVALE">MONVALE</option>
			
			<option value="MOVE">MOVE</option>
			
			<option value="MTD">MTD</option>
			
			<option value="MULTIPETRO">MULTIPETRO</option>
			
			<option value="MUNDIAL">MUNDIAL</option>
			
			<option value="NACIONAL DISTRIBUIDORA">NACIONAL DISTRIBUIDORA</option>
			
			<option value="NASA">NASA</option>
			
			<option value="NASCAR">NASCAR</option>
			
			<option value="NAUTILUS">NAUTILUS</option>
			
			<option value="NELL-OIL">NELL-OIL</option>
			
			<option value="NORDESTE">NORDESTE</option>
			
			<option value="NORFOLK">NORFOLK</option>
			
			<option value="NOROESTE">NOROESTE</option>
			
			<option value="NOVOESTE">NOVOESTE</option>
			
			<option value="N.S.A. DISTRIBUIDORA">N.S.A. DISTRIBUIDORA</option>
			
			<option value="OASIS">OASIS</option>
			
			<option value="OCEÂNICA">OCEÂNICA</option>
			
			<option value="OCIDENTAL">OCIDENTAL</option>
			
			<option value="OIL PETRO">OIL PETRO</option>
			
			<option value="OMB">OMB</option>
			
			<option value="ONYX">ONYX</option>
			
			<option value="ORCA">ORCA</option>
			
			<option value="ORGAP">ORGAP</option>
			
			<option value="ORION">ORION</option>
			
			<option value="OSWALDO RIBEIRO DE MENDONÇA">OSWALDO RIBEIRO DE MENDONÇA</option>
			
			<option value="OURO NEGRO">OURO NEGRO</option>
			
			<option value="OUROPETRO">OUROPETRO</option>
			
			<option value="OXXON">OXXON</option>
			
			<option value="PACIFIC">PACIFIC</option>
			
			<option value="PALLUS">PALLUS</option>
			
			<option value="PANAMERICA">PANAMERICA</option>
			
			<option value="PANTANAL">PANTANAL</option>
			
			<option value="PANTERA">PANTERA</option>
			
			<option value="PARAÍSO">PARAÍSO</option>
			
			<option value="PARANAPANEMA">PARANAPANEMA</option>
			
			<option value="PDV BRASIL">PDV BRASIL</option>
			
			<option value="PEDEVESA">PEDEVESA</option>
			
			<option value="PEDRESCHI">PEDRESCHI</option>
			
			<option value="PELIKANO">PELIKANO</option>
			
			<option value="PENTOIL">PENTOIL</option>
			
			<option value="PEROLA">PEROLA</option>
			
			<option value="PETRO AGUIA">PETRO AGUIA</option>
			
			<option value="PETRO AMAZON">PETRO AMAZON</option>
			
			<option value="PETRO DALLAS">PETRO DALLAS</option>
			
			<option value="PETRO ESTIMA">PETRO ESTIMA</option>
			
			<option value="PETRO EXPRESS JC">PETRO EXPRESS JC</option>
			
			<option value="PETRO POWER">PETRO POWER</option>
			
			<option value="PETRO REZENDE">PETRO REZENDE</option>
			
			<option value="PETROALCOOL">PETROALCOOL</option>
			
			<option value="PETROBAHIA">PETROBAHIA</option>
			
			<option value="PETROBALL">PETROBALL</option>
			
			<option value="PETROBOM">PETROBOM</option>
			
			<option value="PETROBRAS DISTRIBUIDORA S.A.">PETROBRAS DISTRIBUIDORA S.A.</option>
			
			<option value="PETROCAMPOS">PETROCAMPOS</option>
			
			<option value="PETROCEM">PETROCEM</option>
			
			<option value="PETROCORP">PETROCORP</option>
			
			<option value="PETRODAN">PETRODAN</option>
			
			<option value="PETROEXPRESS">PETROEXPRESS</option>
			
			<option value="PETROFER">PETROFER</option>
			
			<option value="PETROFORTE">PETROFORTE</option>
			
			<option value="PETRO-GARÇAS">PETRO-GARÇAS</option>
			
			<option value="PETROGOIAS">PETROGOIAS</option>
			
			<option value="PETROGOLD">PETROGOLD</option>
			
			<option value="PETROLAGOS">PETROLAGOS</option>
			
			<option value="PETROLEO EXTRA">PETROLEO EXTRA</option>
			
			<option value="PETROLEUM">PETROLEUM</option>
			
			<option value="PETROLUB">PETROLUB</option>
			
			<option value="PETROLUNA">PETROLUNA</option>
			
			<option value="PETROLUZ">PETROLUZ</option>
			
			<option value="PETROMAIS">PETROMAIS</option>
			
			<option value="PETROMARTE">PETROMARTE</option>
			
			<option value="PETROMAXX">PETROMAXX</option>
			
			<option value="PETROMIL">PETROMIL</option>
			
			<option value="PETROMOTOR">PETROMOTOR</option>
			
			<option value="PETRONAC">PETRONAC</option>
			
			<option value="PETRONOL">PETRONOL</option>
			
			<option value="PETRONOSSA">PETRONOSSA</option>
			
			<option value="PETRONOVA">PETRONOVA</option>
			
			<option value="PETROPALMAS">PETROPALMAS</option>
			
			<option value="PETROPAR DISTRIBUIDORA">PETROPAR DISTRIBUIDORA</option>
			
			<option value="PETROPAULI 0451">PETROPAULI 0451</option>
			
			<option value="PETROPAULO 0056">PETROPAULO 0056</option>
			
			<option value="PETROQUALITY">PETROQUALITY</option>
			
			<option value="PETROQUERA">PETROQUERA</option>
			
			<option value="PETRORIBE">PETRORIBE</option>
			
			<option value="PETROSALVADOR">PETROSALVADOR</option>
			
			<option value="PETROSERRA">PETROSERRA</option>
			
			<option value="PETROSERV">PETROSERV</option>
			
			<option value="PETROSETE">PETROSETE</option>
			
			<option value="PETROSILVA">PETROSILVA</option>
			
			<option value="PETROSOJA">PETROSOJA</option>
			
			<option value="PETROSOL">PETROSOL</option>
			
			<option value="PETROSOL DIESEL">PETROSOL DIESEL</option>
			
			<option value="PETROSUL">PETROSUL</option>
			
			<option value="PETROTIBA">PETROTIBA</option>
			
			<option value="PETROVALLE">PETROVALLE</option>
			
			<option value="PETROVIX">PETROVIX</option>
			
			<option value="PETROWORLD">PETROWORLD</option>
			
			<option value="PETROX">PETROX</option>
			
			<option value="PETROX DISTRIBUIDORA">PETROX DISTRIBUIDORA</option>
			
			<option value="PETROXIM">PETROXIM</option>
			
			<option value="PETROZARA">PETROZARA</option>
			
			<option value="PETRUS BRASILEIRA">PETRUS BRASILEIRA</option>
			
			<option value="PHOENIX">PHOENIX</option>
			
			<option value="PICK GAS">PICK GAS</option>
			
			<option value="PLUS PETRO">PLUS PETRO</option>
			
			<option value="P.N. PETRÓLEO">P.N. PETRÓLEO</option>
			
			<option value="PODIUM">PODIUM</option>
			
			<option value="POLIPETRO">POLIPETRO</option>
			
			<option value="POLLUS">POLLUS</option>
			
			<option value="PONTUAL">PONTUAL</option>
			
			<option value="POTENCIAL">POTENCIAL</option>
			
			<option value="POWER">POWER</option>
			
			<option value="POWER PETRO">POWER PETRO</option>
			
			<option value="P.P.">P.P.</option>
			
			<option value="PR DISTRIBUIDORA">PR DISTRIBUIDORA</option>
			
			<option value="PRADO 0402">PRADO 0402</option>
			
			<option value="PRADOBEL">PRADOBEL</option>
			
			<option value="PREMIUM">PREMIUM</option>
			
			<option value="PREMIUM TRANSPORTES">PREMIUM TRANSPORTES</option>
			
			<option value="PROGRESSO">PROGRESSO</option>
			
			<option value="PUIG">PUIG</option>
			
			<option value="P.W.A.">P.W.A.</option>
			
			<option value="QUALI PETRO">QUALI PETRO</option>
			
			<option value="QUALITY DISTRIBUIDORA">QUALITY DISTRIBUIDORA</option>
			
			<option value="RAIZEN">RAIZEN</option>
			
			<option value="RAIZEN MIME">RAIZEN MIME</option>
			
			<option value="RAÍZEN TARUMÃ">RAÍZEN TARUMÃ</option>
			
			<option value="RAJA">RAJA</option>
			
			<option value="RAVATO">RAVATO</option>
			
			<option value="RCX">RCX</option>
			
			<option value="REAL MINAS">REAL MINAS</option>
			
			<option value="REALCOOL">REALCOOL</option>
			
			<option value="REALPETRO">REALPETRO</option>
			
			<option value="RED LION">RED LION</option>
			
			<option value="REDE BRASIL">REDE BRASIL</option>
			
			<option value="REDE SOL">REDE SOL</option>
			
			<option value="REDEPETRO">REDEPETRO</option>
			
			<option value="REJAILE">REJAILE</option>
			
			<option value="RESIPETROS">RESIPETROS</option>
			
			<option value="RESIVALE">RESIVALE</option>
			
			<option value="REZENDE">REZENDE</option>
			
			<option value="RIO BRANCO">RIO BRANCO</option>
			
			<option value="RIO GRANDE">RIO GRANDE</option>
			
			<option value="RIO VERDE">RIO VERDE</option>
			
			<option value="RIO VERMELHO">RIO VERMELHO</option>
			
			<option value="RIOIL 0457">RIOIL 0457</option>
			
			<option value="RIOPETRO">RIOPETRO</option>
			
			<option value="RM PETROLEO">RM PETROLEO</option>
			
			<option value="RN PETRÓLEO">RN PETRÓLEO</option>
			
			<option value="RODOIL">RODOIL</option>
			
			<option value="RODONAP">RODONAP</option>
			
			<option value="RODOPETRO">RODOPETRO</option>
			
			<option value="ROMA">ROMA</option>
			
			<option value="ROYAL FIC">ROYAL FIC</option>
			
			<option value="ROYAL PETRO">ROYAL PETRO</option>
			
			<option value="RR">RR</option>
			
			<option value="RUFF C.J.">RUFF C.J.</option>
			
			<option value="RUMOS">RUMOS</option>
			
			<option value="RZD DISTRIBUIDORA">RZD DISTRIBUIDORA</option>
			
			<option value="SAARA">SAARA</option>
			
			<option value="SAB TRADING">SAB TRADING</option>
			
			<option value="SABBÁ">SABBÁ</option>
			
			<option value="SADIPE">SADIPE</option>
			
			<option value="SAFRA">SAFRA</option>
			
			<option value="SALEMCO">SALEMCO</option>
			
			<option value="SAMPAPETRO">SAMPAPETRO</option>
			
			<option value="SANTA FE">SANTA FE</option>
			
			<option value="SANTAREN">SANTAREN</option>
			
			<option value="SARFIL">SARFIL</option>
			
			<option value="SATELITE">SATELITE</option>
			
			<option value="SAUDA">SAUDA</option>
			
			<option value="SAURO">SAURO</option>
			
			<option value="SCORPION">SCORPION</option>
			
			<option value="SDP">SDP</option>
			
			<option value="SEC">SEC</option>
			
			<option value="SEC">SEC</option>
			
			<option value="SEDERAMA">SEDERAMA</option>
			
			<option value="SERCOM">SERCOM</option>
			
			<option value="SERTA">SERTA</option>
			
			<option value="SETA">SETA</option>
			
			<option value="SETTA DISTRIBUIDORA">SETTA DISTRIBUIDORA</option>
			
			<option value="SEVEN">SEVEN</option>
			
			<option value="SHS-DISTRIBUIDORA">SHS-DISTRIBUIDORA</option>
			
			<option value="SIGG">SIGG</option>
			
			<option value="SIGMA">SIGMA</option>
			
			<option value="SIMARELLI">SIMARELLI</option>
			
			<option value="SIMEIRA">SIMEIRA</option>
			
			<option value="SKY LUB">SKY LUB</option>
			
			<option value="SL">SL</option>
			
			<option value="SMALL">SMALL</option>
			
			<option value="SOLL">SOLL</option>
			
			<option value="SOLLUZ">SOLLUZ</option>
			
			<option value="SORRISO">SORRISO</option>
			
			<option value="SP">SP</option>
			
			<option value="SPCOM">SPCOM</option>
			
			<option value="SPPEDGO">SPPEDGO</option>
			
			<option value="S.R.">S.R.</option>
			
			<option value="SR">SR</option>
			
			<option value="SR BRASIL (EX-METRON)">SR BRASIL (EX-METRON)</option>
			
			<option value="STA HELENA">STA HELENA</option>
			
			<option value="STANG">STANG</option>
			
			<option value="STAR">STAR</option>
			
			<option value="STAR PETRO">STAR PETRO</option>
			
			<option value="STOCK">STOCK</option>
			
			<option value="STORAGE">STORAGE</option>
			
			<option value="STS">STS</option>
			
			<option value="SUL AMERICA">SUL AMERICA</option>
			
			<option value="SUL AMERICANA">SUL AMERICANA</option>
			
			<option value="SUL COMBUSTÍVEIS">SUL COMBUSTÍVEIS</option>
			
			<option value="SULANDRE">SULANDRE</option>
			
			<option value="SULPETRO">SULPETRO</option>
			
			<option value="SULTAO">SULTAO</option>
			
			<option value="SUMMER PETRO">SUMMER PETRO</option>
			
			<option value="SUPER FLEX">SUPER FLEX</option>
			
			<option value="SUPREMA">SUPREMA</option>
			
			<option value="T.A.">T.A.</option>
			
			<option value="TABOCAO">TABOCAO</option>
			
			<option value="TAG DISTRIBUIDORA">TAG DISTRIBUIDORA</option>
			
			<option value="TAURUS">TAURUS</option>
			
			<option value="TECAB">TECAB</option>
			
			<option value="TEMAPE">TEMAPE</option>
			
			<option value="TEMOPE">TEMOPE</option>
			
			<option value="TERRA">TERRA</option>
			
			<option value="TERRA BRASIL">TERRA BRASIL</option>
			
			<option value="THOR">THOR</option>
			
			<option value="TIC">TIC</option>
			
			<option value="TIGER OIL">TIGER OIL</option>
			
			<option value="TIGRE">TIGRE</option>
			
			<option value="TIM DISTRIBUIDORA">TIM DISTRIBUIDORA</option>
			
			<option value="TINSPETRO">TINSPETRO</option>
			
			<option value="TITANIC">TITANIC</option>
			
			<option value="T.M.">T.M.</option>
			
			<option value="TOBRAS">TOBRAS</option>
			
			<option value="TOP PETROLEUM">TOP PETROLEUM</option>
			
			<option value="TORRAO">TORRAO</option>
			
			<option value="TOTAL">TOTAL</option>
			
			<option value="TOWER">TOWER</option>
			
			<option value="T.R.">T.R.</option>
			
			<option value="TRAMP OIL">TRAMP OIL</option>
			
			<option value="TRAMP OIL DIST">TRAMP OIL DIST</option>
			
			<option value="TRANSO">TRANSO</option>
			
			<option value="TRANS-OIL">TRANS-OIL</option>
			
			<option value="TREVO">TREVO</option>
			
			<option value="TRIANGULO">TRIANGULO</option>
			
			<option value="TRIANGULO 0329">TRIANGULO 0329</option>
			
			<option value="TRIM">TRIM</option>
			
			<option value="TROPICAL">TROPICAL</option>
			
			<option value="TUBE TOY`S">TUBE TOY`S</option>
			
			<option value="TUX">TUX</option>
			
			<option value="TWISTER">TWISTER</option>
			
			<option value="UBERLANDIA">UBERLANDIA</option>
			
			<option value="UBINAN">UBINAN</option>
			
			<option value="UBP PETRÓLEO">UBP PETRÓLEO</option>
			
			<option value="UF">UF</option>
			
			<option value="UMBARA">UMBARA</option>
			
			<option value="UNI">UNI</option>
			
			<option value="UNIBRASPE">UNIBRASPE</option>
			
			<option value="UNIP">UNIP</option>
			
			<option value="UNITY">UNITY</option>
			
			<option value="USINA DA BARRA">USINA DA BARRA</option>
			
			<option value="VALE DO PARAIBA">VALE DO PARAIBA</option>
			
			<option value="VALESUL">VALESUL</option>
			
			<option value="VALLE">VALLE</option>
			
			<option value="VALLE PETRO">VALLE PETRO</option>
			
			<option value="VECTHA">VECTHA</option>
			
			<option value="VECTRO OIL">VECTRO OIL</option>
			
			<option value="VEGA">VEGA</option>
			
			<option value="VETOR">VETOR</option>
			
			<option value="VIRALCOOL">VIRALCOOL</option>
			
			<option value="VISUAL">VISUAL</option>
			
			<option value="VITOL ENERGY">VITOL ENERGY</option>
			
			<option value="VITORIA PETROS">VITORIA PETROS</option>
			
			<option value="VR PETRO">VR PETRO</option>
			
			<option value="WALENDOWSKY">WALENDOWSKY</option>
			
			<option value="WALTER LUIS">WALTER LUIS</option>
			
			<option value="WATT">WATT</option>
			
			<option value="WD DISTRIBUIDORA">WD DISTRIBUIDORA</option>
			
			<option value="WEBPETRO">WEBPETRO</option>
			
			<option value="W.E.P">W.E.P</option>
			
			<option value="WEST OIL">WEST OIL</option>
			
			<option value="WEST'CO">WEST'CO</option>
			
			<option value="WJ">WJ</option>
			
			<option value="WV">WV</option>
			
			<option value="X DISTRIBUIDORA">X DISTRIBUIDORA</option>
			
			<option value="X PETRO">X PETRO</option>
			
			<option value="Y. KAMINAGAKURA">Y. KAMINAGAKURA</option>
			
			<option value="YPETRO">YPETRO</option>
			
			<option value="ZEMA">ZEMA</option>
			
			<option value="76 OIL">76 OIL</option>
			
                  </select></td>
               <tr> <td align="right">
                  <span class="txtcinza2b">Combustível:</span></td>
                  <td><select class="busca" name="sProduto" onChange="limpaCnpj()">
                      <option value="0"></option>
                      
			<option value="420201001">DMA - MGO</option> 
			
			<option value="810101002">ETANOL HIDRATADO ADITIVADO</option> 
			
			<option value="810101001">ETANOL HIDRATADO COMUM</option> 
			
			<option value="220101005">GÁS NATURAL VEICULAR</option> 
			
			<option value="320102001">GASOLINA C COMUM</option> 
			
			<option value="320102002">GASOLINA C COMUM ADITIVADA</option> 
			
			<option value="320102003">GASOLINA C PREMIUM</option> 
			
			<option value="320102005">GASOLINA C PREMIUM ADITIVADA</option> 
			
			<option value="320201001">GASOLINA DE AVIAÇÃO</option> 
			
			<option value="820101033">ÓLEO DIESEL B S10 - ADITIVADO</option> 
			
			<option value="820101034">ÓLEO DIESEL B S10 - COMUM</option> 
			
			<option value="820101013">ÓLEO DIESEL B S500 - ADITIVADO</option> 
			
			<option value="820101012">ÓLEO DIESEL B S500 - COMUM</option> 
			
			<option value="410101001">QUEROSENE DE AVIAÇÃO</option> 
			
			<option value="410102001">QUEROSENE ILUMINANTE</option> 
			
                  </select>
              </td>
               <tr> <td align="right">
                  <span class="txtcinza2b">Tipo de posto:</span></td>
                  <td><select class="busca" name="sTipodePosto">
                      
                      <option value="0" selected></option>
					  <option value="1" >Revendedor</option>
                      <option value="2" >Abastecimento</option>
                      <option value="3" >Escola</option>
                      <option value="4" >GNV</option>
                      <option value="5" >Flutuante</option>
                      <option value="6" >Aviação</option>
                      <option value="7" >Marítimo</option> <!-- 2096222 12/08/2015 -->

                  </select>
              </td>
              <td>
              <input type="hidden" name="p" value="">
              <input type="hidden" name="hPesquisar" value="">
              <input tabindex=3 type="button" value="Pesquisar" name="bPesquisar" onClick="Submeter();">
              <!--Submeter();-->
              </td>
            </tr>
            <tr><td class="txtcinza2b" colspan=2>
                Informar ao menos mais de um campo para pesquisa.
            </td></tr>
            <tr><td colspan=3 class="txtcinza2b">
                Caso deseje verificar a autenticidade de Certificado já emitido, <b><a  href="CertificadoConfirmacao.asp">clique aqui</a></b>
            </td></tr>
			<td><td colspan=1 class="txtcinza2b"> Versão 7.2.0 </td>
          </table>

      </form>


  </table>

   
		  <table>
				<tr >
					<td width="100%" height="100%" align="top" bgcolor="E7E7E7">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
 			    </tr>
				<tr>
					<form Method="Post" Action = "GeraExcel.asp" name = "formexport">
						<td align="left"  ><font face=Verdana  size=1.5 color=Red> <b> Caso deseje exportar os dados dos REVENDEDORES AUTORIZADOS EM OPERAÇÃO <b> clique em exportar </b>  </b> </font>
						</td>
							<td align = "right" >
							<input align = left Type="Submit" Value="Exportar" id=Submit2 name=Submit1 >
							<form Method="Post" Action="resultado.asp"   name="frmResultado">
							</form>
							<a href="GeraExcel.asp"></a>
							</td>
						</form>
				</tr>
				<tr >
					<td width="100%" height="100%" align="top" > <font face=Verdana  size=1.5 color=Red ><b> ATENÇÃO:</b> Não serão exportados os dados dos agentes que não se encontram autorizados pela ANP no momento dessa consulta.</font></td>
				</tr>
				<tr >
					<td width="100%" height="100%" align="top" bgcolor="E7E7E7">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
				</tr>
			</table>
	           <tr>          <td bgcolor=#D7D7D7 colspan=6><font face=Verdana size=2 color=red><b>Resultado da pesquisa: 16116 registros encontrados.</b></font></td>        </tr>      <table width=100% border=0 cellspacing=3>        <tr>          <td bgcolor=#D7D7D7 colspan=7><font face=Verdana size=1 color=#666666><FONT face=Verdana color=blue size=1><b>Para visualizar informações mais detalhadas, clique no CNPJ do posto desejado.</b></FONT></td>        </tr>        <tr>          <td width=120 bgcolor=#D7D7D7 VALIGN=TOP><span class=txtcinza2b>CNPJ</span></td>          <td width=150 bgcolor=#D7D7D7 VALIGN=TOP><span class=txtcinza2b>Razão Social</span></td>          <td width=140 bgcolor=#D7D7D7 VALIGN=TOP><span class=txtcinza2b>Nome Fantasia</span></td>          <td width=20  bgcolor=#D7D7D7 VALIGN=TOP><span class=txtcinza2b>UF</span></td>          <td width=50  bgcolor=#D7D7D7 VALIGN=TOP><span class=txtcinza2b>Município</span></td>          <td width=40  bgcolor=#D7D7D7 VALIGN=TOP><span class=txtcinza2b>Bandeira/Início</span></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38611' name = 'i16116' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.000.891/0001-86' language=JavaScript onMouseMove='' onClick=jogaform('38611');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38611&estado=SP&municipio=SAO PAULO">
             00.000.891/0001-86
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BRASILIA AUTO SERVICOS LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BRASILIA AUTO SERVICOS</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55150' name = 'i16115' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.001.177/0001-02' language=JavaScript onMouseMove='' onClick=jogaform('55150');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55150&estado=SP&municipio=ANDRADINA">
             00.001.177/0001-02
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MEGID & MARINHO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO 1000</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ANDRADINA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='39085' name = 'i16114' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.001.653/0001-95' language=JavaScript onMouseMove='' onClick=jogaform('39085');>
             <!--
             <a href="resultado.asp?sRegRevendedor=39085&estado=SP&municipio=TARUMA">
             00.001.653/0001-95
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>B. A. DE MORAES & CIA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TARUMA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31203' name = 'i16113' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.002.953/0001-99' language=JavaScript onMouseMove='' onClick=jogaform('31203');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31203&estado=SP&municipio=BAURU">
             00.002.953/0001-99
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO JARDIM AMERICA DE BAURU LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO JARDIM AMERICA DE BAURU LTDA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BAURU</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31048' name = 'i16112' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.002.953/0002-70' language=JavaScript onMouseMove='' onClick=jogaform('31048');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31048&estado=SP&municipio=BAURU">
             00.002.953/0002-70
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO JARDIM AMERICA DE BAURU LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BAURU</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 03/04/2008</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='1408' name = 'i16111' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0001-21' language=JavaScript onMouseMove='' onClick=jogaform('1408');>
             <!--
             <a href="resultado.asp?sRegRevendedor=1408&estado=SP&municipio=SOROCABA">
             00.003.188/0001-21
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38808' name = 'i16110' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0002-02' language=JavaScript onMouseMove='' onClick=jogaform('38808');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38808&estado=SP&municipio=SOROCABA">
             00.003.188/0002-02
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO II</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38769' name = 'i16109' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0003-93' language=JavaScript onMouseMove='' onClick=jogaform('38769');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38769&estado=SP&municipio=SOROCABA">
             00.003.188/0003-93
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 03/12/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38813' name = 'i16108' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0004-74' language=JavaScript onMouseMove='' onClick=jogaform('38813');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38813&estado=SP&municipio=SOROCABA">
             00.003.188/0004-74
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO IV</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38809' name = 'i16107' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0005-55' language=JavaScript onMouseMove='' onClick=jogaform('38809');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38809&estado=SP&municipio=SOROCABA">
             00.003.188/0005-55
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32551' name = 'i16106' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0006-36' language=JavaScript onMouseMove='' onClick=jogaform('32551');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32551&estado=SP&municipio=ITAPETININGA">
             00.003.188/0006-36
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ITAPETININGA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 19/12/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38807' name = 'i16105' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0009-89' language=JavaScript onMouseMove='' onClick=jogaform('38807');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38807&estado=SP&municipio=SOROCABA">
             00.003.188/0009-89
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO IX</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 09/12/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38806' name = 'i16104' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0010-12' language=JavaScript onMouseMove='' onClick=jogaform('38806');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38806&estado=SP&municipio=SOROCABA">
             00.003.188/0010-12
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO - X</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 11/12/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='30727' name = 'i16103' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0011-01' language=JavaScript onMouseMove='' onClick=jogaform('30727');>
             <!--
             <a href="resultado.asp?sRegRevendedor=30727&estado=SP&municipio=ARACOIABA DA SERRA">
             00.003.188/0011-01
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ARACOIABA DA SERRA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 06/02/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38810' name = 'i16102' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0012-84' language=JavaScript onMouseMove='' onClick=jogaform('38810');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38810&estado=SP&municipio=SOROCABA">
             00.003.188/0012-84
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO XII</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/02/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38687' name = 'i16101' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0013-65' language=JavaScript onMouseMove='' onClick=jogaform('38687');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38687&estado=SP&municipio=SARAPUI">
             00.003.188/0013-65
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO XIII</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SARAPUI</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/02/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38686' name = 'i16100' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0014-46' language=JavaScript onMouseMove='' onClick=jogaform('38686');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38686&estado=SP&municipio=SARAPUI">
             00.003.188/0014-46
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO XIV</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SARAPUI</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/02/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='30694' name = 'i16099' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0015-27' language=JavaScript onMouseMove='' onClick=jogaform('30694');>
             <!--
             <a href="resultado.asp?sRegRevendedor=30694&estado=SP&municipio=ANGATUBA">
             00.003.188/0015-27
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO XV</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ANGATUBA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 10/12/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58607' name = 'i16098' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0016-08' language=JavaScript onMouseMove='' onClick=jogaform('58607');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58607&estado=SP&municipio=SAO ROQUE">
             00.003.188/0016-08
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO XVI</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO ROQUE</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 09/12/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='173469' name = 'i16097' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0017-99' language=JavaScript onMouseMove='' onClick=jogaform('173469');>
             <!--
             <a href="resultado.asp?sRegRevendedor=173469&estado=SP&municipio=MARILIA">
             00.003.188/0017-99
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MARILIA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 09/10/2010</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='178149' name = 'i16096' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0018-70' language=JavaScript onMouseMove='' onClick=jogaform('178149');>
             <!--
             <a href="resultado.asp?sRegRevendedor=178149&estado=SP&municipio=SAO PAULO">
             00.003.188/0018-70
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 16/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32547' name = 'i16095' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.188/0019-50' language=JavaScript onMouseMove='' onClick=jogaform('32547');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32547&estado=SP&municipio=ITAPETININGA">
             00.003.188/0019-50
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO COMERCIO E DISTRIBUICAO DE DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMPETRO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ITAPETININGA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 06/08/2004</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33176' name = 'i16094' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.003.803/0001-08' language=JavaScript onMouseMove='' onClick=jogaform('33176');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33176&estado=SP&municipio=MARTINOPOLIS">
             00.003.803/0001-08
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>LUIZ ARTHUR ESTEVES DE MELLO</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO DA FORD</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MARTINOPOLIS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35279' name = 'i16093' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.004.110/0001-21' language=JavaScript onMouseMove='' onClick=jogaform('35279');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35279&estado=SP&municipio=SANTO ANDRE">
             00.004.110/0001-21
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ZAPP AUTO POSTO LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ZAPP AUTO POSTO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SANTO ANDRE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 20/06/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56835' name = 'i16092' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.004.654/0001-93' language=JavaScript onMouseMove='' onClick=jogaform('56835');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56835&estado=SP&municipio=ITATIBA">
             00.004.654/0001-93
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO POLO SANTA CRUZ LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO POLO ORIGINAL</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ITATIBA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55119' name = 'i16091' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.005.087/0001-90' language=JavaScript onMouseMove='' onClick=jogaform('55119');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55119&estado=SP&municipio=AMERICANA">
             00.005.087/0001-90
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>NABAS & CAMARGO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AMERICANA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 12/04/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33495' name = 'i16090' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.007.663/0001-38' language=JavaScript onMouseMove='' onClick=jogaform('33495');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33495&estado=SP&municipio=MOGI DAS CRUZES">
             00.007.663/0001-38
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MJS AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MOGI DAS CRUZES</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 02/08/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58586' name = 'i16089' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.008.183/0001-91' language=JavaScript onMouseMove='' onClick=jogaform('58586');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58586&estado=SP&municipio=SAO JOSE DOS CAMPOS">
             00.008.183/0001-91
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PRIMOS AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO JOSE DOS CAMPOS</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AGIP DISTRIBUIDORA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='39186' name = 'i16088' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.008.226/0001-39' language=JavaScript onMouseMove='' onClick=jogaform('39186');>
             <!--
             <a href="resultado.asp?sRegRevendedor=39186&estado=SP&municipio=TAUBATE">
             00.008.226/0001-39
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO MANGUEIRA II LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TAUBATE</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 19/01/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55271' name = 'i16087' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.008.311/0001-05' language=JavaScript onMouseMove='' onClick=jogaform('55271');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55271&estado=SP&municipio=ARACATUBA">
             00.008.311/0001-05
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO JC ARACATUBA LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO JC</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ARACATUBA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56752' name = 'i16086' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.008.468/0001-22' language=JavaScript onMouseMove='' onClick=jogaform('56752');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56752&estado=SP&municipio=ITAPIRA">
             00.008.468/0001-22
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO V.O. LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO V.O.</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ITAPIRA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55461' name = 'i16085' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.008.991/0001-59' language=JavaScript onMouseMove='' onClick=jogaform('55461');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55461&estado=SP&municipio=BARRETOS">
             00.008.991/0001-59
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO DIXON LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO ROTARORIA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BARRETOS</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33220' name = 'i16084' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.010.435/0001-17' language=JavaScript onMouseMove='' onClick=jogaform('33220');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33220&estado=SP&municipio=MATAO">
             00.010.435/0001-17
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BUCK AUTO POSTO E TRANSPORTES LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO BUCK</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MATAO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34332' name = 'i16083' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.010.577/0001-84' language=JavaScript onMouseMove='' onClick=jogaform('34332');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34332&estado=SP&municipio=PRESIDENTE VENCESLAU">
             00.010.577/0001-84
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO VENCESLAU II LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PEDRO II</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PRESIDENTE VENCESLAU</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57993' name = 'i16082' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.011.614/0001-79' language=JavaScript onMouseMove='' onClick=jogaform('57993');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57993&estado=SP&municipio=PRESIDENTE PRUDENTE">
             00.011.614/0001-79
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>REDE PRESTES MERIDIONAL LTDA - EPP</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PRESIDENTE PRUDENTE</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 03/06/2003</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57743' name = 'i16081' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.012.132/0001-33' language=JavaScript onMouseMove='' onClick=jogaform('57743');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57743&estado=SP&municipio=PIRASSUNUNGA">
             00.012.132/0001-33
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CENTER PIRAMIDE LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>CENTER PIRAMIDE</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PIRASSUNUNGA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROFORTE - 14/05/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34201' name = 'i16080' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.012.909/0001-60' language=JavaScript onMouseMove='' onClick=jogaform('34201');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34201&estado=SP&municipio=PIRACICABA">
             00.012.909/0001-60
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MAURICIO VALE</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO REZENDE</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PIRACICABA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31516' name = 'i16079' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.013.021/0001-41' language=JavaScript onMouseMove='' onClick=jogaform('31516');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31516&estado=SP&municipio=CATANDUVA">
             00.013.021/0001-41
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>COMERCIAL JULIU'S LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>JULIU'S AVENIDA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>CATANDUVA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34006' name = 'i16078' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.013.262/0001-90' language=JavaScript onMouseMove='' onClick=jogaform('34006');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34006&estado=SP&municipio=PEREIRA BARRETO">
             00.013.262/0001-90
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO PINHEIRO PEREIRA BARRETO LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO PINHEIRO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PEREIRA BARRETO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32561' name = 'i16077' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.013.386/0001-76' language=JavaScript onMouseMove='' onClick=jogaform('32561');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32561&estado=SP&municipio=ITAPETININGA">
             00.013.386/0001-76
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>NASCIMENTO E TRALDI LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO SAO PAULO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ITAPETININGA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AGIP DISTRIBUIDORA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36892' name = 'i16076' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.013.688/0001-44' language=JavaScript onMouseMove='' onClick=jogaform('36892');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36892&estado=SP&municipio=SAO PAULO">
             00.013.688/0001-44
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AMIRA AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AMIRA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MERCOIL - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32727' name = 'i16075' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.013.701/0001-65' language=JavaScript onMouseMove='' onClick=jogaform('32727');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32727&estado=SP&municipio=JARINU">
             00.013.701/0001-65
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO COLINAS DE JARINU LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>JARINU</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58814' name = 'i16074' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.015.401/0001-15' language=JavaScript onMouseMove='' onClick=jogaform('58814');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58814&estado=SP&municipio=TATUI">
             00.015.401/0001-15
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO POR DO SOL DE TATUI LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO POR SOL</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TATUI</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MERCOIL - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33976' name = 'i16073' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.015.449/0001-23' language=JavaScript onMouseMove='' onClick=jogaform('33976');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33976&estado=SP&municipio=PEDERNEIRAS">
             00.015.449/0001-23
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PICELLI & REIS LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PEDERNEIRAS</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33494' name = 'i16072' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.015.745/0001-24' language=JavaScript onMouseMove='' onClick=jogaform('33494');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33494&estado=SP&municipio=MOGI DAS CRUZES">
             00.015.745/0001-24
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO PITBULL LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO MOGI CENTER</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MOGI DAS CRUZES</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38610' name = 'i16071' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.016.966/0001-17' language=JavaScript onMouseMove='' onClick=jogaform('38610');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38610&estado=SP&municipio=SAO PAULO">
             00.016.966/0001-17
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>APLAUSO AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 27/04/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36668' name = 'i16070' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.016.968/0001-06' language=JavaScript onMouseMove='' onClick=jogaform('36668');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36668&estado=SP&municipio=SAO PAULO">
             00.016.968/0001-06
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO DE SERVICOS TALISMA SAO PAULO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO DE SERVICOS TALISMA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 04/04/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38609' name = 'i16069' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.016.969/0001-50' language=JavaScript onMouseMove='' onClick=jogaform('38609');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38609&estado=SP&municipio=SAO PAULO">
             00.016.969/0001-50
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO LIDER SANTOS DUMONT LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO LIDER</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 21/08/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38614' name = 'i16068' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.017.258/0001-09' language=JavaScript onMouseMove='' onClick=jogaform('38614');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38614&estado=SP&municipio=SAO PEDRO DO TURVO">
             00.017.258/0001-09
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO N. SRA APARECIDA SAO PEDRO DO TURVO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO N. SRA APARECIDA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PEDRO DO TURVO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 11/09/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36667' name = 'i16067' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.017.512/0001-60' language=JavaScript onMouseMove='' onClick=jogaform('36667');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36667&estado=SP&municipio=SAO PAULO">
             00.017.512/0001-60
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO DE SERVIÇOS MAKTOOB LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>REDE CAMPEÃO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 14/12/2016</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36569' name = 'i16066' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.017.674/0001-07' language=JavaScript onMouseMove='' onClick=jogaform('36569');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36569&estado=SP&municipio=SAO PAULO">
             00.017.674/0001-07
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO DO CARMO</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO DO CARMO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 01/02/2010</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38608' name = 'i16065' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.017.750/0001-76' language=JavaScript onMouseMove='' onClick=jogaform('38608');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38608&estado=SP&municipio=SAO PAULO">
             00.017.750/0001-76
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>CENTRO AUTOMOTIVO ARIZONA LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO EDGAR DOS SANTOS</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56527' name = 'i16064' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.018.273/0001-63' language=JavaScript onMouseMove='' onClick=jogaform('56527');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56527&estado=SP&municipio=IACANGA">
             00.018.273/0001-63
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>GONÇALVES & CAZARIN LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO SAO PAULO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IACANGA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 28/06/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34707' name = 'i16063' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.018.315/0001-66' language=JavaScript onMouseMove='' onClick=jogaform('34707');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34707&estado=SP&municipio=RIBEIRAO PRETO">
             00.018.315/0001-66
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>FUEL & WASH COMERCIAL LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RIBEIRAO PRETO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34383' name = 'i16062' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.018.417/0002-62' language=JavaScript onMouseMove='' onClick=jogaform('34383');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34383&estado=SP&municipio=RIBEIRAO BRANCO">
             00.018.417/0002-62
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SILVANA ROCHA MACHADO</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO MACHADO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RIBEIRAO BRANCO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56343' name = 'i16061' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.018.710/0001-49' language=JavaScript onMouseMove='' onClick=jogaform('56343');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56343&estado=SP&municipio=FRANCA">
             00.018.710/0001-49
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO-SHOPPING, FRANCA POSTO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO-SHOPPING</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>FRANCA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55270' name = 'i16060' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.018.789/0001-08' language=JavaScript onMouseMove='' onClick=jogaform('55270');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55270&estado=SP&municipio=ARACATUBA">
             00.018.789/0001-08
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO CANAL 1 ARAÇATUBA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO CANAL 1</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ARACATUBA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35143' name = 'i16059' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.020.280/0001-08' language=JavaScript onMouseMove='' onClick=jogaform('35143');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35143&estado=SP&municipio=SANTO ANDRE">
             00.020.280/0001-08
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PADOVA AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PADOVA AUTO POSTO LTDA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SANTO ANDRE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 12/07/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35059' name = 'i16058' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.021.093/0001-30' language=JavaScript onMouseMove='' onClick=jogaform('35059');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35059&estado=SP&municipio=SANTA ROSA DE VITERBO">
             00.021.093/0001-30
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO NOVA ROMA LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO ESTRELA AZUL</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SANTA ROSA DE VITERBO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 06/04/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38639' name = 'i16057' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.021.094/0001-85' language=JavaScript onMouseMove='' onClick=jogaform('38639');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38639&estado=SP&municipio=SAO SIMAO">
             00.021.094/0001-85
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO VALE DOS EUCALIPTOS LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO VALE DOS EUCALIPTOS LTDA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO SIMAO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MERCOIL - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55269' name = 'i16056' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.021.195/0001-56' language=JavaScript onMouseMove='' onClick=jogaform('55269');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55269&estado=SP&municipio=ARACATUBA">
             00.021.195/0001-56
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ARAÇATUBA NORTE AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO IPANEMA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ARACATUBA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 03/09/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58585' name = 'i16055' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.021.449/0001-36' language=JavaScript onMouseMove='' onClick=jogaform('58585');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58585&estado=SP&municipio=SAO JOSE DOS CAMPOS">
             00.021.449/0001-36
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO BOSQUE SATELITE LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO CIDADE JARDIM</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO JOSE DOS CAMPOS</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31202' name = 'i16054' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.021.475/0001-64' language=JavaScript onMouseMove='' onClick=jogaform('31202');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31202&estado=SP&municipio=BAURU">
             00.021.475/0001-64
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO NOSSA SENHORA DE FATIMA BAURU LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO DUQUE</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BAURU</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 30/11/2015</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32786' name = 'i16053' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.021.976/0001-40' language=JavaScript onMouseMove='' onClick=jogaform('32786');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32786&estado=SP&municipio=JAU">
             00.021.976/0001-40
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>DELTA JAU POSTO DE SERVIÇOS LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>DELTA POSTO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>JAU</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 01/12/2010</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38607' name = 'i16052' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.022.054/0001-58' language=JavaScript onMouseMove='' onClick=jogaform('38607');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38607&estado=SP&municipio=SAO PAULO">
             00.022.054/0001-58
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CENTRO AUTOMOTIVO TEXAS LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33700' name = 'i16051' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.022.127/0001-01' language=JavaScript onMouseMove='' onClick=jogaform('33700');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33700&estado=SP&municipio=NOVA GRANADA">
             00.022.127/0001-01
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>FERREIRA DERIVADOS DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO 18</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>NOVA GRANADA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31014' name = 'i16050' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.022.170/0001-77' language=JavaScript onMouseMove='' onClick=jogaform('31014');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31014&estado=SP&municipio=BASTOS">
             00.022.170/0001-77
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COMERCIAL AUTO POSTO ANDREASSA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO 2000</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BASTOS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57541' name = 'i16049' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.022.473/0001-90' language=JavaScript onMouseMove='' onClick=jogaform('57541');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57541&estado=SP&municipio=PALMITAL">
             00.022.473/0001-90
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>THORK OIL COMERCIO LUBRIFICANTES LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO ROTA SUL</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PALMITAL</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58834' name = 'i16048' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.022.964/0001-30' language=JavaScript onMouseMove='' onClick=jogaform('58834');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58834&estado=SP&municipio=TORRINHA">
             00.022.964/0001-30
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO DA PEDRA DE TORRINHA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO DA PEDRA DE TORRINHA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TORRINHA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 22/02/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34200' name = 'i16047' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.023.198/0001-29' language=JavaScript onMouseMove='' onClick=jogaform('34200');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34200&estado=SP&municipio=PIRACICABA">
             00.023.198/0001-29
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO E TRANSPORTADORA DIAS E MARTINS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO JARDIM EUROPA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PIRACICABA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 15/03/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57880' name = 'i16046' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.023.289/0001-64' language=JavaScript onMouseMove='' onClick=jogaform('57880');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57880&estado=SP&municipio=PRAIA GRANDE">
             00.023.289/0001-64
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO PRAIA DO FUTURO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PRAIA GRANDE</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='30847' name = 'i16045' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.024.598/0001-59' language=JavaScript onMouseMove='' onClick=jogaform('30847');>
             <!--
             <a href="resultado.asp?sRegRevendedor=30847&estado=SP&municipio=ARARAQUARA">
             00.024.598/0001-59
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO TROPICAL SHOPPING LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO TROPICAL SHOPPING</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ARARAQUARA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38606' name = 'i16044' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.024.610/0001-25' language=JavaScript onMouseMove='' onClick=jogaform('38606');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38606&estado=SP&municipio=SAO PAULO">
             00.024.610/0001-25
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TREVO DO PESSEGO COM E SERV DE COMBUST E LUBRIFIC LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TREVO DO PESSEGO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 25/08/2017</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56282' name = 'i16043' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.025.000/0001-46' language=JavaScript onMouseMove='' onClick=jogaform('56282');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56282&estado=SP&municipio=FRANCA">
             00.025.000/0001-46
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO CARAMURU DE FRANCA LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO CARAMURU</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>FRANCA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AGIP DISTRIBUIDORA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='39072' name = 'i16042' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.025.047/0001-00' language=JavaScript onMouseMove='' onClick=jogaform('39072');>
             <!--
             <a href="resultado.asp?sRegRevendedor=39072&estado=SP&municipio=TAQUARITINGA">
             00.025.047/0001-00
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO BIONDI LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO VITORIA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TAQUARITINGA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38605' name = 'i16041' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.025.107/0001-94' language=JavaScript onMouseMove='' onClick=jogaform('38605');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38605&estado=SP&municipio=SAO PAULO">
             00.025.107/0001-94
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO DE SERVICOS M C P LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO DE SERVICO M C P LTDA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31704' name = 'i16040' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.025.108/0001-39' language=JavaScript onMouseMove='' onClick=jogaform('31704');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31704&estado=SP&municipio=CRUZALIA">
             00.025.108/0001-39
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO BIDU III LTDA - EPP</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO BIDU III</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CRUZALIA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31238' name = 'i16039' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.025.345/0001-08' language=JavaScript onMouseMove='' onClick=jogaform('31238');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31238&estado=SP&municipio=BOM JESUS DOS PERDOES">
             00.025.345/0001-08
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO MAGGA LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO DEL CARMEN DE LA GALICIA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BOM JESUS DOS PERDOES</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 14/09/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36581' name = 'i16038' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.025.605/0001-37' language=JavaScript onMouseMove='' onClick=jogaform('36581');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36581&estado=SP&municipio=SAO PAULO">
             00.025.605/0001-37
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MAXXI POSTO DE SERVICOS LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MAXXI</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 18/09/2013</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32587' name = 'i16037' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.026.909/0001-19' language=JavaScript onMouseMove='' onClick=jogaform('32587');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32587&estado=SP&municipio=ITAPETININGA">
             00.026.909/0001-19
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MOREIRA & MOREIRA LTA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO BELA VISTA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ITAPETININGA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33420' name = 'i16036' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.026.947/0001-71' language=JavaScript onMouseMove='' onClick=jogaform('33420');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33420&estado=SP&municipio=MOGI DAS CRUZES">
             00.026.947/0001-71
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CENTRAL DE TAIACUPEBA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>R</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MOGI DAS CRUZES</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38604' name = 'i16035' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.021/0001-09' language=JavaScript onMouseMove='' onClick=jogaform('38604');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38604&estado=SP&municipio=SAO PAULO">
             00.027.021/0001-09
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>CLASSE A SERVICOS AUTOMOTIVOS LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 01/08/2012</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34706' name = 'i16034' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.372/0001-01' language=JavaScript onMouseMove='' onClick=jogaform('34706');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34706&estado=SP&municipio=RIBEIRAO PRETO">
             00.027.372/0001-01
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO PARQUE RIBEIRAO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROMAX</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RIBEIRAO PRETO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56580' name = 'i16033' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.493/0001-53' language=JavaScript onMouseMove='' onClick=jogaform('56580');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56580&estado=SP&municipio=IGUAPE">
             00.027.493/0001-53
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO MAR PEQUENO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MAR PEQUENO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IGUAPE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MERCOIL - 07/05/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38603' name = 'i16032' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.640/0001-95' language=JavaScript onMouseMove='' onClick=jogaform('38603');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38603&estado=SP&municipio=SAO PAULO">
             00.027.640/0001-95
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COPA 94 AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COPA 94 AUTO POSTO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57992' name = 'i16031' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.652/0001-10' language=JavaScript onMouseMove='' onClick=jogaform('57992');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57992&estado=SP&municipio=PRESIDENTE PRUDENTE">
             00.027.652/0001-10
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>TANCREDO POSTO DE SERVICO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO TANCREDO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PRESIDENTE PRUDENTE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 07/06/2004</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33699' name = 'i16030' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.751/0001-00' language=JavaScript onMouseMove='' onClick=jogaform('33699');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33699&estado=SP&municipio=NOVA GRANADA">
             00.027.751/0001-00
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SANTOS REIS & SANTOS LTDA - ME</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>NOVA GRANADA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 18/01/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33979' name = 'i16029' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.843/0001-81' language=JavaScript onMouseMove='' onClick=jogaform('33979');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33979&estado=SP&municipio=PEDRA BELA">
             00.027.843/0001-81
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO PEDRA BELA LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO PEDRA BELA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PEDRA BELA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 21/09/2006</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31201' name = 'i16028' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.905/0001-55' language=JavaScript onMouseMove='' onClick=jogaform('31201');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31201&estado=SP&municipio=BAURU">
             00.027.905/0001-55
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>DUQUE COMERCIO DE DERIVADOS DE PETROLEO</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO XINGU</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BAURU</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38602' name = 'i16027' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.027.989/0001-27' language=JavaScript onMouseMove='' onClick=jogaform('38602');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38602&estado=SP&municipio=SAO PAULO">
             00.027.989/0001-27
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MARTE POSTO DE SERVICOS LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MARTE POSTO DE SERVICOS</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33703' name = 'i16026' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.028.369/0001-02' language=JavaScript onMouseMove='' onClick=jogaform('33703');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33703&estado=SP&municipio=NOVA INDEPENDENCIA">
             00.028.369/0001-02
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>HIDALGO & SILVA JUNIOR LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO SÃO PAULO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>NOVA INDEPENDENCIA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34705' name = 'i16025' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.028.642/0001-07' language=JavaScript onMouseMove='' onClick=jogaform('34705');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34705&estado=SP&municipio=RIBEIRAO PRETO">
             00.028.642/0001-07
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>APRISCO AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO APRISCO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RIBEIRAO PRETO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36810' name = 'i16024' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.028.849/0001-73' language=JavaScript onMouseMove='' onClick=jogaform('36810');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36810&estado=SP&municipio=SAO PAULO">
             00.028.849/0001-73
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PAULISTA CENTER AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PAULISTA CENTER</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 26/09/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36927' name = 'i16023' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.029.312/0001-28' language=JavaScript onMouseMove='' onClick=jogaform('36927');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36927&estado=SP&municipio=SAO PAULO">
             00.029.312/0001-28
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>CENTRAL DE ITAQUERA AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO ITAQUERA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36505' name = 'i16022' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.029.804/0001-13' language=JavaScript onMouseMove='' onClick=jogaform('36505');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36505&estado=SP&municipio=SAO PAULO">
             00.029.804/0001-13
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CENTRO AUTOMOTIVO DUMONT LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36904' name = 'i16021' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.029.834/0001-20' language=JavaScript onMouseMove='' onClick=jogaform('36904');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36904&estado=SP&municipio=SAO PAULO">
             00.029.834/0001-20
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO POL 1</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POL1</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MERCOIL - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58665' name = 'i16020' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.030.020/0001-05' language=JavaScript onMouseMove='' onClick=jogaform('58665');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58665&estado=SP&municipio=SERRANA">
             00.030.020/0001-05
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO BELA VISTA DE SERRANA LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO BELA VISTA DE SERRANA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SERRANA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36902' name = 'i16019' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.030.377/0001-93' language=JavaScript onMouseMove='' onClick=jogaform('36902');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36902&estado=SP&municipio=SAO PAULO">
             00.030.377/0001-93
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO DONA RAQUEL LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>DONA RAQUEL</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MERCOIL - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58584' name = 'i16018' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.035.200/0001-80' language=JavaScript onMouseMove='' onClick=jogaform('58584');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58584&estado=SP&municipio=SAO JOSE DOS CAMPOS">
             00.035.200/0001-80
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CENTRO AUTOMOTIVO ATUAL LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO JOSE DOS CAMPOS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 20/05/2015</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='30897' name = 'i16017' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.106.382/0001-32' language=JavaScript onMouseMove='' onClick=jogaform('30897');>
             <!--
             <a href="resultado.asp?sRegRevendedor=30897&estado=SP&municipio=ATIBAIA">
             00.106.382/0001-32
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO SÃO LOURENÇO DE ATIBAIA LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO SÃO LOURENÇO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ATIBAIA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 29/03/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34199' name = 'i16016' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.109.251/0001-09' language=JavaScript onMouseMove='' onClick=jogaform('34199');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34199&estado=SP&municipio=PIRACICABA">
             00.109.251/0001-09
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>DEGASPARI RIVIERA COM.  DE COMBUSTIVEIS LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>DEGASPARI RIVIERA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PIRACICABA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38601' name = 'i16015' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.112.612/0001-76' language=JavaScript onMouseMove='' onClick=jogaform('38601');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38601&estado=SP&municipio=SAO PAULO">
             00.112.612/0001-76
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALBERTO ARMANDO FORTE</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALBERTO ARMANDO FORTE</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57626' name = 'i16014' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.115.933/0001-24' language=JavaScript onMouseMove='' onClick=jogaform('57626');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57626&estado=SP&municipio=PENAPOLIS">
             00.115.933/0001-24
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ZAQUEU & ZAQUEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO ELDORADO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PENAPOLIS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31726' name = 'i16013' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.117.290/0001-58' language=JavaScript onMouseMove='' onClick=jogaform('31726');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31726&estado=SP&municipio=CRUZEIRO">
             00.117.290/0001-58
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MICHELONI PINTO MOREIRA E FILHO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO SETE</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>CRUZEIRO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='30951' name = 'i16012' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.117.348/0001-63' language=JavaScript onMouseMove='' onClick=jogaform('30951');>
             <!--
             <a href="resultado.asp?sRegRevendedor=30951&estado=SP&municipio=AVARE">
             00.117.348/0001-63
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO TROPICAL DE AVARÉ LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AVARE</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MERCOIL - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='30949' name = 'i16011' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.117.348/0002-44' language=JavaScript onMouseMove='' onClick=jogaform('30949');>
             <!--
             <a href="resultado.asp?sRegRevendedor=30949&estado=SP&municipio=AVARE">
             00.117.348/0002-44
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO TROPICAL DE AVARÉ LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO TROPICAL DE AVARÉ II</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AVARE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 10/10/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38600' name = 'i16010' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.119.377/0001-64' language=JavaScript onMouseMove='' onClick=jogaform('38600');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38600&estado=SP&municipio=SAO PAULO">
             00.119.377/0001-64
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO JEMINA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>JEMINA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57799' name = 'i16009' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.125.759/0001-09' language=JavaScript onMouseMove='' onClick=jogaform('57799');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57799&estado=SP&municipio=PORTO FERREIRA">
             00.125.759/0001-09
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MIC PORTO LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MIC PORTO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PORTO FERREIRA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 13/03/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='215744' name = 'i16008' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.126.464/0001-49' language=JavaScript onMouseMove='' onClick=jogaform('215744');>
             <!--
             <a href="resultado.asp?sRegRevendedor=215744&estado=SP&municipio=SAO PAULO">
             00.126.464/0001-49
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>HELICENTRO LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 07/11/2014</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38599' name = 'i16007' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.129.505/0001-50' language=JavaScript onMouseMove='' onClick=jogaform('38599');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38599&estado=SP&municipio=SAO PAULO">
             00.129.505/0001-50
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO 9 LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO GRACIE</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35437' name = 'i16006' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.135.799/0001-23' language=JavaScript onMouseMove='' onClick=jogaform('35437');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35437&estado=SP&municipio=SANTOS">
             00.135.799/0001-23
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO BRUMAR LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO BRUMAR</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SANTOS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33889' name = 'i16005' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.136.766/0001-06' language=JavaScript onMouseMove='' onClick=jogaform('33889');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33889&estado=SP&municipio=PARAPUA">
             00.136.766/0001-06
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SOUSA & LINGIARDI LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO SOUSA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PARAPUA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 19/03/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56815' name = 'i16004' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.138.367/0001-76' language=JavaScript onMouseMove='' onClick=jogaform('56815');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56815&estado=SP&municipio=ITAQUAQUECETUBA">
             00.138.367/0001-76
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>J F D AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ITAQUAQUECETUBA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35278' name = 'i16003' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.138.629/0001-00' language=JavaScript onMouseMove='' onClick=jogaform('35278');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35278&estado=SP&municipio=SANTO ANDRE">
             00.138.629/0001-00
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO DE SERVIÇOS REQUINTE LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SANTO ANDRE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 16/11/2015</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56077' name = 'i16002' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.140.019/0001-33' language=JavaScript onMouseMove='' onClick=jogaform('56077');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56077&estado=SP&municipio=CAMPINAS">
             00.140.019/0001-33
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>L. C. GOMES & GOMES LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>L. C. GOMES & GOMES LTDA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CAMPINAS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='39235' name = 'i16001' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.142.822/0001-07' language=JavaScript onMouseMove='' onClick=jogaform('39235');>
             <!--
             <a href="resultado.asp?sRegRevendedor=39235&estado=SP&municipio=URANIA">
             00.142.822/0001-07
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO URANIA LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO URANIA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>URANIA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 26/01/2016</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36560' name = 'i16000' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.144.051/0001-97' language=JavaScript onMouseMove='' onClick=jogaform('36560');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36560&estado=SP&municipio=SAO PAULO">
             00.144.051/0001-97
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO SANTA CLARA DE ASSIS LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO SANTA CLARA DE ASSIS LTDA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 31/03/2007</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57233' name = 'i15999' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.146.450/0001-97' language=JavaScript onMouseMove='' onClick=jogaform('57233');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57233&estado=SP&municipio=LIMEIRA">
             00.146.450/0001-97
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO COLINAS DE SAO JOAO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>LIMEIRA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='39219' name = 'i15998' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.154.858/0001-00' language=JavaScript onMouseMove='' onClick=jogaform('39219');>
             <!--
             <a href="resultado.asp?sRegRevendedor=39219&estado=SP&municipio=TORRE DE PEDRA">
             00.154.858/0001-00
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MARCO ANTONIO AMARO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO TORRE DE PEDRA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TORRE DE PEDRA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AGIP DISTRIBUIDORA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38598' name = 'i15997' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.158.433/0001-70' language=JavaScript onMouseMove='' onClick=jogaform('38598');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38598&estado=SP&municipio=SAO PAULO">
             00.158.433/0001-70
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO 43 LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 28/03/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38597' name = 'i15996' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.159.549/0001-23' language=JavaScript onMouseMove='' onClick=jogaform('38597');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38597&estado=SP&municipio=SAO PAULO">
             00.159.549/0001-23
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO RAGUEB LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAM II</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 25/08/2017</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='30999' name = 'i15995' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.160.930/0001-02' language=JavaScript onMouseMove='' onClick=jogaform('30999');>
             <!--
             <a href="resultado.asp?sRegRevendedor=30999&estado=SP&municipio=BARIRI">
             00.160.930/0001-02
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO AQUILANTE LTDA - EPP</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO AQUILANTE</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BARIRI</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 10/08/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38691' name = 'i15994' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.160.956/0001-50' language=JavaScript onMouseMove='' onClick=jogaform('38691');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38691&estado=SP&municipio=SARAPUI">
             00.160.956/0001-50
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO E EMPORIO NOVA LAVAPES LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SARAPUI</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TOWER - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56649' name = 'i15993' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.161.122/0001-60' language=JavaScript onMouseMove='' onClick=jogaform('56649');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56649&estado=SP&municipio=INUBIA PAULISTA">
             00.161.122/0001-60
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>GUSTAVO HIDEKI FUKUDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>INUBIA PAULISTA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 15/02/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31298' name = 'i15992' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.163.056/0001-67' language=JavaScript onMouseMove='' onClick=jogaform('31298');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31298&estado=SP&municipio=CACAPAVA">
             00.163.056/0001-67
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CEREJEIRA DO VALE LTDA - EPP</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CACAPAVA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='244360' name = 'i15991' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.163.056/0002-48' language=JavaScript onMouseMove='' onClick=jogaform('244360');>
             <!--
             <a href="resultado.asp?sRegRevendedor=244360&estado=SP&municipio=TAUBATE">
             00.163.056/0002-48
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CEREJEIRA DO VALE LTDA - EPP</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>TAUBATE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 12/09/2017</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35288' name = 'i15990' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.165.510/0001-19' language=JavaScript onMouseMove='' onClick=jogaform('35288');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35288&estado=SP&municipio=SANTO ANTONIO DO ARACANGUA">
             00.165.510/0001-19
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>VERISSIMO & SILVA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO VICENTINOPOLIS</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SANTO ANTONIO DO ARACANGUA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 19/12/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34489' name = 'i15989' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.253/0001-30' language=JavaScript onMouseMove='' onClick=jogaform('34489');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34489&estado=SP&municipio=RIBEIRAO PRETO">
             00.166.253/0001-30
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>REAL COMERCIO DE COMBUSTIVEIS LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO REAL</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RIBEIRAO PRETO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 18/04/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34729' name = 'i15988' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0025-15' language=JavaScript onMouseMove='' onClick=jogaform('34729');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34729&estado=SP&municipio=RIO CLARO">
             00.166.290/0025-15
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RIO CLARO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 08/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55353' name = 'i15987' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0026-04' language=JavaScript onMouseMove='' onClick=jogaform('55353');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55353&estado=SP&municipio=ASSIS">
             00.166.290/0026-04
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ASSIS</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 17/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55352' name = 'i15986' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0027-87' language=JavaScript onMouseMove='' onClick=jogaform('55352');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55352&estado=SP&municipio=ASSIS">
             00.166.290/0027-87
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ASSIS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 17/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58781' name = 'i15985' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0028-68' language=JavaScript onMouseMove='' onClick=jogaform('58781');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58781&estado=SP&municipio=TATUI">
             00.166.290/0028-68
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO TATUÍ</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>TATUI</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 18/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38787' name = 'i15984' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0029-49' language=JavaScript onMouseMove='' onClick=jogaform('38787');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38787&estado=SP&municipio=SOROCABA">
             00.166.290/0029-49
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 08/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55031' name = 'i15983' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0030-82' language=JavaScript onMouseMove='' onClick=jogaform('55031');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55031&estado=SP&municipio=AMERICANA">
             00.166.290/0030-82
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AMERICANA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 01/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34069' name = 'i15982' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0031-63' language=JavaScript onMouseMove='' onClick=jogaform('34069');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34069&estado=SP&municipio=PIRACICABA">
             00.166.290/0031-63
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PIRACICABA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 17/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58993' name = 'i15981' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0032-44' language=JavaScript onMouseMove='' onClick=jogaform('58993');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58993&estado=SP&municipio=VINHEDO">
             00.166.290/0032-44
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>VINHEDO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 10/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32839' name = 'i15980' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0033-25' language=JavaScript onMouseMove='' onClick=jogaform('32839');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32839&estado=SP&municipio=JUNDIAI">
             00.166.290/0033-25
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>JUNDIAI</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 08/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32840' name = 'i15979' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0034-06' language=JavaScript onMouseMove='' onClick=jogaform('32840');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32840&estado=SP&municipio=JUNDIAI">
             00.166.290/0034-06
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>JUNDIAI</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 01/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32841' name = 'i15978' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0035-97' language=JavaScript onMouseMove='' onClick=jogaform('32841');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32841&estado=SP&municipio=JUNDIAI">
             00.166.290/0035-97
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>JUNDIAI</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 01/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36132' name = 'i15977' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0036-78' language=JavaScript onMouseMove='' onClick=jogaform('36132');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36132&estado=SP&municipio=SAO PAULO">
             00.166.290/0036-78
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 18/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='39199' name = 'i15976' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0038-30' language=JavaScript onMouseMove='' onClick=jogaform('39199');>
             <!--
             <a href="resultado.asp?sRegRevendedor=39199&estado=SP&municipio=TIETE">
             00.166.290/0038-30
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TIETE</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 07/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55030' name = 'i15975' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0039-10' language=JavaScript onMouseMove='' onClick=jogaform('55030');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55030&estado=SP&municipio=AMERICANA">
             00.166.290/0039-10
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AMERICANA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 07/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35064' name = 'i15974' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0040-54' language=JavaScript onMouseMove='' onClick=jogaform('35064');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35064&estado=SP&municipio=SANTANA DE PARNAIBA">
             00.166.290/0040-54
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO ALPHAVILLE</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SANTANA DE PARNAIBA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 01/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='34070' name = 'i15973' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0041-35' language=JavaScript onMouseMove='' onClick=jogaform('34070');>
             <!--
             <a href="resultado.asp?sRegRevendedor=34070&estado=SP&municipio=PIRACICABA">
             00.166.290/0041-35
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PIRACICABA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 07/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31041' name = 'i15972' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0042-16' language=JavaScript onMouseMove='' onClick=jogaform('31041');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31041&estado=SP&municipio=BAURU">
             00.166.290/0042-16
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BAURU</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 17/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36140' name = 'i15971' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0043-05' language=JavaScript onMouseMove='' onClick=jogaform('36140');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36140&estado=SP&municipio=SAO PAULO">
             00.166.290/0043-05
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 01/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36141' name = 'i15970' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0044-88' language=JavaScript onMouseMove='' onClick=jogaform('36141');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36141&estado=SP&municipio=SAO PAULO">
             00.166.290/0044-88
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 01/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36135' name = 'i15969' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0045-69' language=JavaScript onMouseMove='' onClick=jogaform('36135');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36135&estado=SP&municipio=SAO PAULO">
             00.166.290/0045-69
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO PELICANO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 10/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57146' name = 'i15968' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0046-40' language=JavaScript onMouseMove='' onClick=jogaform('57146');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57146&estado=SP&municipio=LIMEIRA">
             00.166.290/0046-40
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO LIMEIRÃO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>LIMEIRA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 17/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57515' name = 'i15967' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0047-20' language=JavaScript onMouseMove='' onClick=jogaform('57515');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57515&estado=SP&municipio=OSVALDO CRUZ">
             00.166.290/0047-20
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OSVALDO CRUZ</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 10/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36078' name = 'i15966' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0048-01' language=JavaScript onMouseMove='' onClick=jogaform('36078');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36078&estado=SP&municipio=SAO PAULO">
             00.166.290/0048-01
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BURGUESE</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 08/05/2006</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35107' name = 'i15965' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0050-26' language=JavaScript onMouseMove='' onClick=jogaform('35107');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35107&estado=SP&municipio=SANTO ANDRE">
             00.166.290/0050-26
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SANTO ANDRE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 01/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36131' name = 'i15964' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0051-07' language=JavaScript onMouseMove='' onClick=jogaform('36131');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36131&estado=SP&municipio=SAO PAULO">
             00.166.290/0051-07
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 18/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36133' name = 'i15963' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0052-98' language=JavaScript onMouseMove='' onClick=jogaform('36133');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36133&estado=SP&municipio=SAO PAULO">
             00.166.290/0052-98
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO IPIRANGA</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 17/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36077' name = 'i15962' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0053-79' language=JavaScript onMouseMove='' onClick=jogaform('36077');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36077&estado=SP&municipio=SAO PAULO">
             00.166.290/0053-79
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO SANTA RITA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 04/10/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36139' name = 'i15961' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.290/0054-50' language=JavaScript onMouseMove='' onClick=jogaform('36139');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36139&estado=SP&municipio=SAO PAULO">
             00.166.290/0054-50
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>OPERADORA DE POSTOS E SERVICOS LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALE COMBUSTÍVEIS - 01/03/2005</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31520' name = 'i15960' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.166.555/0001-08' language=JavaScript onMouseMove='' onClick=jogaform('31520');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31520&estado=SP&municipio=CATANDUVA">
             00.166.555/0001-08
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>NARDI COMERCIO DE COMBUST. E DERIV. DE PETROLEO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CATANDUVA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 05/10/2016</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57692' name = 'i15959' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.167.309/0001-70' language=JavaScript onMouseMove='' onClick=jogaform('57692');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57692&estado=SP&municipio=PINDAMONHANGABA">
             00.167.309/0001-70
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RUFINO DE SOUZA & PUCCI LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO TREVO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PINDAMONHANGABA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 22/10/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58583' name = 'i15958' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.168.947/0001-06' language=JavaScript onMouseMove='' onClick=jogaform('58583');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58583&estado=SP&municipio=SAO JOSE DOS CAMPOS">
             00.168.947/0001-06
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>EXCELENCIA AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO JOSE DOS CAMPOS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55324' name = 'i15957' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.169.071/0001-12' language=JavaScript onMouseMove='' onClick=jogaform('55324');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55324&estado=SP&municipio=ARARAS">
             00.169.071/0001-12
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO BELVEDERE DE ARARAS LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ARARAS</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AGIP DISTRIBUIDORA - 27/09/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56076' name = 'i15956' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.170.071/0001-32' language=JavaScript onMouseMove='' onClick=jogaform('56076');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56076&estado=SP&municipio=CAMPINAS">
             00.170.071/0001-32
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IMPERIO POSTO DE SERVICOS LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CAMPINAS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38596' name = 'i15955' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.170.259/0001-80' language=JavaScript onMouseMove='' onClick=jogaform('38596');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38596&estado=SP&municipio=SAO PAULO">
             00.170.259/0001-80
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO GASOCENTER LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>GASOCENTER</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36664' name = 'i15954' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.170.487/0001-50' language=JavaScript onMouseMove='' onClick=jogaform('36664');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36664&estado=SP&municipio=SAO PAULO">
             00.170.487/0001-50
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CIDADE VARGAS LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 18/04/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38595' name = 'i15953' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.174.576/0001-75' language=JavaScript onMouseMove='' onClick=jogaform('38595');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38595&estado=SP&municipio=SAO PAULO">
             00.174.576/0001-75
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ALMIR CAMARGO PAGLIARI</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SERVE CENTRO CANTAGALO - 55333</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58347' name = 'i15952' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.175.079/0001-91' language=JavaScript onMouseMove='' onClick=jogaform('58347');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58347&estado=SP&municipio=SAO CARLOS">
             00.175.079/0001-91
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CIDADE ARACY LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CIDADE ARACY</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO CARLOS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROFORTE - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55049' name = 'i15951' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.182.523/0001-04' language=JavaScript onMouseMove='' onClick=jogaform('55049');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55049&estado=SP&municipio=AMERICANA">
             00.182.523/0001-04
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>CRISTIANO SAMMARONE</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO CINCO ESTRELAS</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AMERICANA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38594' name = 'i15950' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.182.538/0001-64' language=JavaScript onMouseMove='' onClick=jogaform('38594');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38594&estado=SP&municipio=SAO PAULO">
             00.182.538/0001-64
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO DE SERVIÇOS XV DE NOVEMBRO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58813' name = 'i15949' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.186.497/0001-84' language=JavaScript onMouseMove='' onClick=jogaform('58813');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58813&estado=SP&municipio=TATUI">
             00.186.497/0001-84
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ROBERTI & ROBERTI AUTO POSTO LTDA. - EPP</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>REDE VICTORIO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>TATUI</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 09/12/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38593' name = 'i15948' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.186.690/0001-15' language=JavaScript onMouseMove='' onClick=jogaform('38593');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38593&estado=SP&municipio=SAO PAULO">
             00.186.690/0001-15
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COLONIA COM E SERV DE COMBUSTIVEIS E LUBRIFICANTES LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>COLINIA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56465' name = 'i15947' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.190.001/0001-46' language=JavaScript onMouseMove='' onClick=jogaform('56465');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56465&estado=SP&municipio=GUARUJA">
             00.190.001/0001-46
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO PRAIA DE PERNAMBUCO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PRAIA DE PERNAMBUCO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>GUARUJA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33864' name = 'i15946' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.196.039/0001-26' language=JavaScript onMouseMove='' onClick=jogaform('33864');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33864&estado=SP&municipio=PANORAMA">
             00.196.039/0001-26
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>A. H. F. SAHELI</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO AVENIDA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PANORAMA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31341' name = 'i15945' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.197.769/0001-41' language=JavaScript onMouseMove='' onClick=jogaform('31341');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31341&estado=SP&municipio=CAIABU">
             00.197.769/0001-41
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MARISA GOMES MONTEIRO</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO CAIABU</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>CAIABU</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38592' name = 'i15944' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.200.457/0001-40' language=JavaScript onMouseMove='' onClick=jogaform('38592');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38592&estado=SP&municipio=SAO PAULO">
             00.200.457/0001-40
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AGUIA DA MARGINAL AUTO POSTO LIMITADA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 06/06/2017</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33159' name = 'i15943' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.203.959/0001-24' language=JavaScript onMouseMove='' onClick=jogaform('33159');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33159&estado=SP&municipio=MARILIA">
             00.203.959/0001-24
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO PALADIUM DE MARÍLIA LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO PALADIUM</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MARILIA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35291' name = 'i15942' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.206.836/0001-47' language=JavaScript onMouseMove='' onClick=jogaform('35291');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35291&estado=SP&municipio=SANTO ANTONIO DO JARDIM">
             00.206.836/0001-47
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TRINCHA & TRINCHA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO SAO CRISTOVAO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SANTO ANTONIO DO JARDIM</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 16/10/2006</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55685' name = 'i15941' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.206.850/0001-40' language=JavaScript onMouseMove='' onClick=jogaform('55685');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55685&estado=SP&municipio=BOTUCATU">
             00.206.850/0001-40
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CONDE DE SERRA NEGRA LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BOTUCATU</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 03/04/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58908' name = 'i15940' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.207.826/0001-26' language=JavaScript onMouseMove='' onClick=jogaform('58908');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58908&estado=SP&municipio=UBATUBA">
             00.207.826/0001-26
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO TROVAO</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>UBATUBA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>MERCOIL - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33868' name = 'i15939' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.210.913/0001-32' language=JavaScript onMouseMove='' onClick=jogaform('33868');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33868&estado=SP&municipio=PARAIBUNA">
             00.210.913/0001-32
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO KORUJÃO PARAIBUNA LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO KORUJÃO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PARAIBUNA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 30/01/2003</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58582' name = 'i15938' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.211.123/0001-71' language=JavaScript onMouseMove='' onClick=jogaform('58582');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58582&estado=SP&municipio=SAO JOSE DOS CAMPOS">
             00.211.123/0001-71
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO GIRASSOL LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO JOSE DOS CAMPOS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38925' name = 'i15937' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.211.778/0001-40' language=JavaScript onMouseMove='' onClick=jogaform('38925');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38925&estado=SP&municipio=SOROCABA">
             00.211.778/0001-40
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO JULIO DE MESQUITA FILHO LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SOROCABA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 24/01/2012</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38591' name = 'i15936' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.215.728/0001-30' language=JavaScript onMouseMove='' onClick=jogaform('38591');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38591&estado=SP&municipio=SAO PAULO">
             00.215.728/0001-30
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>JOSE NELSON AGUIAR FERNANDES POSTO DE GASOLINA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>JNAF POSTO GASOLINA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/05/2011</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32742' name = 'i15935' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.216.977/0001-40' language=JavaScript onMouseMove='' onClick=jogaform('32742');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32742&estado=SP&municipio=JAU">
             00.216.977/0001-40
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CONTINENTAL DE JAU EIRELI LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO CONTINENTAL</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>JAU</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 15/09/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='57232' name = 'i15934' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.218.244/0001-45' language=JavaScript onMouseMove='' onClick=jogaform('57232');>
             <!--
             <a href="resultado.asp?sRegRevendedor=57232&estado=SP&municipio=LIMEIRA">
             00.218.244/0001-45
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>FERREIRA E LOPES AUTO POSTO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO BEIRA RIO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>LIMEIRA</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58086' name = 'i15933' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.218.703/0001-90' language=JavaScript onMouseMove='' onClick=jogaform('58086');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58086&estado=SP&municipio=RIFAINA">
             00.218.703/0001-90
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO RIFAINAO LTDA - EPP</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO RIFAINAO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RIFAINA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='35785' name = 'i15932' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.218.801/0001-28' language=JavaScript onMouseMove='' onClick=jogaform('35785');>
             <!--
             <a href="resultado.asp?sRegRevendedor=35785&estado=SP&municipio=SAO JOSE DO RIO PRETO">
             00.218.801/0001-28
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ADALFREDO FERRISI RIO PRETO</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO FERRISI</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO JOSE DO RIO PRETO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='30846' name = 'i15931' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.218.960/0001-22' language=JavaScript onMouseMove='' onClick=jogaform('30846');>
             <!--
             <a href="resultado.asp?sRegRevendedor=30846&estado=SP&municipio=ARARAQUARA">
             00.218.960/0001-22
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>REYSSOL COMERCIO E SERVIÇOS LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO GIRASSOL</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>ARARAQUARA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 24/01/2002</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='36551' name = 'i15930' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.218.986/0001-70' language=JavaScript onMouseMove='' onClick=jogaform('36551');>
             <!--
             <a href="resultado.asp?sRegRevendedor=36551&estado=SP&municipio=SAO PAULO">
             00.218.986/0001-70
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO TETRA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>TETRA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROFORTE - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55603' name = 'i15929' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.218.992/0001-28' language=JavaScript onMouseMove='' onClick=jogaform('55603');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55603&estado=SP&municipio=BEBEDOURO">
             00.218.992/0001-28
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO PETROCAP LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROCAP</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BEBEDOURO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROFORTE - 11/05/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32601' name = 'i15928' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.222.130/0001-79' language=JavaScript onMouseMove='' onClick=jogaform('32601');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32601&estado=SP&municipio=ITAPEVI">
             00.222.130/0001-79
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO JORNADA LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO JORNADA LTDA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ITAPEVI</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/10/2012</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32721' name = 'i15927' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.224.409/0001-91' language=JavaScript onMouseMove='' onClick=jogaform('32721');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32721&estado=SP&municipio=JARDINOPOLIS">
             00.224.409/0001-91
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>RAUL GUIMARAES JUNIOR</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>JARDINOPOLIS</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 04/11/2009</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56777' name = 'i15926' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.225.260/0001-65' language=JavaScript onMouseMove='' onClick=jogaform('56777');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56777&estado=SP&municipio=ITAPOLIS">
             00.225.260/0001-65
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>BATISTA SILVEIRA & SILVEIRA LTDA.</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO SILVEIRA</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>ITAPOLIS</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AGIP DISTRIBUIDORA - 29/03/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='58843' name = 'i15925' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.225.489/0001-08' language=JavaScript onMouseMove='' onClick=jogaform('58843');>
             <!--
             <a href="resultado.asp?sRegRevendedor=58843&estado=SP&municipio=TREMEMBE">
             00.225.489/0001-08
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO VALLE DO SOL ARR LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSTO COLORADO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>TREMEMBE</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AGIP DISTRIBUIDORA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38590' name = 'i15924' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.226.307/0001-05' language=JavaScript onMouseMove='' onClick=jogaform('38590');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38590&estado=SP&municipio=SAO PAULO">
             00.226.307/0001-05
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CENTRO AUTOMOTICO CANCUN LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='55626' name = 'i15923' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.226.807/0001-47' language=JavaScript onMouseMove='' onClick=jogaform('55626');>
             <!--
             <a href="resultado.asp?sRegRevendedor=55626&estado=SP&municipio=BIRIGUI">
             00.226.807/0001-47
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO SCUCUGLIA E OLIVEIRA LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO MODELO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BIRIGUI</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>IPIRANGA - 14/01/2015</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32096' name = 'i15922' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.227.847/0001-03' language=JavaScript onMouseMove='' onClick=jogaform('32096');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32096&estado=SP&municipio=GENERAL SALGADO">
             00.227.847/0001-03
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSSETTI & POSSETTI LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO GENERAL</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>GENERAL SALGADO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 18/01/2016</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='32097' name = 'i15921' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.227.847/0002-94' language=JavaScript onMouseMove='' onClick=jogaform('32097');>
             <!--
             <a href="resultado.asp?sRegRevendedor=32097&estado=SP&municipio=GENERAL SALGADO">
             00.227.847/0002-94
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>POSSETTI & POSSETTI LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>MALIBU AUTO POSTO</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>GENERAL SALGADO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='31374' name = 'i15920' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.229.487/0001-89' language=JavaScript onMouseMove='' onClick=jogaform('31374');>
             <!--
             <a href="resultado.asp?sRegRevendedor=31374&estado=SP&municipio=CAJAMAR">
             00.229.487/0001-89
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO ESTILO LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>POSTO ESTILO</font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CAJAMAR</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>RAIZEN - 02/07/2001</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='33993' name = 'i15919' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.230.753/0001-93' language=JavaScript onMouseMove='' onClick=jogaform('33993');>
             <!--
             <a href="resultado.asp?sRegRevendedor=33993&estado=SP&municipio=PEDRO DE TOLEDO">
             00.230.753/0001-93
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>AUTO POSTO DE SERVIÇOS EDE LTDA</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1></font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PEDRO DE TOLEDO</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>BANDEIRA BRANCA - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#d7d7d7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='38589' name = 'i15918' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#d7d7d7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.231.439/0001-25' language=JavaScript onMouseMove='' onClick=jogaform('38589');>
             <!--
             <a href="resultado.asp?sRegRevendedor=38589&estado=SP&municipio=SAO PAULO">
             00.231.439/0001-25
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>CENTRO AUTOMOTIVO ATENAS LTDA</font></td>          <td width=140 bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1> </font></td>          <td width=20  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>SAO PAULO</font></td>          <td width=40  bgcolor='#d7d7d7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 05/06/2000</font></td>        </tr>        <tr>
             <td width=180 bgcolor=#e7e7e7 VALIGN=TOP><font face=Verdana size=1>
             <input Type=hidden Value='56515' name = 'i15917' ><input style='TEXT-DECORATION:underline;cursor:Hand;color:blue;Background:#e7e7e7;BORDER-TOP-STYLE: none; BORDER-RIGHT-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none' Type=button Value='00.232.539/0001-76' language=JavaScript onMouseMove='' onClick=jogaform('56515');>
             <!--
             <a href="resultado.asp?sRegRevendedor=56515&estado=SP&municipio=GUARUJA">
             00.232.539/0001-76
             </a>
             -->
             </font>
             </td>
                       <td width=150 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>P.R.L. PETROLEO LTDA.</font></td>          <td width=140 bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>P.R.L. PETROLEO LTDA.</font></td>          <td width=20  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>SP</font></td>          <td width=50  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>GUARUJA</font></td>          <td width=40  bgcolor='#e7e7e7' VALIGN=TOP><font face=Verdana size=1>PETROBRAS DISTRIBUIDORA S.A. - 22/02/2012</font></td>        </tr>        <tr>          <td bgcolor=#e7e7e7 colspan=7><font face=Verdana size=1 color=#666666><b>200  Registro(s)</b></font></td>        </tr>    </table>
    <center>
    <Table Border="0" Cellpadding="0" Cellspacing="0" >
		<tr>
		 
			   <td>
				 <form 	Method="Post"
						Action="index.asp"
						Name="formNext">
						<input 	Type="button"
								Value="Próximo(s) 200 "
								name="Submit3"
								onClick="document.frmPesquisa.p.value='2';Submeter()">
				 </form>
			   </td>
		
		</tr>
	</table>
	</center>
	</table>

	</TABLE>
	</table>

	<form Method="Post" Action="resultado.asp"   name="frmResultado">
		<input Type="hidden" Value="" name = "Cod_inst">
		<input Type="hidden" Value="" name = "estado">
		<input Type="hidden" Value="" name = "municipio">
	</form>



<!-- corpo do consulta de postos -->
<!-- Termino da tabela do moldura principal -->
<tr>
<td colspan="2">&nbsp;</td>
</tr>
</table>
<!-- fim tabela moldura principal -->

</BODY>
</HTML>
"""

@pytest.fixture
def station_detail():
    return """


<HTML>
<head>
	<title>:: ANP - Agência Nacional de Petróleo ::</title>
	<!--
	<link rel="STYLESHEET" type="text/css" href="/css/default.css">
	-->
	<style type="text/css">
		@import "/SITE/extras/css/default.css";
	</style>
	<META http-equiv=Content-Type content="text/html; charset=iso-8859-1">
	<meta http-equiv=pragma content=no-cache>
	<meta http-equiv=expires content="Mon, 06 Jan 1990 00:00:01 GMT">
</head>

<script language="JAVASCRIPT">
function ShowHours() 
{
    TodaysHour = new Date()
	horas = TodaysHour.getHours()
	minutos = TodaysHour.getMinutes()
	segundos = TodaysHour.getSeconds()
	if (horas < 10)
		horas= "0" + horas

	if (minutos < 10)
		minutos = "0" + minutos

	if (segundos < 10)
		segundos = "0" + segundos
	
    document.write(horas+":"+minutos+":"+segundos)
}

function ShowTodayDate() 
{
	now = new Date()
	dia = now.getDate()
	mes = now.getMonth() + 1
	ano = now.getYear()

	if (dia < 10)
		dia = "0" + dia
	if (mes < 10)
		mes = "0" + mes
	if (ano < 2000)
		ano = "19" + ano

        if (navigator.appName == "Netscape") 
        {
             if (ano > 1999)  
             ano = "200" + (now.getYear()-100)  
 	    }
        if (navigator.appName == "Netscape") 
        {
             if (ano > 2009) 
	     ano = "20" + (now.getYear()-100)  
	     }
	document.write(dia+"/" +mes+ "/" +ano)
}
</script>

<body leftmargin=0 topmargin=0 marginheight="0" marginwidth="0" bgcolor="#ffffff">
<!-- tabela moldura principal -->

<table width="760" border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="126" bgcolor="#D7D7D7" valign="top">&nbsp;</td>
<td valign="top" width="634">

<!-- fim da tabela moldura principal e inicio do corpo do consulta de postos -->
		<TABLE>
        <!--span class="txtcinza2"><b>Data:</b> <script language="javascript">ShowTodayDate();</script>&nbsp;&nbsp; <b>Hora:</b> <script language="javascript">ShowHours();</script></span-->
        <span class="txtcinza2"><b>Data:</b> 28/10/2017&nbsp;&nbsp; <b>Hora:</b> 14:31:29</span>

</TABLE>

    <!--include virtual="/postos/resultadoquery.asp"-->
    
	<TABLE height=530 cols=1 width=634  border=0>
	  <TBODY>
	  <TR>
	    <TD height=121 valign="top" align="left">
	        <DIV align=left>
	        <table border="0" width=634 cellspacing="3">
	        <tr><td colspan=2 align=right><font face="Arial" size="2"><b><a href="consulta.asp">Nova Consulta</a></b></font></td></tr>
	
	      <tr><td bgcolor=#e7e7e7 colspan=2><font face=verdana color=#666666 size=3><div align="left"><b>Posto com autorização revogada</FONT></b></br></tr></td>
	      <tr><td colspan=2><font face=verdana color=#666666 size=1><br><div align="justify"> </FONT></br>
	      <font face=verdana color=#666666 size=1 bgcolor=#d7d7d7 color=red>A situação cadastral atual não permite a emissão do Certificado.</font><br>
	      <font face=Verdana color=#666666 size=1> </a></font>
	      <font face=Verdana color=#666666 size=1>Caso deseje verificar a autenticidade de Certificado já emitido para este posto, <b><a href="CertificadoConfirmacao.asp?">clique aqui.</a></b></font><br>&nbsp;</td></tr>
	      <tr> <td align=right bgcolor=#e7e7e7 valign=top><font face=Verdana color=#666666 size=1><b>CNPJ/CPF:</b></font></td>            <td valign=top align=left bgcolor=#e7e7e7><font face=Verdana color=#666666 size=1>03.081.666/0001-00</font></td></tr><tr><td align=right bgcolor=#d7d7d7 valign=top><font face=Verdana color=#666666 size=1><b>Razão Social:</b></font></td>            <td valign=top align=left bgcolor=#d7d7d7><font face=Verdana color=#666666 size=1>AUTO POSTO TIMBUIBOM LTDA</font></td></tr><tr><td align=right bgcolor=#e7e7e7 valign=top><font face=Verdana color=#666666 size=1><b>Nome Fantasia:</b></font></td>            <td valign=top align=left bgcolor=#e7e7e7><font face=Verdana color=#666666 size=1>POSTO BELEM</font></td></tr><tr><td align=right bgcolor=#d7d7d7 valign=top><font face=Verdana color=#666666 size=1><b>Endereço:</b></font></td>            <td valign=top align=left bgcolor=#d7d7d7><font face=Verdana color=#666666 size=1>  RODOVIA BR 101, KM 160  S/N&nbsp;</font></td></tr><tr><td align=right bgcolor=#e7e7e7 valign=top><font face=Verdana color=#666666 size=1><b>Complemento:</b></font></td>            <td valign=top align=left bgcolor=#e7e7e7><font face=Verdana color=#666666 size=1>&nbsp;</font></td></tr><tr><td align=right bgcolor=#d7d7d7 valign=top><font face=Verdana color=#666666 size=1><b>Bairro:</b></font></td>            <td valign=top align=left bgcolor=#d7d7d7><font face=Verdana color=#666666 size=1>BEBEDOURO&nbsp;</font></td></tr><tr><td align=right bgcolor=#e7e7e7 valign=top><font face=Verdana color=#666666 size=1><b>Município/UF:</b></font></td>            <td valign=top align=left bgcolor=#e7e7e7><font face=Verdana color=#666666 size=1>LINHARES/ES&nbsp;</font></td></tr><tr><td align=right bgcolor=#d7d7d7 valign=top><font face=Verdana color=#666666 size=1><b>CEP:</b></font></td>            <td valign=top align=left bgcolor=#d7d7d7><font face=Verdana color=#666666 size=1>29900000&nbsp;</font></td></tr><tr><td align=right bgcolor=#e7e7e7 valign=top><font face=Verdana color=#666666 size=1><b>Número Despacho:</b></font></td>            <td valign=top align=left bgcolor=#e7e7e7><font face=Verdana color=#666666 size=1>ANP Nº 982&nbsp;</font></td></tr><tr><td align=right bgcolor=#d7d7d7 valign=top><font face=Verdana color=#666666 size=1><b>Data Publicação:</b></font></td>            <td valign=top align=left bgcolor=#d7d7d7><font face=Verdana color=#666666 size=1>09/07/2015&nbsp;</font></td></tr><tr><td align=right bgcolor=#e7e7e7 valign=top><font face=Verdana color=#666666 size=1><b>Tipo do Posto:</b></font></td>            <td valign=top align=left bgcolor=#e7e7e7><font face=Verdana color=#666666 size=1>REVENDEDOR&nbsp;</font></td>		<!--</ul>&nbsp;</td></tr></table><DIV align=left><table border=0 cellspacing=3 width=100>-->
       
       </ul>&nbsp;</td></tr></table><DIV align=left><table border=0 cellspacing=3 width=280>
                   <tr><td valign=top align=left bgcolor=#FFFFFF><font face=Verdana color=#666666 size=1>&nbsp;</font></td></tr>
       </table>
       </DIV></BLOCKQUOTE></TD></TR>
       </TBODY></TABLE>
    

<!-- fim  do corpo do consulta de postos -->
<!-- termino da tabela moldura principal -->
</td>
</tr>
<tr>
<td colspan="2">&nbsp;</td>
</tr>
</table>
<!-- fim tabela moldura principal -->

</BODY></HTML>
"""