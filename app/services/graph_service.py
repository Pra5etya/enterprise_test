from app.extension.arango import arango

def get_related_products(product_id):
    query = """
    FOR v, e IN 1..2 OUTBOUND @product GRAPH 'supply_chain'
        RETURN v
    """

    cursor = arango.get_db().aql.execute(query, bind_vars = {"product": f"products/{product_id}"})
    
    return [doc for doc in cursor]
