(function () {
    var Message;

    Message = function ({
                            text: text1,
                            message_side: message_side1,
                            name: name1
                        }) {
        this.text = text1;
        this.name = name1;
        this.message_side = message_side1;
        this.draw = () => {
            var $message;
            $message = $($('.message_template').clone().html());
            $message.addClass(this.message_side).find('.text').html(this.text);
            $message.addClass(this.message_side).find('.name').html(this.name);

            $message.find('.name').html(this.name);
            $('.messages').append($message);
            return setTimeout(function () {
                return $message.addClass('appeared');
            }, 0);
        };
        return this;
    };

    $(function () {
        var getMessageText, message_side, sendMessage;
        message_side = 'right';
        getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };
        sendMessage = function (text, side, name) {
            var $messages, message;
            if (text.trim() === '') {
                return;
            }
            $('.message_input').val('');
            $messages = $('.messages');
            message_side = side;
            message = new Message({text, message_side, name});
            message.draw();
            return $messages.animate({
                scrollTop: $messages.prop('scrollHeight')
            }, 300);
        };
        $('.send_message').click(function (e) {
            var text = getMessageText();
            sendUserResponse(text);
        });
        $('.message_input').keyup(function (e) {
            if (e.which === 13) {
                var text = getMessageText();
                sendUserResponse(text);
            }
        });
        sendAIResponse("1. В каком городе вы хотите учиться?<br>" +
            "2. Какие предметы вам больше всего нравились в школе или университете?<br>" +
            "3. В каком классе обучаетесь?<br>" +
            "4. Как вы оцениваете свои коммуникативные, организационные и технические навыки?<br>" +
            "5. Вам больше нравится работать в команде или индивидуально?<br>" +
            "6. Какую роль играет заработная плата в выборе профессии?<br>" +
            "7. Какие профессии вам представляются интересными и привлекательными?<br>" +
            "8. Как бы вы описали свою идеальную рабочую среду?<br>" +
            "9. Вы предпочитаете работать по строгому графику или иметь некоторую свободу в определении своего рабочего времени?<br>" +
            "10. Что вы знаете о различных отраслях и профессиях, и какие из них вас привлекают?")

        function sendAIResponse(text) {


            setTimeout(() => {
                sendMessage(text, "left", "AI");
            }, 500);
        }

        function sendUserResponse(text) {
            sendMessage(text, "right", "AI");

            fetch(`http://127.0.0.1:5000/fast_get_text?text=${encodeURIComponent(text)}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data.text)

                    sendMessage(data.text, "left", "AI");
                })
                .catch(error => {
                    console.error("Error making the GET request:", error);
                });
        }


    });

}).call(this);