<script>
export default {
    name: 'TreeItem', // necessary for self-reference
    props: {
        model: Object
    },
    data() {
        return {
        isOpen: true
        }
    },
    computed: {
        isFolder() {
            return this.model.children && this.model.children.length
        },
    },
    methods: {
        toggle() {
            if (this.isFolder) {
                this.isOpen = !this.isOpen
            }
        },
        changeType() {
            if ( !this.isFolder & this.model.block_element  ) {
                this.model.children = []
                this.isOpen = true
                this.addChild()
            }
            else if( !this.model.block_element ){
                alert("This tag is void_element")
            }
        },
        addChild() {
            // alert("add child")
            this.model.children.push({tagName:"child" , block_element:true })
        }

    },

}
</script>
<template>
  <li>
    <a class="tree-transition"  @click.prevent :class="{ bold: isFolder }" @click="toggle" @dblclick="changeType">
        <span class="tree-text">{{ model.tagName }}</span>
        <div class="tree-append" > 
            <span v-if="isFolder">[{{ isOpen ? '-' : '+' }}]</span>
        </div>
     </a>
    <ul v-show="isOpen" v-if="isFolder">
        <TreeItem class="item" v-for="model in model.children" :model="model"></TreeItem>
        <li class="add" @click="addChild" style="color:red;">+</li>
    </ul>
  </li>
</template> 