<script>
export default {
    name: 'Folder', // necessary for self-reference
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


    },

}
</script>
<template>
  <div id="">
    ff
  </div>
</template>
<style scoped>

div{
    width: 100%;
    height: 2rem;
    background-color: rgb(177, 43, 43);
    text-align: center;
    font-size: 20px;
    outline: none;
    border: none;
}

</style>