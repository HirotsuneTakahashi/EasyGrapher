function updateGraph() {
    var graph_type = document.getElementById('graph_type').value;
    var title = document.getElementById('graph_title').value;
    var xAxis = document.getElementById('x_axis').value;
    var yAxis = document.getElementById('y_axis').value;
    
    // Ajaxリクエストを送信
    fetch('/customizeGraph', {
        method: 'POST', // またはGET、APIの設計に依存
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({x_column: xAxis, y_column: yAxis, graph_type: graph_type, graph_title: title}), // 送信するデータ
    })
    .then(response => response.json())
    .then(data => {
        // グラフの画像を更新
        document.getElementById('cus_graph').src = 'data:image/png;base64,' + data.img_data;
    })
    .catch(error => console.error('Error:', error));
}

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
    
    $('#file').change(function() {
        var fileName = $(this).val().split('\\').pop(); // ファイルパスからファイル名を取得
        $('#fileName').text(fileName); // ファイル名を表示要素に設定
        $("#file-submit label").css("color","gray");
        $("#file-submit label").css("background-color","gray");
        $("#submit-button").css("display","inline-block");
    });

    $("#submit-button").click(function(){
        var dotCount = 0;
        var interval = setInterval(function(){
            $('#fileName').text('loading' + '.'.repeat(dotCount));
                dotCount = (dotCount + 1) % 4; // 点は最大3つまでとし、それ以上になったらリセット
            }, 750);
    })

    $("#file-submit").draggable();
    $("#file-submit").droppable({
        drop: function( event, ui ) {
            $( this )
                .addClass( "ui-state-highlight" )
                .find( "p" )
                . html( "ドロップされました！" );
        }
    });

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