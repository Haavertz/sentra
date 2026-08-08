# Sentra

Sentra is a server and API monitoring platform under development with FastAPI. Its goal is to provide uptime tracking, response-time metrics, incident detection, and real-time service monitoring.

The project is currently in its initial learning stage. It already provides an API for registering and managing monitors, but it does not perform automatic uptime checks yet.

## Current features

- Create a monitor with a name and URL.
- Validate monitor URLs with Pydantic.
- List all registered monitors.
- Get a monitor by ID.
- Delete a monitor by ID.
- Display registered monitors on a Jinja2 home page.
- Explore the API through the automatically generated FastAPI documentation.

Monitor data is currently stored in memory. It is lost whenever the application restarts.

## Technologies

- Python
- FastAPI
- Pydantic
- Jinja2
- Pytest
- HTTPie

## Project structure

```text
sentra/
├── db/
│   └── client.py            # Temporary in-memory database
├── routers/
│   ├── home.py              # HTML home page
│   └── monitors.py          # Monitor API routes
├── static/
│   └── css/
│       └── home.css         # Home page styles
├── templates/
│   └── home/
│       └── index.html       # Home page template
├── tests/
│   └── test_monitors.py     # Test setup (test cases are still pending)
├── utils/
│   ├── html.py              # Templates and static-file configuration
│   └── request_model.py     # Pydantic request models
├── main.py                  # FastAPI application entry point
├── requirement.txt          # Python dependencies
└── run                      # Development server script
```

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd sentra
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirement.txt
```

## Running the application

Start the development server with:

```bash
./run
```

Alternatively:

```bash
fastapi dev main.py
```

The application will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Render the HTML home page |
| `POST` | `/monitors/` | Create a monitor |
| `GET` | `/monitors/` | List all monitors |
| `GET` | `/monitors/{monitor_id}` | Get a monitor by ID |
| `DELETE` | `/monitors/{monitor_id}` | Delete a monitor by ID |

## HTTPie examples

Create a monitor:

```bash
http POST :8000/monitors/ name=Sentra url=https://example.com
```

List all monitors:

```bash
http GET :8000/monitors/
```

Get monitor `1`:

```bash
http GET :8000/monitors/1
```

Delete monitor `1`:

```bash
http DELETE :8000/monitors/1
```

## Running tests

Run the test suite from the project root:

```bash
python -m pytest -q
```

The test structure exists, but API test cases still need to be implemented.

## Roadmap

- Add automated API tests.
- Store monitors in SQLite instead of memory.
- Perform periodic HTTP health checks.
- Measure and store response times.
- Track monitor status and uptime history.
- Detect and record incidents.
- Add a monitoring dashboard.
- Provide real-time status updates.

## Development status

Sentra is a learning project and is not ready for production use yet.
