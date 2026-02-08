from fastapi import FastAPI, Query

app = FastAPI()

PRODUCTS = [
    {"id": 1, "name": "Notebook Lenovo ThinkPad", "price": 1200},
    {"id": 2, "name": "Notebook HP Pavilion", "price": 980},
    {"id": 3, "name": "Mouse Logitech inalámbrico", "price": 25},
    {"id": 4, "name": "Teclado mecánico Redragon", "price": 70},
]

@app.get("/")
def healthcheck():
    return {
        "status": "ok",
        "service": "mini-search-engine"
    }

@app.get("/search")
def search(q: str = Query(..., min_length=1)):
    results = [
        p for p in PRODUCTS
        if q.lower() in p["name"].lower()
    ]

    return {
        "query": q,
        "total": len(results),
        "results": results
    }
