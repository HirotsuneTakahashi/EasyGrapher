$(document).ready(function(){
    $('#file').change(function() {
        var fileName = $(this).val().split('\\').pop(); // ファイルパスからファイル名を取得
        $('#fileName').text(fileName); // ファイル名を表示要素に設定
        $("#file-submit label").css("color","gray");
        $("#file-submit label").css("background-color","gray");
        $("#submit-button").css("display","inline-block");
    });

    $("#submit-button").click(function(){
        var dotCount = 0;
        var loadingText = $(this).data('data-loading-text');
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
});