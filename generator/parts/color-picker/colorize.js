function colorizeor_backgroundColor(id1 , id2){
    let element1 = document.getElementById(id1)
    let element2 = document.getElementById(id2) 

    element1.addEventListener("input" , function(event){
        let color = event.target.value ;
        element2.style.backgroundColor = color ;
    })
}


function colorizeor_borderColor(id1 , id2){
    let element1 = document.getElementById(id1)
    let element2 = document.getElementById(id2) 

    element1.addEventListener("input" , function(event){
        let color = event.target.value ;
        element2.style.borderColor = color ;
    })
}


function colorizeor_textColor(id1 , id2){
    let element1 = document.getElementById(id1)
    let element2 = document.getElementById(id2) 

    element1.addEventListener("input" , function(event){
        let color = event.target.value ;
        element2.style.color = color ;
    })
}





colorizeor_backgroundColor("backgroundColor" , "myBox")

colorizeor_borderColor("borderColor" , "myBox")

colorizeor_textColor("textColor" , "myBox")












