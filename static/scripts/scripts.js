window.addEventListener("load",function(){
    document.getElementById("decipherForm").addEventListener("submit", formSubmit);
    document.getElementById("exampleButton").addEventListener("click", examplePopulate);
    document.getElementById("clearButton").addEventListener("click", clearForm);
});

var formLoading = false;

function doneLoading() {
    document.getElementById("submitbtn").disabled = false;
    formLoading = false;
}

function formSubmit(event) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 || this.status == 200) {
            if (this.responseText) {
                doneLoading();
                var response = JSON.parse(this.responseText);

                if (response.error) {
                    clearPlaintextResult();
                    document.getElementById("errorContainer").classList.remove("hidden");
                    document.getElementById("resultError").innerText = response.message;
                    document.getElementById("loadingContainer").classList.add("hidden");
                } else {
                    clearErrorResult();
                    document.getElementById("resultContainer").classList.remove("hidden");
                    document.getElementById("resultPlaintext").innerText = response.message;
                    document.getElementById("resultKey").innerText = response.key;
                    document.getElementById("resultNote").innerText = response.note;
                    document.getElementById("resultScore").innerText = response.score + "%";
                    document.getElementById("loadingContainer").classList.add("hidden");
                }
            }
        } else if (this.status == 429) {
            doneLoading();            
            clearPlaintextResult();
            document.getElementById("errorContainer").classList.remove("hidden");
            document.getElementById("resultError").innerText = "Please slow down";
            document.getElementById("loadingContainer").classList.add("hidden");
        }
    }

    if (!formLoading) {
        formLoading = true;
        var formCiphertext = document.getElementById("ciphertext").value;
        var formKeylength = document.getElementById("keylength").value;
        var formAuto = document.getElementById("auto").checked;
        var params = "ciphertext=" + formCiphertext + "&keylength=" + formKeylength + "&auto=" + formAuto;

        clearPlaintextResult();
        clearErrorResult();
        document.getElementById("submitbtn").disabled = true;
        document.getElementById("loadingContainer").classList.remove("hidden");

        xhr.open("POST", "/decrypt", true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

        xhr.send(params);
    }

    event.preventDefault();
}

function examplePopulate() {
    document.getElementById("ciphertext").value = `USE QCDLRU DVCN QX TFNFKZ HHKMI DEGWT LBQEU CIIRU LFVOS EHKC MZNI CUCAPQF
    LWCBED TTSQ EHG LBRGGB GPENC MTKG K OZNCQFYATSBY TQY
    USE CGBCDU BBNE YKT MOQUFYDGN CJ TJO EPMKCF ZF JKSGEA GFTNUDFTN CD JES QEUDEV
    KOO TJO BAPCBFYT KWQWOUSPY OH RJD FKVN NOOZBYY CD USE GXE LNF SU HAU CILPGN CJ
    TJO FXETQFYCG YG XEVYP EIOOT FP DVBNKIYXY PQVJEIEC BCMEKOOY CMUTVKCN LNF
    K OLTKYOLL EYOGETCBEIQX BD BTSFQ APN NLD CC B QEXOS ORGKN LBQEU HHGDIPR VRFCE
    QEHST VY CP A RBFDIFOOE WKXGCEA DIP SGKTZN FSEYT VETE SGON PXVBB WOPQ JE WCC
    FITTK MZNI LFNAWCF EHG YTNATC XPRG WPGEF DP EHG PJCSV GFPKGXE TN OKSNH VY
    BGOKN DZNHVJNTKXH HIVR USE EVPDIPQ DPRGWPYY QP USE YSOEET YMJMRSDD TJKOVS
    RIFZNIMILNI
    YOP BKQ RFEUDJZN UESCOWXETNI DITS AOBCS CMBOEOI BHATNT TS JYX ZR KP USE
    EOSPMQXZ HINV BODTOTD MGDPZ EUZFNICVMJ AHDFC TJO HZLFOO RLQLFD WJSDS BGMBXE
    C DVMINKOE CQWJYGQEU AATDZ QOT DJXEU EQ EHG WPGEOOOE SROBCHGKEPD DI
    QZWGBGFL JYMWYYYPO WQWFY WJY IPLROE CAKCF XINVJZNU YG OONVBCS VY GTGJD TPXWKM
    SATKTDMGXU LRQEOO TJO DZUPDSJ
    SKQOLLKXH EHGSS DURZPCT IYMOEP QMZBGC BETGXEPEU CXLTJOE EHGWTPLXOT TN DVBNK
    UZPCTGN MLPGV QTNU KOO SQEOOEF YGQ ADYVE SGHJDT RYXPR KWCLLCXDPS HBPX TJO SPD
    EKSAEV KOO TJO TEAIO PY TJO BTR G GBD CCVMPD QEU LBQEU AAA SOPQWSUJ AHDFC
    IVC GZROOS LNERPC CCDU DAFVFC QWSU ZNEO TSE NOBCNGN USAV CIP WCC NLKKXH QAT
    VFDS VRBY A OKMP CQRPDT CXE OUTSOR TJO DPRGWPYY PKULLKO QZRVWBY TQYL L BNEOE
    APN TLTKCGJIPQ ETG CD USE CVMXANO SZSVOS ZF PYNTNCDFO DKBFNTQBT SOY MPFLF
    DILT DO UZPROE
    LS KD UFRPC PFT CD MPAUD JY TGBND OH DIP OUMBCS KD QCODKCWY YYOE BG
    GPXEP SOGONFFO IP DJXEU EQ DAKN USAV KMEHQEHS TJO HWODOT DIIXJQIGN USE
    KXJEICDJGEU VBFNER USEA XFGET SOEEPNFO IV DP ME VETE AP KXLRFC TPAUYO
    NAOZBTGP YS ZNG DILT DODLMG KTDOESBEEF YOWY YSUS RGNDLRROU LCVSPYS KXTEECN
    B DPQUFDWQWBY SCSE EHG QSZUR ST HOTUJYG DOITNF MMZSGN EZOTC BYD JKT DIPMF
    LMCCTPD OSMWIQX GZR KDT WEIKM OEHOODE HEOO WJSDS AHDFC TJO HWODOT HAU
    PMZOFOE HIVR USOWCBYDU YG OOPKUTOPC PQ OT VFDS HBPX PGYQWE KX TZMG
    MPFNVBJPS
    PY DLLN DP HECB CWAEU HZWPC XPNV YVE IP KEGAPMF ZF VRF ZSEKSD TJYVRH VRF
    XOXONPNV GJWL CVNZSV MFCTCSOWY DO SPFGBFYCGN CPFQBF LNF NVCIPQ USE EOSPMQXZ
    PSRODTANVZ DIPMF GOEKM XEVYP DURZPCTGBT WIMO BDHNOZ EUFN MLUTK EPRP KOO
    NKMPWE MSEXAP KSP SERFOUNOE ARGCFYTGBT
    LNQDIPR HOBEUTO PQ TJST DECCPY NQ YOP RGKMWY MXPHS YRP TS IYJYG VY XTN DOTE
    PKMUFRG KSRUCLMJ TJST SARZFYS C VPE OH DIP TKWF TNCBHFADVZ EHG XBTLDSUPR
    PKSCAVSWP OPVZ DETFFD TJO BHATNT SYRO NLCJSOP BWD PQTGX USE ROPALG PPCEEKTEIPQ
    USE TKDP SQMBWLGN PDCCBPWOISTES EKO XAMO PYLA OEFCCDFO GWOTDEU
    DIP WCI USE CMBOEOI ULBWVBEEU DIP BKQ XTNPOS OOGCOE HGVQ TN GFFCY QDIPR
    EKUPGQBZ EHG XPXIPOF HIVR USE OYTE VQDFD WKXT MUV SO EHG LFDT RSDEUTO
    DLTGQPCY XYUPRU KSP AUUFO TQ VJDT VRFTR VYQ XOXSFD IP ZSPFGBFYTKKM ZRFOS TF C
    WPGIG QFES OYSP TJKO AETMFYT QP USE HSSDTRVBNE XYUPS KD XTNU GIPN PY
    NZVKO NLNCQFD TJKU EHG YOP WKDI EHG PFHEUD GTRUDQWAEO WZTGC JD ENSNTNCDFO APN
    JES XYUPS CBF CEFSTERKLVEEF DP EHG WPGIGC USAV QBCNGBFO TJO FWIOSOLTGN CLLNYUD
    SGMPYDRVBNE XYUPS CXE EHKC DZNVSOFEU EOEIN K XTNPOS PMGBHPS
    KD JD ANV UPRTSCWY EYOQUUSOR BWD BAPCBFYTNI USE EYODEPCVD FCFPCIVO DZMGC PFT
    CRFLD KX USE GXE EHKC NPAPC USAV OOOOHCFLSQX BHATNT NHCDUPR KXWLRKKCWY
    KXWZLXOT EOTDVCEF CQPCWVBEIQX BMOWD XSIER GTLO GPFLF WPDT NSLPLA LF GOVOSD
    SGMPYD QB USITN GLVQBJEE CXE EHGX FBUCVMJ TQBUFRGN DZNEVVDIQXT LBQEU HHKMI
    QINW NTGJD QCEXKJW
    IP SU HAU K UZSUEQ MEVGFPN DYZSOQN BYD VRF PVGXUFAN GJYNGB CTRFWBY
    IP GJEH NYUD OH OYAETDT MEVDJYG QX USE TOWPNCXU ZR VRF MII CIZRV DIP
    PTSAP WGXU EO UZPELKQIE LCCU JECB OPATVZ LLN DIP FQBFNAUDFCS FODWATOE WA
    NK MLNF DIP PTOTFMRDJGE YSOYET KOO FQB UHO CXE L HCVG XIPEUPS VRFJ WGBF
    NOTBFNT DOGZRG KO PNXOMZPG COLFW GBD RGFFLLGN BYD VRF CIIRUQUN GJYNGB NZOPVJRHV GBD`;
    document.getElementById("keylength").value = "5";
}

function clearForm() {
    document.getElementById("ciphertext").value = "";
    document.getElementById("keylength").value = "";
    document.getElementById("resultContainer").classList.add("hidden");
    document.getElementById("errorContainer").classList.add("hidden");
    document.getElementById("resultPlaintext").innerText = "";
    document.getElementById("resultKey").innerText = "";
    document.getElementById("resultError").innerText = "";
}

function clearPlaintextResult() {
    document.getElementById("resultContainer").classList.add("hidden");
    document.getElementById("resultPlaintext").innerText = "";
    document.getElementById("resultNote").innerText = "";
    document.getElementById("resultKey").innerText = "";
    document.getElementById("resultScore").innerText = "";
}

function clearErrorResult() {
    document.getElementById("errorContainer").classList.add("hidden");
    document.getElementById("resultError").innerText = "";
}