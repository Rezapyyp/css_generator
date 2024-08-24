<script>
import TreeNode from './TreeNode.vue';

let treeData = {
                tag: "html",
                children: [
                    {
                        tag: "head",

                        children: [
                            {
                                tag: "title",
                                content: "Page Title"
                            }
                        ]
                    },
                    {
                        tag: "body",
                        children: [
                            {
                                tag: "div",
                                children: [
                                    {
                                        tag: "h1",
                                        content: "Welcome to My Website"
                                    },
                                    {
                                        tag: "p",
                                        content: "This is a paragraph."
                                    },
                                    {
                                        tag: "div",
                                        children: [
                                            {
                                                tag: "ul",
                                                children: [
                                                    {
                                                        tag: "li",
                                                        content: "Item 1"
                                                    },
                                                    {
                                                        tag: "li",
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
    components: {
        TreeNode
    },
    data() {
        return {
            treeData ,
            selectedNode: null,
            editTag: '',
            editContent: '',
            newTag: '',
            newContent: ''
        };
    },
    methods: {
        selectNode(node) {
            this.selectedNode = node;
            this.editTag = node.tag;
            this.editContent = node.content || '';
        },
        updateNode() {
            if (this.selectedNode) {
                this.selectedNode.tag = this.editTag;
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
};
</script>
<template>
    <div id="app">
        <h1>HTML Tree Structure</h1>

        <!-- فراخوانی کامپوننت TreeNode -->
        <TreeNode :node="treeData" :selected-node="selectedNode" @select-node="selectNode" />

        <!-- نمایش جزئیات و عملیات CRUD -->
        <div v-if="selectedNode" class="node-details">
            <h2>Selected Node</h2>
            <p><strong>Tag:</strong> {{ selectedNode.tag }}</p>
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
</template>
<style>
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
    margin-bottom: 20px;
}

.node-details {
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
}
</style>