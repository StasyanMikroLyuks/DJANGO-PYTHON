"use strict"
$(document).ready(() => {
    $("#mainBtn").click(() => {
        let error = formValidate($('#mainForm').get(0));

        var formData = new FormData();
        //var formImage = $('#formImage')[0].files;
        //formData.append('image', formImage[0]);
        //var qwe = formImage[0];
        debugger;
        formData.append('name', $('#mainForm').get(0)[0].value);
        formData.append('number', $('#mainForm').get(0)[1].value);
        formData.append('email', $('#mainForm').get(0)[2].value);
        formData.append('message', $('#mainForm').get(0)[3].value);
        formData.append('age', $('#mainForm').get(0)[4].value);
        
        
        var qwe = formData;
        debugger;

        if(error===0){
            // form.classList.add('_sending'); //класс для уведомления о том что форма придёт спустя время
            //технология аякс с помощью fetch
            $.ajax({
                url: 'sendmail.php',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: (response) => {
                    debugger
                    alert(response.message)                    
                }
            });
        }
        else{
            alert('Заполните обязательные поля');
        }
    });

    function formValidate(form){
        let error = 0; //переменная error которая равна 0
        let formReq = document.querySelectorAll('._req');
        //обязательное поле 
        //цикл
        for (let index = 0; index < formReq.length; index++){
            const input = formReq[index];
            formRemoveError(input) //изначально убираем класс error

            if (input.classList.contains('_email')){
                if (emailTest(input)){
                    //если проверка email не пройдена то выскакивает функция error
                    formAddError(input);
                    error++;
                }
                //проверка на тип что это чекбокс а так же если этот чекбокс не включен
            }else if(input.getAttribute("type") === "checkbox" && input.checked === false){
                formAddError(input);
                error++;
            }else{
                //проверка заполнено ли поле вообще, если пустая строка то ошибка
                if (input.value === ''){
                    formAddError(input);
                    error++;
                }
            }
        }
        return error; //либо 0 либо 1
    }

    //добавляет объекту и родительскому класс error
    function formAddError(input){
        input.parentElement.classList.add('_error');
        input.classList.add('_error');
    }

    //убирает у объекта и родительскому класс error
    function formRemoveError(input){
        input.parentElement.classList.remove('_error');
        input.classList.remove('_error');
    }

    //проверка строки email на символы
    function emailTest(input){
        return !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,8})+$/.test(input.value);
    }

    //для того чтобы видеть превью фото
    //перевод id formImage в переменную
    //const formImage = document.getElementById('formImage');
    //перевод formPrewiew в переменную для дальнейшего показа фотографии
    //const formPrewiew = document.getElementById('formPrewiew');

    //для объекта выбора файла добавляется событие change, то есть 
    //при выборе какого-то файла срабатывает данное событие и перенаправится на функцию UploadFile и передавать туда файл который выбран
    //formImage.addEventListener('change', () => {
        //uploadFile(formImage.files[0]);
    //});

    //function uploadFile(file){
        //проверка типа файла
        //if (!['image/jpeg', 'image/png', 'image/gif'].includes(file.type)){
           // alert('Разрешены только изображения.');
           // formImage.value= '';
           // return;
        //}

        //проверка размера файла чтоб был не меньше 2 мб
        //if (file.size > 2 * 1024 * 1024){
            //alert('Файл должен быть не менее 2 мб.');
            //return;            
        //}

        //вывод файла пользователю в качестве превью
        //когда файл успешно загружен идёт отправка изображения и помещается внутрь div formPrewiew 
        //var reader = new FileReader();
        //reader.onload = function (e) {
       // formPrewiew.innerHTML = `<img src="${e.target.result}" alts="Фото">`;
        //};  
        //reader.onerror = function (e) {
        //alert('Ошибка');
        //};     
        //reader.readAsDataURL(file);                 
    //}
});

document.addEventListener('DOMContentLoaded', function () {
    
});
