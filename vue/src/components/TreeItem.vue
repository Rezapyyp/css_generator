<script>


export default {
    name: 'TreeItem',
    props: {
        node: {
            type: Object,
            required: true
        },
        selectedNode: {
            type: Object,
            required: true
        }
    },
    computed: {
        isFolder() {
            return this.node.children && this.node.children.length
        },
        isSelected() {
            return this.node === this.selectedNode;
        },
    },

    data() {
        return {
            isOpen: true,
        }
    },
    methods: {
        selectNode() {
        this.$emit('select-node', this.node);
        },
        handleSelectNode(node) {
            console.log(node)
            this.$emit('', node);
        },
        changeType() {
            if ( !this.isFolder & this.node.block_element ) {
                this.node.children = []
                this.isOpen = true
                this.addChild()
            }
            else if( !this.node.block_element ){
                alert("This tag is void_element")
            }
        },
        addChild() {
            // alert("add child")
            this.node.children.push({tagName:"child" , block_element:true })
        }

    },

}
</script>
<template>
  <li>
    <a class="tree-transition"  :class="{ bold: isFolder  }"  @dblclick="changeType">
        <span class="tree-text">{{ node.tagName }}</span>
        <div class="tree-append" > 
        </div>
    </a>
    <ul v-show="isOpen" v-if="isFolder">
        <!-- <TreeItem class="item"
         v-for="(child , index) in node.children" 
         :key = "`${index} ${node.tagName}`"
         :node="node"
         
         @click="(node)=> $emit('selectednode' , node ) "
         
         /> -->
         <TreeItem class="item"
                  v-for="(child, index) in node.children" 
                  :key="index" 
                  :node="child" 
                  :selected-node="selectedNode"
                  @select-node="handleSelectNode"
                  @click="(node)=> $emit('selectNode' , child ) "
                  />
        
        <li class="add" @click="addChild" style="color:red;">+</li>
    </ul>
</li>
</template> 
<style>
.bg_selected{
    color: white !important;
    background-color:blueviolet;
}
</style>