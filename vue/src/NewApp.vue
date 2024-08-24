<script>
import TreeNode from './TreeNode.vue';

let treeData = {
                tagName: "html",
                children: [
                    {
                        tagName: "head",

                        children: [
                            {
                                tagName: "title",
                                content: "Page Title"
                            }
                        ]
                    },
                    {
                        tagName: "body",
                        children: [
                            {
                                tagName: "div",
                                children: [
                                    {
                                        tagName: "h1",
                                        content: "Welcome to My Website"
                                    },
                                    {
                                        tagName: "p",
                                        content: "This is a paragraph."
                                    },
                                    {
                                        tagName: "div",
                                        children: [
                                            {
                                                tagName: "ul",
                                                children: [
                                                    {
                                                        tagName: "li",
                                                        content: "Item 1"
                                                    },
                                                    {
                                                        tagName: "li",
                                                        content: "Item 2"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }

export default {
    name: 'NewApp',
    components: { TreeNode },
    data() {
        return {
            treeData ,
            selectedNode: null,
            editTag: '',
            editContent: '',
            newTag: '',
            newContent: '' ,
            showNodeContent: false ,
            msgHideShowContent: "Show" , 
            showCss : true ,

        };
    },
    methods: {
        selectNode(node) {
            this.selectedNode = node;
            this.editTag = node.tagName;
            this.editContent = node.content || '';
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
                    tagName: this.newTag,
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
        },
        addChild(){
			console.log(this.newTag)
            if (this.selectedNode) {
                if (!this.selectedNode.children) {
                    this.selectedNode.children = [];
                }
                this.selectedNode.children.push({
                    tagName: 'div',
                });
            }
		},
        
    },
    created:function(){
		window.addEventListener("keyup",(e)=>{
			if (e.keyCode==65 && this.selectedNode) {
					this.addChild()
				}
		})
	},
	destroyed:function(){
		window.removeEventListener("keyup")
	}
};
</script>
<template>
    <div class="content_box">
        <div id="treeBox" >
            <div id="treeDOM">
                <TreeNode :show-node-content="showNodeContent" :node="treeData" :selected-node="selectedNode" @select-node="selectNode"/>
            </div>
        </div>
        <div id="settings">
            <div id="go-to-settings">
                <div :class="[{b_b_2:this.showCss}]" @click="()=>{this.showCss = !this.showCss}" id="go-to-css-settings">showCssSettings</div>
                <div :class="[{b_b_2:!this.showCss}]" @click="()=>{this.showCss = !this.showCss}" id="go-to-html-settings">showHtmlSettings</div>
            </div>
            <div v-show="this.showCss" id="css">
                <h1>CSS Settings</h1>
                <p style="text-align: center; background-color: chocolate; color: white;">
                    برای اضافه کردن یک بچه به درخت
                    <br>
                    پس ار انتخاب کردن ان
                    <br>
                    <span style="color: black;">CTRL + A</span>
                    <br>
                    را فشار دهید
                </p>
            </div>
            <div v-show="!this.showCss" id="html" >
                <button @click="()=>{this.showNodeContent = !this.showNodeContent;}">{{ showNodeContent ? "Hide Content" : "Show Content" }}</button>
                <!-- نمایش جزئیات و عملیات CRUD -->
                <div v-if="selectedNode" class="node-details">
                    <h2>Selected Node</h2>
                    <p><strong>Tag:</strong> {{ selectedNode.tagName }}</p>
                    <p><strong>Content:</strong> {{ selectedNode.content || 'No content' }}</p>

                    <!-- عملیات بروزرسانی -->
                    <h3>Update Node</h3>
                    <input v-model="editTag" placeholder="Update Tag" />
                    <input v-model="editContent" placeholder="Update Content" />
                    <button @click="updateNode">Update</button>

                    <!-- عملیات ایجاد -->
                    <h3>Add Child Node</h3>
                    <input v-model="newTag" placeholder="New Child Tag" />
                    <input v-model="newContent" placeholder="New Child Content" />
                    <button @click="addChildNode">Add Child</button>

                    <!-- عملیات حذف -->
                    <h3>Delete Node</h3>
                    <button @click="deleteNode">Delete Node</button>
                </div>
            </div>
        </div>
        <div id="demo_section">
            demo
        </div>
    </div>
</template>
<style>

</style>
