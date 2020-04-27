$(document).ready(function(){

    setActiveNavLink();
    
    function setActiveNavLink(){
        $('.navbar-nav li a').click(function(){
            $('.navbar-nav li a').addClass('active')
        });
    }

  });