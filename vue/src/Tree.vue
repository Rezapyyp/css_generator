<script>
import { isProxy, toRaw } from 'vue';
import TreeItem from './TreeItem.vue'


const treeData = {
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
                selected_model : "no model" ,

            }
        },
    methods :{
    }
}



</script>


<template>
    <div id="treeBox" >
        <div id="treeDOM" >
            <ul>
                <TreeItem class="item" @model_res="(model) => selected_model = model" :model="treeData"></TreeItem>
                <!-- <TreeItem class="item" @model_res="model" :model="treeData"></TreeItem> -->
            </ul>
        </div>
    </div>
	<div class="settings">
        selected_tag : {{ selected_model }}
    </div>
	
</template>

<style>
    .settings{
        width: 30vw;
        background-color: rgb(53, 230, 191);
    }
</style>