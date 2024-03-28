$(document).ready(function(){

    var nextPage = $("#nextPageData").data("next-page");
    
    var homeText = $("#textHome").text();
    if(nextPage === "howToUse-home"){
        $("#selecter1").attr("href", "/").text(homeText);
    }
    else if(nextPage === "termsOfUse-home"){
        $("#selecter2").attr("href", "/").text(homeText);
    }
    else if(nextPage === "aboutThisSite-home"){
        $("#selecter3").attr("href", "/").text(homeText);
    }
});