"""
98: GraphQL API
Use Graphene to handle complex, nested relational queries.
"""
def execute_graphql_query(query_str):
    print(f"Executing GraphQL query: {query_str}")
    return {"data": {"user": {"id": "1", "name": "Alice"}}}

if __name__ == "__main__":
    res = execute_graphql_query("{ user { id name } }")
    print("Result:", res)
