"""
92: Web Application Firewall (WAF)
Intercept and analyze HTTP requests for SQL injection attempts.
"""
def inspect_request(query_params):
    sql_patterns = ["UNION SELECT", "1=1", "--", "DROP TABLE"]
    for pattern in sql_patterns:
        if pattern in query_params.upper():
            return False, "SQL Injection Attempt Blocked!"
    return True, "Request Allowed"

if __name__ == "__main__":
    allowed, msg = inspect_request("user_id=1 OR 1=1--")
    print("WAF Result:", msg)
