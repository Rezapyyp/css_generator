<script>
// import axios from "axios"
import Folder from "./Folder.vue"

export default {
    components: { Folder, },
    data(){
        return{
            showFormCreateFolder : false ,
            showFile: false ,
        }
    },
    methods: {
        // showForm(){
        //     this.showFormCreateFolder = ! this.showFormCreateFolder 
        // },
        // async send_data(){
        //     const data = {name: this.$refs.inputValue.value,}
        //     console.log(data);
        //     await axios.post('http://127.0.0.1:8000/createFolder', data , {headers: {'content-type':'application/json' }})
        //     .then(function (response) {
        //         console.log(response);
        //         console.log(response.status);
        //         alert(response.data.f_msg)
        //     })
        //     .catch(function (error) {
        //         console.log(error.message);
        //     });
        //     this.showFormCreateFolder = false
        // },
    }
}
</script>
<template>

<div id="explorerFolderBody">

</div>



</template>
<style scoped>
#explorerFolderBody{
    width: 20vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    /* background-color: rgb(21, 27, 27); */
    background-color: rgb(192, 235, 235);
    overflow: hidden;
}
#createNewFolder{
    color: white;
    background-color: blueviolet;
    font-size: 1.5rem;
    padding: 10px;
    margin: 20px;
    cursor: pointer;
}
#CRUDexplorer{
    width: 100vw;
    height: 5rem;
    margin-bottom: 1px ;
    background-color: black;
    display: flex;
    flex-direction: row-reverse;
    align-items: center;
}

#folders{
    display: flex;
    flex-direction: column;
    margin-bottom: 100px;
    background-color: rgb(245, 175, 175);
    font-size: 20px;
    /* overflow: scroll; */
}

#myForm{
    background-color: rgb(109, 30, 30);
    color: white;
    height: 3rem;
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
}

#myForm input {
    /* width: 20rem;
    height: 2rem; */
    width: 100%;
    height: 100%;
    background-color: rgb(99, 99, 99);
    text-align: center;
    font-size: 20px;
    outline: none;
    border: none;
}


.folder{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100vw;
    height: 3rem;
    background-color: rgb(99, 99, 99);
    margin: 1px;
    font-size: 20px;
    /* overflow: scroll; */
}

.folder-head{
    width: 100vw;
    height: 3rem;
}
.folder-head span{
    display: block;
    margin-top: 0.7rem;
}

.files{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background-color: rgb(148, 206, 206);
    /* height: 3rem;
    width: 100vw; */
}

</style>