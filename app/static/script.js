$(document).ready(function(){

    var nextPage = $("#nextPageData").data("next-page");
    
    if(nextPage === "howToUse-home"){
        $("#selecter1").removeAttr('href');
        $("#selecter1").css({
            'color': 'gray',
            'textDecoration': 'none'
        })
    }
    else if(nextPage === "termsOfUse-home"){
        $("#selecter2").removeAttr('href');
        $("#selecter2").css({
            'color': 'gray',
            'textDecoration': 'none'
        })
    }
    else if(nextPage === "aboutThisSite-home"){
        $("#selecter3").removeAttr('href');
        $("#selecter3").css({
            'color': 'gray',
            'textDecoration': 'none'
        })
    }
    else if(nextPage === "faq"){
        $("#selecter4").removeAttr('href');
        $("#selecter4").css({
            'color': 'gray',
            'textDecoration': 'none'
        })
    }
    else if(nextPage === "upload1"){
        
    }
});