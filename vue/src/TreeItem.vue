<script>
import { isProxy, toRaw } from 'vue';


export default {
    name: 'TreeItem',
    // emits: {'model_res':null},
    // emits: {
    //     // No validation
    //     click: null,

    //     // Validate submit event
    //     submit: ({ email, password }) => {
    //         if (email && password) {
    //             return true
    //         } else {
    //             console.warn('Invalid submit event payload!')
    //             return false
    //         }
    //     }
    // },
    // created() {
        // this.$emit('response', 'hello from child')
        // this.$emit('model_res', "this.selected_model()")
        
    // },
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
        selected_model(model){
            this.$emit('model_res', "model")
            // return "this.selected_model()"
            // return model

            // this.$emit('selected_model', model)
            // let d_selected_model = toRaw(model)
            // this.d_selected_model = d_selected_model  
            // console.log(this.d_selected_model)
            // this.d_selected_model = "not null"
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
    <!-- <a class="tree-transition"  @click.prevent :class="{ bold: isFolder , bg_selected:model.selected  }" @click="selected_model(model)" @dblclick="changeType"> -->
    <a class="tree-transition"   @click="$emit('someEvent')"   @click.prevent :class="{ bold: isFolder , bg_selected:model.selected  }"  @dblclick="changeType">
        <span class="tree-text">{{ model.tagName }}</span>
        <div class="tree-append" > 
            <!-- <span v-if="isFolder">[{{ isOpen ? '-' : '+' }}]</span> -->
        </div>
    </a>
    <input type="checkbox" value="model" >
    <ul v-show="isOpen" v-if="isFolder">
        <TreeItem class="item" v-for="model in model.children" :model="model"></TreeItem>
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