<script>
export default {
    name: 'TreeNode',
    props: {
        node: {
            type: Object,
            required: true
        },
        selectedNode: {
            type: Object,
        },
        showNodeContent: {
            type: Boolean,
            required: true
        }
    },
	data(){
		return{
			counter:0,
		}
	},
    computed: {
        isSelected() {
            return this.node === this.selectedNode;
        }
    },
    methods: {
        selectNode() {
			this.$emit('select-node', this.node);
        },
        handleSelectNode(node) {
			this.$emit('select-node', node);
        },
		
    },
}
</script>
<template>
    <div :class="['tree-node', { selected: isSelected }]" @click.stop="selectNode">
      <!-- نمایش نام تگ -->
      <div class="tag-name">
        {{ node.tagName }}
      </div>
  
      <!-- نمایش محتوای تگ (در صورت وجود) -->
      <div v-if="node.content &&  showNodeContent" class="tag-content">
        {{ node.content }}
      </div>
  
      <!-- نمایش فرزندان به صورت بازگشتی (در صورت وجود) -->
      <div v-if="node.children" class="children">
        <TreeNode v-for="(child, index) in node.children" 
                  :key="index" 
                  :node="child" 
                  :show-node-content="showNodeContent" 
                  :selected-node="selectedNode"
                  @select-node="handleSelectNode"
                  @send-signal="()=>{this.$emit('toggle-content', showNodeContent)}"
                  />
      </div>
    </div>
</template>  
<style scoped>
.tree-node {
  margin-left: 20px;
  padding: 5px;
  border-left: 2px solid #ccc;
  cursor: pointer;
}

.selected {
  background-color: #4f83bb;
  /* background-color: #cce5ff; */
  min-width: 6rem;
}

.tag-name {
  font-weight: bold;
}

.tag-content {
  color: #555;
  margin-left: 10px;
}
.children {
  margin-left: 20px;
}
</style>










