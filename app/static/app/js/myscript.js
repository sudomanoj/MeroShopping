$('#slider1').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    autoplayTimeout: 2000,
    responsive: {
      0: {
        items: 2,
        nav: false,
        autoplay: true,
      },
      600: {
        items: 3,
        nav: true,
        autoplay: true,
      },
      1000: {
        items: 5,
        nav: true,
        loop: true,
        autoplay: true,
      }
    }
});

$('#slider2').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    autoplayTimeout: 2500,
    responsive: {
      0: {
        items: 2,
        nav: false,
        autoplay: true,
      },
      600: {
        items: 3,
        nav: true,
        autoplay: true,
      },
      1000: {
        items: 5,
        nav: true,
        loop: true,
        autoplay: true,
      }
    }
});

$('#slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    autoplayTimeout: 3000,
    responsive: {
      0: {
        items: 2,
        nav: false,
        autoplay: true,
      },
      600: {
        items: 3,
        nav: true,
        autoplay: true,
      },
      1000: {
        items: 5,
        nav: true,
        loop: true,
        autoplay: true,
      }
    }
});

$('#slider4').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    autoplayTimeout: 3500,
    responsive: {
      0: {
        items: 2,
        nav: false,
        autoplay: true,
      },
      600: {
        items: 3,
        nav: true,
        autoplay: true,
      },
      1000: {
        items: 5,
        nav: true,
        loop: true,
        autoplay: true,
      }
    }
  });

$('.plus-cart').click(function(){
    var id = $(this).attr('pid').toString();
    var ele = this.parentNode.children[2]

    $.ajax({
        type:'GET',
        url:'/pluscart',
        data:{
            product_id:id
        },
        success: function (data) {
            ele.innerText = data.quantity
            document.getElementById('shipping').innerText = data.shipping_fee
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            console.log(data.shipping_fee)
        }
    })
})

$('.minus-cart').click(function(){
    var id = $(this).attr('pid').toString();
    var ele = this.parentNode.children[2];
    var quantity = parseInt(ele.innerText); // Get the current quantity

    // Check if quantity is greater than one
    if (quantity > 1) {
        $.ajax({
            type:'GET',
            url:'/minuscart',
            data:{
                product_id:id
            },
            success: function (data) {
                ele.innerText = data.quantity
                document.getElementById('shipping').innerText = data.shipping_fee
                document.getElementById('amount').innerText = data.amount
                document.getElementById('totalamount').innerText = data.totalamount
            }
        });
    }
});



$('.remove-cart').click(function(){
    var id = $(this).attr('pid').toString();
    var ele = this

    $.ajax({
        type:'GET',
        url:'/removecart',
        data:{
            product_id:id
        },
        success: function (data) {
            document.getElementById('amount').innerText = data.amount
            document.getElementById('shipping').innerText = data.shipping_fee
            document.getElementById('totalamount').innerText = data.totalamount
            ele.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})


// Get the footer element
const footer = document.getElementById("footer");

// Function to check if the user has scrolled to the end
function checkFooterVisibility() {
  // Calculate the scroll position
  const scrollPosition = window.innerHeight + window.pageYOffset;
  // Calculate the total height of the document
  const documentHeight = document.documentElement.offsetHeight;

  // Show or hide the footer based on scroll position
  if (scrollPosition >= documentHeight) {
    footer.style.display = "block";
  } else {
    footer.style.display = "none";
  }
}

// Event listener for scroll event
window.addEventListener("scroll", checkFooterVisibility);

// Initial check when the page loads
checkFooterVisibility();