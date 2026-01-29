# Excel Ingestion Agent

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Python-based agent that parses uploaded Excel files and normalizes test cases into canonical JSON format. Deploy locally as a CLI tool or on AWS EC2 as a web service.

## Features

- **Excel Parsing**: Extract test case data from `.xlsx` and `.xls` files
- **Data Normalization**: Convert raw test case data into canonical format
- **JSON Output**: Generate well-structured JSON with metadata
- **REST API**: Flask-based API for uploading and processing files
- **Web UI**: Beautiful HTML interface for file uploads
- **CLI Tools**: Standalone command-line interfaces
- **Data Validation**: Automatic validation and normalization of test cases
- **Error Handling**: Comprehensive error reporting
- **AWS Ready**: Includes EC2 deployment configuration

## Quick Start

### Local Usage (CLI)

```bash
# Install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Process an Excel file
python agent.py test_cases.xlsx
python agent_cli.py test_cases.xlsx -o ./output -p

# Or use as Python module
python
>>> from agent import process_excel_file
>>> result = process_excel_file('test_cases.xlsx')
>>> print(result)
```

### Web Service (Local)

```bash
# Start Flask app
python app.py

# Access in browser
http://localhost:5000/
```

### AWS EC2 Deployment

```bash
# See DEPLOYMENT.md for detailed instructions
bash ec2-setup.sh
sudo systemctl start excel-agent
```

Access from local machine: `http://your-ec2-ip:5000/`

## Project Structure

```
.
├── app.py                      # Flask web application
├── agent.py                    # Standalone Python API
├── agent_cli.py                # CLI tool with advanced options
├── config.py                   # Configuration management
├── requirements.txt            # Python dependencies
├── upload.html                 # Web UI
├── ec2-setup.sh               # EC2 deployment script
├── excel-agent.service        # Systemd service file
├── DEPLOYMENT.md              # Deployment guide
├── src/
│   ├── agent.py               # Main orchestration agent
│   ├── parser.py              # Excel file parser
│   ├── normalizer.py          # Test case normalizer
│   └── models.py              # Data models
├── tests/
│   ├── test_parser.py
│   └── test_normalizer.py
├── uploads/                   # Uploaded files (auto-created)
└── output/                    # Generated JSON files (auto-created)
```

## Excel File Format

Your Excel file should have these columns:

| Column | Example | Required |
|--------|---------|----------|
| Test Case ID | TC-001 | ✓ Yes |
| Description | Login test | ✓ Yes |
| Preconditions | User logged out | No |
| Steps | 1. Click login\|2. Enter password | No |
| Expected Result | User authenticated | No |

Supported column names:
- `Test Case ID`, `id`, `ID`
- `Description`, `title`
- `Preconditions`, `preconditions`
- `Steps`, `steps`
- `Expected Result`, `expected_result`
- `Priority` (critical, high, medium, low)
- `Status` (active, deprecated, draft)
- `Tags` (comma-separated)
- `Module`, `module`

## API Endpoints

### GET /
Serves the web UI upload form

### POST /upload
Upload and process Excel file
```bash
curl -F "file=@test_cases.xlsx" http://localhost:5000/upload
```

### GET /health
Health check
```bash
curl http://localhost:5000/health
```

### GET /template
Get template structure
```bash
curl http://localhost:5000/template
```

### GET /info
Agent information
```bash
curl http://localhost:5000/info
```

## Output Format

The agent generates JSON files with the following structure:

```json
{
  "metadata": {
    "generated_at": "2026-01-29T12:00:00.000000",
    "source_file": "test_cases.xlsx",
    "test_cases_count": 5
  },
  "test_cases": [
    {
      "id": "TC-001",
      "title": "Login test",
      "description": "Verify user login",
      "preconditions": "User has account",
      "steps": [
        {
          "step_number": 1,
          "action": "Click login button",
          "expected_result": "Login form displays"
        }
      ],
      "expected_result": "User authenticated",
      "priority": "high",
      "status": "active",
      "tags": ["auth", "smoke"],
      "module": "Authentication",
      "created_date": null,
      "last_modified": null
    }
  ]
}
```

## Configuration

Create a `.env` file to customize settings:

```env
DEBUG=False
HOST=0.0.0.0
PORT=5000
UPLOAD_FOLDER=uploads
OUTPUT_FOLDER=output
MAX_FILE_SIZE=52428800
CORS_ORIGINS=*
```

## Testing

```bash
# Run tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_parser.py -v
```

## Deployment

### Local Development
```bash
python app.py
```

### Production (EC2)
See [DEPLOYMENT.md](DEPLOYMENT.md) for:
- EC2 setup and configuration
- Systemd service setup
- Nginx reverse proxy configuration
- HTTPS/SSL setup
- Security best practices

### Docker (Coming Soon)
```bash
docker build -t excel-agent .
docker run -p 5000:5000 excel-agent
```

## Technologies Used

- **Python 3.8+**
- **Flask 2.3.3** - Web framework
- **pandas 2.0.3** - Data processing
- **openpyxl 3.1.5** - Excel parsing
- **Werkzeug 2.3.7** - WSGI utilities
- **Flask-CORS 4.0.0** - CORS support

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or suggestions:
1. Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
2. Open an issue on GitHub
3. Contact the development team

## Roadmap

- [ ] Docker support
- [ ] Database integration (PostgreSQL)
- [ ] Advanced filtering and querying
- [ ] Batch processing API
- [ ] Test case deduplication
- [ ] S3 integration for large files
- [ ] OpenAPI/Swagger documentation
- [ ] Admin dashboard

## Version History

### v1.0.0 (2026-01-29)
- Initial release
- Excel parsing and normalization
- Flask web API
- CLI tools
- AWS EC2 deployment support
