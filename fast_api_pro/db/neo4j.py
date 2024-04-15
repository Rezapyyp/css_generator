
# important !!!
# from neo4j import Record , Result
# from neo4j.graph import Node

from neo4j import GraphDatabase, RoutingControl 
from neo4j.exceptions import DriverError, Neo4jError
import logging


class BaseApp :
    
    def __init__(self, uri, user, password, database="neo4j"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.database = database

    def close(self):
        self.driver.close()


class App(BaseApp):

    def craete_tag(self,props:dict): # ,name_attr,class_attr,value_attr
        query_method = 'CREATE'
        props_str = ", ".join([ f"{key}:'{value}'" for key,value in props.items()  ])
        try:
            query = query_method + "  (n:Tag {" + props_str + "}" + ")  RETURN n AS tag"
            result = self.driver.execute_query(query , database_=self.database, result_transformer_= lambda r : r.value("tag"))
            return result
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise


    def get_all(self):
        ...
    
    def delete_all_tags(self):
        query = "MATCH (n:Tag) DETACH DELETE n "
        try:
            self.driver.execute_query(query, database_=self.database,)
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise


    # وقتی یه نود حذف میشه : کل نسلش هم حذف میشه
    def delte_tag(self,tag_id):
        query = f"MATCH (n:Tag) WHERE (ID(n)={tag_id}) DELETE n"
        try:
            self.driver.execute_query(query, database_=self.database,)
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise
    
    def return_tag(self,tag_id):
        query = f"MATCH (n:Tag) WHERE (ID(n)={tag_id}) RETURN n AS node"
        try:
            result = self.driver.execute_query(query, database_=self.database,
                                               result_transformer_= lambda r : r.values("node")
                                               )
            return result[0][0].items()
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise
        

    def get_properties(self,tag_id):
        query = f"MATCH (n:Tag) WHERE (ID(n)={tag_id}) RETURN PROPERTIES(n) AS props "
        try:
            result = self.driver.execute_query(query, database_=self.database,
                                               result_transformer_=lambda r: r.value("props")
                                               )
            # return .records[0].data()
            return result
            
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise

    def set_prop(self,tag_id,prop_name,value):
        if type(value).__name__=="str" or type(value).__name__=="int" :
            query = f"MATCH (n:Tag) WHERE (ID(n)={tag_id}) SET n.{prop_name}={value}"
            try :
                self.driver.execute_query(query, database_=self.database,)
            except (DriverError, Neo4jError) as exception:
                logging.error("%s raised an error: \n%s", query, exception)
                raise
        else :
            raise ValueError("type of value must be a *(str) or (int)* ")
    
    def remove_prop(self,tag_id,prop_name):
        query = f"MATCH (n:Tag) WHERE (ID(n)={tag_id}) REMOVE n.{prop_name}l"
        try:
            self.driver.execute_query(query, database_=self.database,)
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise
    
    
    def set_label(self,tag_id,LABELNAME):
        if type(LABELNAME).__name__=="str" :
            query = f"MATCH (n:Tag) WHERE (ID(n)={tag_id}) SET n:{LABELNAME}"
            try :
                self.driver.execute_query(query, database_=self.database,)
            except (DriverError, Neo4jError) as exception:
                logging.error("%s raised an error: \n%s", query, exception)
                raise
        else :
            raise ValueError("type of value must be a *(str)* ")
    
    def remove_label(self,tag_id,LABELNAME):
        query = f"MATCH (n:Tag) WHERE (ID(n)={tag_id}) REMOVE n:{LABELNAME}"
        try:
            self.driver.execute_query(query, database_=self.database,)
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise
    
    
    def add_child_to_parent(self,parent_id,child_id):
        if type(parent_id).__name__=="int" or type(child_id).__name__=="int" :
            query = f"match (p),(ch) where ID(p)={parent_id} AND ID(ch)={child_id} create (p)-[:HAS_CHILD]->(ch)"
            try:
                self.driver.execute_query(query, database_=self.database)
            except (DriverError, Neo4jError) as exception:
                logging.error("%s raised an error: \n%s", query, exception)
                raise
        else :
            raise ValueError("type of parent_id and child_id must be a *(int)* ")
    
    def get_childs(self,tag_id):
        if type(tag_id).__name__=="int":
            query = f"MATCH (p)-[r]-(ch) WHERE ID(p)={tag_id}  RETURN p,ch "
            try:
                self.driver.execute_query(query, database_=self.database)
            except (DriverError, Neo4jError) as exception:
                logging.error("%s raised an error: \n%s", query, exception)
                raise
        else :
            raise ValueError("type of tag_id and must be a *(int)* ")
    
    def get_NASL(self,tag_id):
        if type(tag_id).__name__=="int":
            query = f"MATCH (p)-[r*]-(ch) WHERE ID(p)={tag_id}  RETURN p,ch "
            try:
                self.driver.execute_query(query, database_=self.database)
            except (DriverError, Neo4jError) as exception:
                logging.error("%s raised an error: \n%s", query, exception)
                raise
        else :
            raise ValueError("type of tag_id and must be a *(int)* ")
    
    
    
    
    # Create node   $
    # Delete ‌node   $
    # Return node  -->  get_properties , $
    # Upadte node  -->  set_prop , remove_prop , set_label , remove_label    $
    
    
    # add_child_to_parent   $
    # گرفتن بچه‌های یک نود
    # get_childs    $
    # حذف بچه‌های یک نود
    # اپدیت بچه‌های یک نود

    # حذف یک نسل با داشتن پدرش

    # گرفتن داداش های یک نود
    # get_NASL  $
    # گرفتن پدر یک نود
    # گرفتن اجداد یک نود
    
    
    # ساخت OrderID برای بچه ها 
    
    
    # JSON
    # برگردوندن یک نسل به صورت جیسون



# if __name__ == "__main__":
    # uri = "neo4j://localhost:7687"
    # user = "neo4j"
    # password = "reza1212"
    # app = App(uri, user, password )
    # try:
    #     props = {"tag_name":"html" ,"id_attr":"box" ,}
    #     print(app.craete_tag(props))
        # app.craete_tag("html",None,"")
        # app.create_tag("head")
        # app.create_tag("main")
        # app.create_tag("div")
        # app.create_tag("h1")
        # app.create_tag("a")
        # app.create_tag("p")
        
        # app.add_child_to_parent(10,1)
        # app.add_child_to_parent(10,0)
        # app.add_child_to_parent(0,2)
        # app.add_child_to_parent(0,3)
        # app.add_child_to_parent(3,6)
        # app.add_child_to_parent(6,4)
        # app.add_child_to_parent(4,5)
        
        # app.remove_label(4,"lablab")
        
        # print(app.return_tag(0))
        
        ...    
        
    # finally:
    #     app.close()