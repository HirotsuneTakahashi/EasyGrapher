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

    $('button[name="action"]').click(function() {
        var graphType = $(this).val(); // クリックされたボタンのvalueを取得

        // クリックされたグラフタイプに応じたデータを準備
        var data = {
            'graph_type': graphType,
        };

        // Ajaxリクエストを送信
        $.ajax({
            url: '/selectImage',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                $('#graph-preview').attr('src', 'data:image/png;base64,' + response.image);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});