
#############   CREATE   #############
def craete_node(labels:list,props:dict ):
        query_method = 'CREATE'
        labels_str = ":".join(labels)
        props_str = ", ".join([ f"{key}:'{value}'" for key,value in props.items()  ])
        # query = query_method + "  (:" + labels_str +  "{" + props_str + "}" + ")  "
        query = query_method + "  (n:" + labels_str +  "{" + props_str + "}" + ")  RETURN n"
        
        
        
        print(query)


labels = ["Tag" ,"void" ,"block"]
props = {"tag_name":"html" ,"id_attr":"box" ,}

craete_node(labels,props)


#############   DELETE ALL   #############

def delete_all_nodes():
    query = "MATCH (n) DETACH DELETE n"


