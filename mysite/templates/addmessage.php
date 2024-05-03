<?php

$connected = new PDO("mysql:host=localhost;dbname=l103521_reviews", "l103521_stas", "40IPkj0w$h0si0cF");


//mysqli_connect(<адрес сервера>, <имя пользователя>, <пароль>, <имя базы данны>
if (!$connected) {
    die('Ошибка: невозможно подключится:' . mysqli_error());
}
echo 'Подключились к базе.<br>';



// try{
//     // $connected = new PDO($dsn, $user, $password);
    
//     if(empty($_POST['name'])) exit("Поле имя не заполнено");

//     if(empty($_POST['content'])) exit("Поле сообщение не заполнено");

//     $query = "INSERT INTO message VALUES (NULL , :name, NOW())";
//     $msg = $connected->prepare($query);
//     $msg->execute( ['name' => $_POST['name']]);

//     $msg_id = $connected->LastInserId();
    
//     $query = "INSERT INTO message content VALUES (NULL, :content, NOW())";
//     $msg = $connected->prepare($query);
//     $msg->execute(['content'=> $_POST['content']]);

//     header("Location: index.html");
// }

// catch (PD0Exception $e)
// {
//     echo "error";
// }
?>