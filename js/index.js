function equalHeights( $objs ) {
    var highest = 0;

    $objs.each(function() {
        thisHeight = $(this).height();
        if(thisHeight > highest ) {
            highest = thisHeight;
        }
    });

    $objs.height( highest );
}

$('#new-icon').hover(function() {
    $('#mac-icon').css('visibility', 'visible');
}, function() {
    $('#mac-icon').css('visibility', 'hidden');
});

equalHeights( $('.footerBox') );