$(document).ready(function(){
    if(graphType === "bar"){
        $("#graph_type").val("bar");
    }
    else if(graphType === "line"){
        $("#graph_type").val("line");
    }
    else if(graphType === "hist"){
        $("#graph_type").val("hist");
    }
    else if(graphType === "box"){
        $("#graph_type").val("box");
    }
    else if(graphType === "area"){
        $("#graph_type").val("area");
    }
    else if(graphType === "pie"){
        $("#graph_type").val("pie");
    }
    else if(graphType === "scatter"){
        $("#graph_type").val("scatter");
    }
});