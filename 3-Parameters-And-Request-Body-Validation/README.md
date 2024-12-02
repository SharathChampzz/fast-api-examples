# FastAPI Examples

This project contains examples demonstrating various FastAPI features, including:

1. **Path Parameters**
   - Endpoint: `/items/{item_id}`
   - Description: Retrieve item details using a path parameter.

2. **Query Parameters**
   - Endpoint: `/search/`
   - Description: Search items with optional query parameters like `q` and `limit`.

3. **JSON Request Body**
   - Endpoint: `/items/`
   - Description: Accept a JSON body to create an item.

4. **Validation with Pydantic**
   - Endpoint: `/validated-items/`
   - Description: Use Pydantic to validate JSON request bodies with constraints.

5. **Combine Path, Query, and JSON Body**
   - Endpoint: 
     - `/items/{item_id}/` (GET) - Fetch item details with an optional query.
     - `/items/{item_id}/` (PUT) - Update an item using its ID and a JSON body.

---

## How to Run

1. Install dependencies:
   ```pip install fastapi uvicorn```


## Summary
```Path Parameters```: Defined in the URL path and annotated with their type.

```Query Parameters```: Have default values and are not Pydantic models.

```Body Parameters```: Are instances of Pydantic models.