from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Hello I am reza" , "age":22 , "is_ok":True , "not_exist":None}


@app.get("/add/{num1}/{num2}")
def math(num1: int , num2: int):
    question = f"{num1} + {num2}"
    answer = num1 + num2
    return {"number1": num1,"number2": num2 , "question" : question , "answer": answer}


@app.get("/div/{num1}/{num2}")
def math(num1: int , num2: int):
    question = f"{num1} / {num2}"
    data = {"number1": num1,"number2": num2 , "question" : question}
    if num2 != 0 :
        answer = num1 / num2
        data["answer"] = answer
        return data
    else :
        data["answer"] = "Erorr Number2 can not be Zero "
        return data
        return data


@app.get("/kam/{num1}/{num2}")
def math(num1: int , num2: int):
    question = f"{num1} - {num2}"
    answer = num1 - num2
    return {"number1": num1,"number2": num2 , "question" : question , "answer": answer}


@app.get("/zarb/{num1}/{num2}")
def math(num1: int , num2: int):
    question = f"{num1} * {num2}"
    answer = num1 * num2
    return {"number1": num1,"number2": num2 , "question" : question , "answer": answer}




if __name__ == "__main__" :
    uvicorn.run(app)