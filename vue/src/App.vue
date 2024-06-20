<script>
import Tree  from "./Tree.vue"


export default {
    components: { Tree },
    data(){
        return{
            msg : "ok" ,
        }
    },
    method: {
    }
}
</script>
<template>

    <div class="content_box">
        <Tree></Tree>
    </div>
    

</template>
<style scoped>
.content_box{
    display: flex;
}
</style>