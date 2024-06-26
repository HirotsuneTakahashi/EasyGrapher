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

    $('#downloadButton').click(function() {
        // 画像のURLを取得
        var imageURL = $('#cus_graph').attr('src');

        // 一時的にダウンロードリンクを作成
        var downloadLink = $('<a>')
            .attr('href', imageURL) // hrefに画像のURLを設定
            .attr('download', 'downloadedImage.png') // ダウンロード時のファイル名を設定
            .css('display', 'none'); // 画面上に表示されないように非表示に設定

        // bodyタグの最後にリンクを追加してクリックイベントを発火
        $('body').append(downloadLink);
        downloadLink[0].click();

        // リンクをドキュメントから削除
        downloadLink.remove();
    });
});