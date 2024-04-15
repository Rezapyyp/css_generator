// // D-0
// let tags = {"html":null }
// // D-1
// tags["html"] = {"head":null , "body":null}
// // D-2
// tags["html"]["head"] = {"meta":null , "link":null , "title":null}
// tags["html"]["body"] = {"nav":null , "main":null , "footer":null}
// // D-3
// tags["html"]["body"]["nav"] = {"ul":null}
// tags["html"]["body"]["main"] = {"h1":null , "p":null}
// // D-4
// tags["html"]["body"]["nav"]["ul"] = {"li":"null1" , "li":"null2" , "li":"null3" , "li":"null4"}

// console.log(tags);



















// console.log(attrs.keys.length);
// let attrs_length = Object.keys(attrs).length

// class Tag{
//     constructor(tagName , classList=[] , attrs = {} , props = [] , ){
//         this.tagName = tagName 
//         this.classList = classList
//         this.attrs = attrs 
//         this.props = props 
//     }

//     get_id(){
//         if( Boolean(typeof this.attrs.id_attr === "string" & this.attrs.id_attr !== "undefined" ) ){
//             return this.attrs.id_attr
//         }
//         else{
//             return ""
//         }
//     }
//     get_classList(){
//         // if ( Boolean((Array.isArray(this.classList) & typeof this.classList !== "undefined")) ){
//         //     return this.classList.toString().replace(/,/g , " ")
//         // }
//         // else{
//         //     return ""
//         // }
//         return this.classList.toString().replace(/,/g , " ")
//     }
//     get_name(){
//         if( Boolean(typeof this.attrs.name_attr === "string" & this.attrs.name_attr !== "undefined" ) ){
//             return this.attrs.name_attr
//         }
//         else{
//             return ""
//         }
//     }
//     get_type(){
//         if( Boolean(typeof this.attrs.type_attr === "string" & this.attrs.type_attr !== "undefined" ) ){
//             return this.attrs.type_attr
//         }
//         else{
//             return ""
//         }
//     }
//     get_value(){
//         if( Boolean(typeof this.attrs.value_attr === "string" & this.attrs.value_attr !== "undefined" ) ){
//             return this.attrs.value_attr
//         }
//         else{
//             return ""
//         }
//     }
//     get_attrs(){
//         let result = ""
//         if( Boolean(this.get_id()) ){
//             result = result + `id="${this.get_id()}" `
//             if( Boolean(this.get_classList()) ){
//                 result = result + `class="${this.get_classList()}" `
//             }
//             if( Boolean(this.get_name()) ){
//                 result = result + `name="${this.get_name()}" `
//             }
//             if( Boolean(this.get_type()) ){
//                 result = result + `type="${this.get_type()}" `
//             }
//             if( Boolean(this.get_value()) ){
//                 result = result + `value="${this.get_value()}" `
//             }
//             return result
//         }
//         else{
//             return "invalid attrbiuts --- plese enter a valid ID"
//         }
        
        
//     }

//     get_props(){
//         return this.props.toString().replace(/,/g , "  ")
//     }

    

//     get_tag(){
//         let result = `<${this.tagName} ${this.get_attrs()} ${this.get_props()}  > . . . </${this.tagName}>`
//         return result   
        
//     }
// }





// // const obj = new Tag(tagName="h1" , attrs = {name_attr:"box" , value_attr:"50px" , id_attr : "myBox"  , type_attr : "input", classList :["center" , "mt-3" , "p6"] } ,  props=["checked" , "prop1" , "prop2" ,] )
// const obj = new Tag(tagName="div" , classList=["main" , "center"] , attrs = {name_attr:"name" , id_attr:"id", } ,  props=["checked" , "prop1" , "prop2" ,] )
// console.log(obj.get_tag());


