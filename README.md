### To run the frontend

Clone the project

```bash
  git clone https://github.com/PCD-EchipaRacheta/on-premise-app.git
```

Go to the frontend directory

```bash
  cd frontend
```

Install dependencies

```bash
  npm install
```

Run dev server

```bash
  npm run dev
```

### To run the backend

Go to the frontend directory

```bash
  cd backend
```

Create a virtual env

```bash
  python -m venv venv
```

Activate the env

```bash
  venv\Scripts\activate
```

Install dependencies

```bash
    pip install -r requirements.txt
```

Run the server

```bash
    uvicorn main:app --reload --port 8000
```