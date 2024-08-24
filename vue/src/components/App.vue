<script>
import TreeItem from './TreeItem.vue'

let treeData = {
    tagName: 'html',
    content : null , 
    block_element: true , 
    children: [
        {
            tagName: 'head',
            content: "Page Title" ,
            block_element: true ,
            children: [  
                    { tagName:'meta' , block_element: false , content: "Page Title" },
                    { tagName:'link' , block_element: false , content: "Page Title" },
                    { tagName:'title' , block_element:true , content: "Page Title" },
                ]
        },
        { 
            tagName: 'body',
            block_element: true ,
            children: [ 
                { tagName : 'header', block_element:true  , content: "Page Title" },
                { tagName : 'main', block_element:true , content: "Page Title"  },
                { tagName : 'footer', block_element:true , content: "Page Title"  }  ]
        },
    ]
}

export default {
    components: { TreeItem },
    data(){
        return{
            treeData,
            selectedNode: null,
            editTag: '',
            editContent: '',
            newTag: '',
            newContent: ''
        }
    },
    method: {
        selectNodeFunc(node) {
            console.log(node)
            // this.selectedNode = node;
            // this.editTag = node.tagName;
            // this.editContent = node.content || '';
        },
        updateNode() {
            if (this.selectedNode) {
                this.selectedNode.tagName = this.editTag;
                this.selectedNode.content = this.editContent;
            }
        },
        addChildNode() {
            if (this.selectedNode) {
                if (!this.selectedNode.children) {
                    this.selectedNode.children = [];
                }
                this.selectedNode.children.push({
                    tag: this.newTag,
                    content: this.newContent
                });
                this.newTag = '';
                this.newContent = '';
            }
        },
        deleteNode() {
            const deleteRecursive = (node, parent, index) => {
                if (node === this.selectedNode) {
                    parent.children.splice(index, 1);
                    this.selectedNode = null;
                } else if (node.children) {
                    node.children.forEach((child, i) => deleteRecursive(child, node, i));
                }
            };
            deleteRecursive(this.treeData, null, null);
        }
    }
}
</script>
<template>

    <div class="content_box">
        <div id="treeBox" >
            <div id="treeDOM" >
                <ul>
                    <TreeItem :node="treeData" :selected-node="selectedNode" @selectNode="selectNodeFunc"  />
                    <!-- <TreeItem class="item" @selectedModel="callback" :model="treeData"></TreeItem> -->

                </ul>
            </div>
        </div>
        <div class="settings">
            selected_tag : {{ selectedNode }}
        </div>
    </div>
    

</template>
<style scoped>
.content_box{
    display: flex;
}
.settings{
        width: 30vw;
        background-color: rgb(53, 230, 191);
}
</style>