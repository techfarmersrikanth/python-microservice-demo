4️⃣ Run It 🚀

From the root folder (python-microservices-demo):

docker compose up --build


Wait until both services start.

5️⃣ Test the Endpoints 🧪
✅ Call user-service directly:

Open in browser / Postman:

http://localhost:5001/users


Output:

["Ravi", "Sita", "John"]

✅ Call order-service (this calls user-service internally):
http://localhost:5002/orders


Output:

{
  "message": "Orders fetched successfully",
  "users_from_user_service": ["Ravi", "Sita", "John"]
}