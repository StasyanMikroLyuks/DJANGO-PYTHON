<?php
    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;

    require 'phpmailer/src/PHPMailer.php';
    require 'phpmailer/src/Exception.php';
    

    $mail = new PHPMailer(true);
    $mail->CharSet = 'UTF-8';
    $mail->setLanguage('ru', 'phpmailer/language/');
    $mail->IsHTML(true);
    
    $mail->setFrom($_POST['email']);
    //кому отправка
    $mail->addAddress('test@mikro-lyuks-servis.ru');
    //тема письма
    $mail->Subject = 'Новое письмо с сайта';

    //тело письма
    $body = '<h1>Вам письмо</h1>';

    if(trim(!empty($_POST['name']))){
        $body.='<p><strong>Имя: <strong>'.$_POST['name'].'</p>';
    }

    if(trim(!empty($_POST['number']))){
        $body.='<p><strong>Телефон: <strong>'.$_POST['number'].'</p>';
    }

    if(trim(!empty($_POST['message']))){
        $body.='<p><strong>Сообщение: <strong>'.$_POST['message'].'</p>';
    }

    if(trim(!empty($_POST['age']))){
        $body.='<p><strong>Выберите удобный для вас метод связи: <strong>'.$_POST['age'].'</p>';
    }
    
    error_log($_POST['email'], 0);

    //прикрепить файл
    if (!empty($_FILES['image']['tmp_name'])){
        //путь загрузки файла
        $filePath *"/files/" . $_FILES['image']['name'];
        error_log($_FILES['image']['tmp_name'], 0);
        //грузим файл
        if (copy($_FILES['image']['tmp_name'], $filePath)){
            error_log("зАШЕЛ сюда", 0);
            $fileAttach = "/files/" . $_FILES['image']['name'];
            $body.='<p><strong>Фото в приложении</strong>';
            $mail->addAttachment($fileAttach);
        }
    }

    $mail->Body = $body;

    //отправление
    if (!$mail->send()){
        $message = 'Ошибка';
    } else {
        $message = 'Данные отправлены!';
    }

    $responce = ['message' => $message];

    header('Content-type: application/json');
    echo json_encode($responce)
?>    







