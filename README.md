## E-Commerce Microservices Platform
### IT4020 — Modern Topics in IT | Year 4 Semester 1 | SLIIT 2026

## Project Overview
This project implements a microservices backend architecture for an 
e-commerce platform. The system is split into 6 independent microservices, 
each handling one business responsibility, all accessible through a single 
API Gateway.

## Group Members
| Member   | Service              | Port |
|----------|----------------------|------|
| ABI      | API Gateway          | 8000 |
| ABI      | Product Service      | 8001 |
| Harithra | Customer Service     | 8002 |
| Savin    | Order Service        | 8003 |
| Rochelle | Inventory Service    | 8004 |
| Maneth   | Payment Service      | 8005 |
| Suhani   | Notification Service | 8006 |

## How to Run
Terminal 1: cd product_service      && uvicorn main:app --reload --port 8001

Terminal 2: cd customer_service     && uvicorn main:app --reload --port 8002

Terminal 3: cd order_service        && uvicorn main:app --reload --port 8003

Terminal 4: cd inventory_service    && uvicorn main:app --reload --port 8004

Terminal 5: cd payment_service      && uvicorn main:app --reload --port 8005

Terminal 6: cd notification_service && uvicorn main:app --reload --port 8006

Terminal 7: cd api_gateway          && uvicorn main:app --reload --port 8000

## Swagger UI
http://localhost:8000/docs - API Gateway (all 30 routes)

http://localhost:8001/docs - Product Service

http://localhost:8002/docs - Customer Service

http://localhost:8003/docs - Order Service

http://localhost:8004/docs - Inventory Service

http://localhost:8005/docs - Payment Service

http://localhost:8006/docs - Notification Service
