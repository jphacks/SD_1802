<?php

    //一次ファイルができているか
    if(is_uploaded_file($_FILES['up_file']['tmp_name'])){

        //一次ファイルをコピーして保存
        if(move_uploaded_file($_FILES['up_file']['tmp_name'],"./upload/".$_FILES['up_file']['name'])){
            //正常
            echo "uploaded";

        }else{
            //コピーに失敗
            echo "error while saving.";
        }
    }else{
        //そもそもファイルが来ていない。
        echo "file not uploaded.";

    }
?>