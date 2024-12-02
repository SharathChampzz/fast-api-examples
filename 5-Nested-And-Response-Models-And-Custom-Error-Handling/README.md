# FastAPI Nested Models, Response Models, and Custom Error Handling

This project demonstrates the following key concepts in FastAPI:
1. **Nested Models**: Handling complex data structures where one model contains other models.
2. **Response Models**: Structuring API responses to control the output format.
3. **Custom Error Handling**: Creating user-friendly error messages using custom exception classes.

---

## **Basic Concepts to Understand the Code**

### **1. Nested Models**
In FastAPI, a **nested model** is a model that contains other models within it. For instance, an `Order` might contain a list of `Item` objects. This helps represent complex data structures, like an order with multiple items, in a clean and maintainable way.

### **2. Response Models**
A **response model** is used to define the structure of the response returned by an API endpoint. It allows you to ensure consistency in the output, such as excluding certain fields or including computed fields (like a total price). Using response models helps in controlling what gets returned to the user, making the API cleaner and more predictable.

### **3. Custom Error Handling**
Custom error handling in FastAPI allows you to create specific exception classes that define how errors should be presented to the user. This is useful for providing clear, user-friendly error messages when something goes wrong, such as when an item is not found in an order. By defining custom exceptions, we can return structured, meaningful error messages instead of generic ones.

---

## **What the Code Does**

In this script:
- We define models for **Item** and **Order** to represent the structure of an order and its items.
- We calculate the **total price** for an order and return a summary of the order using a **response model**.
- We handle cases where an item or an order might not be found by raising **custom errors**, ensuring that users get informative messages.
- The app has endpoints to **create**, **retrieve**, **delete**, and **search** for orders and items.

---

This project gives a hands-on example of how to use FastAPI to handle nested data models, format API responses, and manage errors in a user-friendly way.
