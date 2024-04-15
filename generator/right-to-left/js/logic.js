let toolbar = document.getElementById("toolbar")
let toolbarBody = document.getElementById("toolbarBody")
let triangle = document.getElementById("triangle")





triangle.addEventListener("click",function(){

    
    if( triangle.classList.contains("t-down") ){
        triangle.classList.remove("t-down")
        triangle.classList.add("t-up")
        toolbar.classList.add("b-0")
        toolbarBody.classList.remove("d-none")
    }
    else if( triangle.classList.contains("t-up") ){
        triangle.classList.add("t-down")
        triangle.classList.remove("t-up")
        toolbar.classList.remove("b-0")
        toolbarBody.classList.add("d-none")
    }

})
