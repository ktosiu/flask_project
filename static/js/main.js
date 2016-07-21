
function hide_messages(duration, pause_duration){
    var flash_messages = $('#flash-messages > .flash-message')
    flash_messages.click(function(){
    $(this).hide();
    })


    var flash_message = flash_messages.first();
    function hide_message(flash_message, d){
        flash_message.slideUp(1000, function(){
            flash_message = flash_message.next();
            if (flash_message.length != 0) {
                setTimeout(function() {hide_message(flash_message, duration)}, pause_duration)
            }

        })


    }

    setTimeout(function() {hide_message(flash_message, duration)}, pause_duration)
}


$(function(){
    hide_messages(1500, 500);





})