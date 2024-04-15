from __future__ import annotations
from typing import  List , Optional
from enum import Enum
from pydantic import BaseModel , ConfigDict #, Field , field_validator , ValidationError 

# def folderEntity(item) -> dict:
#     return {
#         "id" : str(item["_id"]) ,
#         "name" : item["name"] ,
#         "html_file" : item["html_file"]
#     }

# def foldersEntity(entity) -> list:
#     return [ folderEntity(item) for item in entity ]


from neo4j import GraphDatabase


    
def get_neo4j_db():
    try :
        URI =  "neo4j://localhost:7687"
        AUTH = ("neo4j", "reza1212")

        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            driver.verify_connectivity()
            yield driver
    finally :
        driver.close()


class TagName(str , Enum):
    html = "html"
    body = "body"
    head = "head"
    meta = "meta"
    # link = "link"
    footer = "footer"
    header = "header"
    link = "link"
    div = "div"
    span = "span"
    main = "main"
    a = "a"
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    p = "p"


# class Tag(BaseModel): 
#     model_config = ConfigDict(use_enum_values=True)
    
#     tagName : TagName
#     id_attr_parent : str
#     id_attr : str
#     class_attr : None | str = None
#     isBlockElement : bool = True



# class Tags(Tag):
#     children :  List[Tag] | None = []


# class Folder(BaseModel):
#     name : str
#     html_file : Tag = None
#     # css_file : 
    
    
#     # @field_validator(mode="after" , __field="name")
#     # def my_validator(value):
#     #     print(type(value).__name__)
#     #     if value.isalpha():
#     #         return value
#     #     else :
#     #         raise ValidationError("Erorr 403")
        
            
class Folder(BaseModel):
    name: str

    