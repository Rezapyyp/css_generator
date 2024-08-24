<script>
// import { isProxy, toRaw } from 'vue';
import TreeItem from './TreeItem.vue'


let treeData = {
    tagName: 'html',
    block_element: true ,
    children: [
        {
            tagName: 'head',
            block_element: true ,
            children: [  
                    { tagName:'meta' , block_element: false },
                    { tagName:'link' , block_element: false },
                    { tagName:'title' , block_element:true },
                ]
        },
        { 
            tagName: 'body',
            block_element: true ,
            children: [ 
                { tagName : 'header', block_element:true },
                { tagName : 'main', block_element:true },
                { tagName : 'footer', block_element:true }  ]
        },
    ]
}


export default {
    components: {
        TreeItem
    },
    data(){
            return {
                treeData,
                count : 0 ,
            }
        },
    methods :{
        getSelectedModel(model){
            console.log(model)
        },
        callback(model){
            // obj_model = toRaw(model) 
            // console.log(obj_model)
            // console.log(toRaw(model))
            console.log(model)
            console.log("Fucked")
        }
    }
}



</script>


<template>
    <div id="treeBox" >
        <div id="treeDOM" >
            <ul>
                <TreeItem class="item" @selectedModel="callback" :model="treeData"></TreeItem>
            </ul>
        </div>
    </div>
	<div class="settings">
        selected_tag : {{count}}
    </div>
	
</template>

<style>
    .settings{
        width: 30vw;
        background-color: rgb(53, 230, 191);
    }
</style>