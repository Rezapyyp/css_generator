<script>
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
                treeData
            }
        },
    methods :{
    }
}



</script>


<template>
	
    <div id="treeBox" >
        <div id="treeSettings">

        </div>
        <div id="treeDOM" >
            <ul>
                <TreeItem class="item" :model="treeData"></TreeItem>
            </ul>
        </div>
    </div>
	
</template>

<style>

</style>