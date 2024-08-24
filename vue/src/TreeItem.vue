<script>
import { isProxy, toRaw } from 'vue';


export default {
    name: 'TreeItem',

    props: {
        model: Object
    },
    data() {
        return {
            isOpen: true,
        }
    },
    computed: {
        isFolder() {
            return this.model.children && this.model.children.length
        },  
    },
    methods: {
        sendModel(){
            // this.$emit('selectedModel', this.model)
            
            // console.log("clicked")
            // console.log(model)

            // let sd = toRaw(model)
            // this.$emit('selectedModel', sd)


            // console.log(sd)
            // this.$emit('selectedModel', sd)
            
            // console.log("clicked")


        },
        changeType() {
            if ( !this.isFolder & this.model.block_element ) {
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
    <a class="tree-transition"  :class="{ bold: isFolder  }"  @dblclick="changeType">
        <span class="tree-text">{{ model.tagName }}</span>
        <div class="tree-append" > 
        </div>
    </a>
    <ul v-show="isOpen" v-if="isFolder">
        <TreeItem class="item"
         v-for="(model , index) in model.children" 
         :key = "`${index} ${model.tagName}`"
         :model="model"
         
         @click="(node)=> $emit('selectedModel' , model ) "
         
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