<script>
import Tree  from "./Tree.vue"
import FolderExplorer from "./generator/folders/FolderExplorer.vue"

export default {
    components: { Tree, FolderExplorer },
    data(){
        return{
            msg : "ok" ,
        }
    },
    method: {
        mmyM(){
            console.log();
        }
    }
}
</script>
<template>

    <FolderExplorer></FolderExplorer>
    

</template>
<style scoped>
.my-box{
    background-color: rgb(207, 195, 22);
    width: 15rem;
    height: 20rem;
    margin: 3rem auto;
    color: black;
    font-size: 100px;
    text-align: center;
}
</style>