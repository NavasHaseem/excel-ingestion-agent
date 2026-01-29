"""Flask application for Excel Ingestion Agent."""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from pathlib import Path

from src.agent import ExcelIngestionAgent

# Load configuration
try:
    from config import DEBUG, HOST, PORT, UPLOAD_FOLDER, OUTPUT_FOLDER, MAX_FILE_SIZE, CORS_ORIGINS
except ImportError:
    # Fallback defaults
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 5000
    UPLOAD_FOLDER = 'uploads'
    OUTPUT_FOLDER = 'output'
    MAX_FILE_SIZE = 10 * 1024 * 1024
    CORS_ORIGINS = '*'

ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

# Create Flask app
app = Flask(__name__)
CORS(app, origins=CORS_ORIGINS.split(',') if CORS_ORIGINS != '*' else '*')

# Create required directories
Path(UPLOAD_FOLDER).mkdir(exist_ok=True)
Path(OUTPUT_FOLDER).mkdir(exist_ok=True)

# Configure app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Initialize agent
agent = ExcelIngestionAgent(output_dir=OUTPUT_FOLDER)


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    """Serve the upload page."""
    with open('upload.html', 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'service': 'Excel Ingestion Agent'}), 200


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Upload and process Excel file.
    
    Returns:
        JSON response with processed test cases
    """
    # Check if file is in request
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file provided'}), 400
    
    file = request.files['file']
    
    # Check if file is empty
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No file selected'}), 400
    
    # Check if file is allowed
    if not allowed_file(file.filename):
        return jsonify({
            'status': 'error',
            'message': f'File type not allowed. Allowed types: {", ".join(ALLOWED_EXTENSIONS)}'
        }), 400
    
    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Process file
        result = agent.process_file(file_path)
        
        # Return result with appropriate status code
        status_code = 200 if result['status'] == 'success' else 400
        return jsonify(result), status_code
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Server error: {str(e)}'
        }), 500


@app.route('/process', methods=['POST'])
def process_file():
    """
    Process an already uploaded file by path.
    
    Request JSON:
        {
            "file_path": "/path/to/file.xlsx"
        }
    """
    data = request.get_json()
    
    if not data or 'file_path' not in data:
        return jsonify({'status': 'error', 'message': 'file_path required'}), 400
    
    file_path = data['file_path']
    
    # Validate file exists
    if not os.path.exists(file_path):
        return jsonify({'status': 'error', 'message': 'File not found'}), 404
    
    try:
        result = agent.process_file(file_path)
        status_code = 200 if result['status'] == 'success' else 400
        return jsonify(result), status_code
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Server error: {str(e)}'
        }), 500


@app.route('/template', methods=['GET'])
def get_template():
    """Return a sample Excel template structure."""
    template = {
        'columns': [
            'id',
            'title',
            'description',
            'preconditions',
            'steps',
            'expected_result',
            'priority',
            'status',
            'tags',
            'module'
        ],
        'example_row': {
            'id': 'TC-001',
            'title': 'Login with valid credentials',
            'description': 'Verify user can login with valid username and password',
            'preconditions': 'User account exists, browser is open',
            'steps': 'Open login page | Login page displays\nEnter username | Username field populated\nEnter password | Password field populated\nClick login | Dashboard displays',
            'expected_result': 'User is logged in successfully',
            'priority': 'high',
            'status': 'active',
            'tags': 'authentication,login,smoke-test',
            'module': 'Auth'
        },
        'notes': [
            'Use pipe (|) to separate action and expected result in steps',
            'Separate multiple steps with newline characters',
            'Valid priorities: critical, high, medium, low',
            'Valid statuses: active, deprecated, draft'
        ]
    }
    return jsonify(template), 200


@app.route('/info', methods=['GET'])
def get_info():
    """Get information about the agent."""
    return jsonify({
        'name': 'Excel Ingestion Agent',
        'version': '1.0.0',
        'description': 'Parse Excel files and normalize test cases into canonical JSON format',
        'endpoints': {
            'POST /upload': 'Upload and process Excel file',
            'POST /process': 'Process a file by path',
            'GET /template': 'Get Excel template structure',
            'GET /health': 'Health check',
            'GET /info': 'Agent information'
        }
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'status': 'error', 'message': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'status': 'error', 'message': 'Internal server error'}), 500


if __name__ == '__main__':
    # Run in production mode to avoid debug/reload issues
    app.run(debug=DEBUG, host=HOST, port=PORT, use_reloader=False)
