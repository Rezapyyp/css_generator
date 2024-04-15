from fastapi.middleware.cors import CORSMiddleware
from tag_model import get_neo4j_db , Folder # , Tag 
from fastapi import FastAPI , Depends
from pydantic import BaseModel



app = FastAPI()
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/createFolder" , status_code=201 ) #,response_model=Tag 
def add_child_tag_to(folder:Folder ,db = Depends(get_neo4j_db)):
    query = 'CREATE (f:Folder{name:'+f"'{folder.name}'"+'})'
    try :
        db.execute_query(query)
    except Exception as e :
        raise e
    return {"f_msg":"fast api is ok"}
    



