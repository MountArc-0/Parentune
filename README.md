# 🧠 Parenting Q&A Platform – Django Backend

A modular, scalable backend system built using Django and Django REST Framework. This project supports JWT authentication, user profiling, Q&A interaction, personalized feeds, and is structured to extend with real-time notifications and analytics.

---

## 🔧 Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Auth:** JWT (SimpleJWT)
- **Async/Real-time Ready:** Django Channels, Celery (Planned)
- **Caching & Queues:** Redis (Planned)
- **Dev Tools:** Postman, Docker (optional)

---

## ✅ Completed Modules

### 1. Authentication
- **JWT** based auth system with `access` and `refresh` tokens.
- **Endpoints:**
  - `POST /api/auth/register/`
  - `POST /api/auth/login/`
  - `POST /api/auth/token/refresh/`

---

### 2. Profile
- Manages user demographic info (location, children, age).
- Auto-created upon first access.
- **Endpoints:**
  - `GET /api/profiles/me/`
  - `PATCH /api/profiles/me/`

---

### 3. QnA (Questions & Answers)
- Ask questions, add tags, post answers.
- Tag management & nested serializers.
- **Endpoints:**
  - `POST /api/qna/questions/`
  - `GET /api/qna/questions/`
  - `POST /api/qna/answers/`
  - `GET /api/qna/answers/`
  - `GET /api/qna/tags/`

---

### 4. Feed
- Caches user-specific feed (questions, tags).
- Stored as JSON for optimized retrieval.
- **Endpoints:**
  - `POST /api/feed/` (generate feed)
  - `GET /api/feed/` (retrieve feed)

---

## 🕒 Upcoming Modules

### 5. Notifications (Planned)
- Real-time updates (WebSocket)
- Push alerts for answers, tags, mentions

### 6. Analytics (Planned)
- Page visits, engagement stats
- Celery + Kafka for async tracking

---

## 🗃️ Database Schema

- SQL schema available at: [`schema.sql`](./schema.sql)
- Uses Django migrations by default

---

## 📮 Postman Collection

- Full API Collection available: [Insert Link Here]
- Includes login, auth token refresh, CRUD for all models

---

## 📂 Folder Structure

