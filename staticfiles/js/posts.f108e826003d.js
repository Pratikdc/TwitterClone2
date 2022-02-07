//
//javascript for post page

$(function() {
    // executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        //$(this) : Self element, namely div.js-menu-icon
        //next() : next to div.js-menu-icon, namely div.menu 
        // toggle() : switch show and hide
        $(this).next().toggle();
    }
    
    )
}

)