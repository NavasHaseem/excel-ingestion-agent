# Excel Ingestion Agent

A Python-based agent that parses uploaded Excel files and normalizes test cases into canonical JSON format.

## Features

- **Excel Parsing**: Extract test case data from Excel files (`.xlsx`, `.xls`)
- **Normalization**: Convert raw test case data into a canonical format
- **JSON Output**: Generate well-structured JSON files with normalized test cases
- **REST API**: Flask-based API for uploading and processing files
- **Data Validation**: Automatic validation and normalization of test case data
- **Error Handling**: Comprehensive error reporting and logging

## Project Structure

```
.
├── app.py                    # Flask application entry point
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── uploads/                  # Directory for uploaded Excel files
├── output/                   # Directory for generated JSON files
├── src/
│   ├── agent.py             # Main orchestration agent
│   ├── parser.py            # Excel file parser
│   ├── normalizer.py        # Test case normalizer
│   └── models.py            # Data models and enums
└── tests/
    ├── test_parser.py       # Parser tests
    └── test_normalizer.py   # Normalizer tests
```

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. Clone or navigate to the project directory:
   ```bash
   cd "Excel Ingestion Agent"
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Flask Application

Start the Flask server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

### API Endpoints

#### 1. **Health Check**
```
GET /health
```
Check if the service is running.

**Response:**
```json
{
  "status": "healthy",
  "service": "Excel Ingestion Agent"
}
```

#### 2. **Upload and Process File**
```
POST /upload
Content-Type: multipart/form-data
```

Upload an Excel file to parse and normalize test cases.

**Example using curl:**
```bash
curl -X POST -F "file=@test_cases.xlsx" http://localhost:5000/upload
```

**Response:**
```json
{
  "status": "success",
  "message": "Successfully processed 5 test cases",
  "test_cases_count": 5,
  "output_file": "output/test_cases_canonical_20240128_120000.json",
  "test_cases": [
    {
      "id": "TC-001",
      "title": "Login with valid credentials",
      "description": "Verify user can login",
      "priority": "high",
      "status": "active",
      "steps": [...],
      "tags": ["auth", "smoke"]
    }
  ]
}
```

#### 3. **Get Excel Template**
```
GET /template
```

Get the expected Excel file structure.

**Response:**
```json
{
  "columns": ["id", "title", "description", ...],
  "example_row": {...},
  "notes": [...]
}
```

#### 4. **Get Agent Info**
```
GET /info
```

Get information about the agent and available endpoints.

## Excel File Format

Your Excel file should have the following columns:

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| id | String | Yes | Unique test case identifier (e.g., TC-001) |
| title | String | Yes | Test case title |
| description | String | Yes | Test case description |
| preconditions | String | No | Prerequisites for running the test |
| steps | String | No | Test steps separated by newlines, use `|` to separate action from expected result |
| expected_result | String | No | Overall expected result |
| priority | String | No | critical, high, medium, low (default: medium) |
| status | String | No | active, deprecated, draft (default: active) |
| tags | String | No | Comma-separated tags |
| module | String | No | Module or component name |

### Example Excel Row

```
id: TC-001
title: Login with valid credentials
description: Verify user can login with valid username and password
preconditions: User account exists, browser is open
steps: Open login page | Login page displays
       Enter username | Username field populated
       Enter password | Password field populated
       Click login | Dashboard displays
expected_result: User is logged in successfully
priority: high
status: active
tags: authentication,login,smoke-test
module: Auth
```

## Output JSON Format

Generated JSON files contain normalized test cases:

```json
{
  "metadata": {
    "generated_at": "2024-01-28T12:00:00.000000",
    "source_file": "test_cases.xlsx",
    "test_cases_count": 5
  },
  "test_cases": [
    {
      "id": "TC-001",
      "title": "Login with valid credentials",
      "description": "Verify user can login",
      "preconditions": "User account exists",
      "steps": [
        {
          "step_number": 1,
          "action": "Open login page",
          "expected_result": "Login page displays"
        }
      ],
      "expected_result": "User is logged in successfully",
      "priority": "high",
      "status": "active",
      "tags": ["authentication", "login"],
      "module": "Auth",
      "created_date": null,
      "last_modified": null
    }
  ]
}
```

## Running Tests

Run the test suite:

```bash
python -m pytest tests/ -v
```

Or using unittest:

```bash
python -m unittest discover tests/
```

## Development

### Project Dependencies

- **Flask**: Web framework
- **Flask-CORS**: Cross-Origin Resource Sharing
- **openpyxl**: Excel file handling
- **pandas**: Data manipulation
- **Werkzeug**: WSGI utilities

### Extending the Agent

To add new fields or modify test case structure:

1. Update `src/models.py` with new fields
2. Update `src/parser.py` to extract the new fields
3. Update `src/normalizer.py` if normalization logic is needed
4. Update tests accordingly

## Error Handling

The agent provides clear error messages:

- **File not found**: Returns 404 with message
- **Invalid file type**: Returns 400 with message
- **Missing required fields**: Test cases are skipped with logging
- **Parse errors**: Partial results with error details

## Limits

- **Maximum file size**: 10MB
- **Allowed formats**: `.xlsx`, `.xls`
- **Required fields**: `id` and `title` (all others are optional)

## Future Enhancements

- [ ] Support for additional Excel sheet formats
- [ ] Batch processing of multiple files
- [ ] Custom mapping configuration
- [ ] Database storage integration
- [ ] Test case deduplication
- [ ] Advanced filtering and querying
- [ ] API documentation (Swagger/OpenAPI)

## License

This project is provided as-is for internal use.

## Support

For issues or questions, please contact the development team.
