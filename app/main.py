from fastapi import FastAPI

app = FastAPI(title="FastAPI, docker and traefik")


list1 = ''
@app.get("/")
def read_root():
    if list1 == '':
        return 'Empty list'
    return list1


@app.post('/test')
def posting(item):
    list1.append(item)