$(document).ready(function () {
    var alltypebtn = document.getElementById("alltypebtn")
    var showsortbrn = document.getElementById("showsortbtn")

    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

    typediv.style.display = "none"
    sortdiv.style.display = "none"

    alltypebtn.addEventListener("click", function () {
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)
    showsortbrn.addEventListener("click", function () {
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)
    typediv.addEventListener("click", function () {
        typediv.style.display = "none"
    },false)
    sortdiv.addEventListener("click", function () {
        sortdiv.style.display = "none"
    },false)

    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")
    for (var i = 0; i < addShoppings.length; i++){
        addShopping = addShoppings[i]
        addShopping.addEventListener("click", function () {
            pid = this.getAttribute("ga")
            $.post("/changecart/0",{"productid":pid},function (data) {
                if (data.status == "success"){

                }
            })
        })
    }
    for (var i = 0; i < subShoppings.length; i++){
        subShopping = addShoppings[i]
        subShopping.addEventListener("click", function () {
            pid = this.getAttribute("ga")
            $.post("/changecart/1",{"productid":pid},function (data) {
                if (data.status == "success"){
                    document.getElementById(pid).innerHTML = data.data
                }else{
                    if (data.data == -1){
                        //
                    }
                }
            })
        })
    }


})