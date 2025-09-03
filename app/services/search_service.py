from flask import current_app

def search_products(keyword):
    es = current_app.elastic
    result = es.search(
        index = "products",
        query = {"match": {"name": keyword}}
    )

    return [hit["_source"] for hit in result["hits"]["hits"]]
