$(document).ready(function(){

    var nextPage = $("#nextPageData").data("next-page");
    
    if(nextPage === "howToUse-home"){
        $("#selecter1").css("display","none");
    }
    else if(nextPage === "termsOfUse-home"){
        $("#selecter2").css("display","none");
    }
    else if(nextPage === "aboutThisSite-home"){
        $("#selecter3").css("display","none");
    }
    else if(nextPage === "faq"){
        $("#selecter4").css("display","none");
    }
});