# Excel Ingestion Agent - AWS EC2 Deployment Guide

## Prerequisites

- AWS EC2 instance (Amazon Linux 2 or Ubuntu recommended)
- SSH access to the instance
- Security Group configured to allow inbound traffic on port 5000

## Step 1: Launch EC2 Instance

1. Go to AWS EC2 Dashboard
2. Launch new instance:
   - AMI: Amazon Linux 2 or Ubuntu 20.04 LTS
   - Instance type: t2.micro (free tier eligible) or larger
   - Security Group: Allow inbound:
     - Port 5000 (TCP) from your IP or 0.0.0.0/0
     - Port 22 (SSH) for administration

## Step 2: Connect to EC2 Instance

```bash
# Download your .pem key file and run:
chmod 400 your-key.pem
ssh -i your-key.pem ec2-user@your-instance-ip
# Or for Ubuntu:
ssh -i your-key.pem ubuntu@your-instance-ip
```

## Step 3: Deploy the Agent

### Option A: Using Provided Setup Script (Amazon Linux 2)

```bash
# Download and run the setup script
curl -O https://your-repo-url/ec2-setup.sh
chmod +x ec2-setup.sh
./ec2-setup.sh
```

### Option B: Manual Setup

```bash
# Update system
sudo yum update -y  # For Amazon Linux 2
# sudo apt update && sudo apt upgrade -y  # For Ubuntu

# Install Python and dependencies
sudo yum install -y python3 python3-pip python3-venv
# sudo apt install -y python3 python3-pip python3-venv  # For Ubuntu

# Create application directory
sudo mkdir -p /opt/excel-ingestion-agent
cd /opt/excel-ingestion-agent

# Copy your project files here (via SCP or Git clone)
# Example using git:
sudo git clone <your-repo-url> .

# Create virtual environment
sudo python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create required directories
sudo mkdir -p uploads output logs
sudo chown -R ec2-user:ec2-user /opt/excel-ingestion-agent
```

## Step 4: Configure Environment Variables

Create `.env` file in `/opt/excel-ingestion-agent/`:

```bash
# .env file
DEBUG=False
HOST=0.0.0.0
PORT=5000
UPLOAD_FOLDER=uploads
OUTPUT_FOLDER=output
MAX_FILE_SIZE=52428800
CORS_ORIGINS=*
```

## Step 5: Run the Agent

### Option A: Direct Execution

```bash
cd /opt/excel-ingestion-agent
source venv/bin/activate
python app.py
```

The server will start on: `http://your-instance-ip:5000`

### Option B: Using Systemd Service (Recommended for Production)

```bash
# Copy service file
sudo cp excel-agent.service /etc/systemd/system/

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl start excel-agent
sudo systemctl enable excel-agent  # Auto-start on reboot

# Check status
sudo systemctl status excel-agent

# View logs
sudo journalctl -u excel-agent -f
```

## Step 6: Configure Local UI

Update your local HTML/UI to point to the EC2 instance:

```javascript
// In your upload.html or UI code:
const API_ENDPOINT = 'http://your-ec2-instance-ip:5000';

// Replace the fetch URL:
const response = await fetch(`${API_ENDPOINT}/upload`, {
    method: 'POST',
    body: formData
});
```

Or set it dynamically:
```javascript
const API_ENDPOINT = localStorage.getItem('api_endpoint') || 'http://localhost:5000';
```

## Step 7: Access the Agent

**From Local Machine:**
```
http://your-ec2-instance-public-ip:5000/
```

**API Endpoints:**
- `GET /health` - Health check
- `GET /` - Web UI
- `POST /upload` - Upload and process Excel file
- `GET /template` - Get template structure
- `GET /info` - Agent information

## Troubleshooting

### Port 5000 not accessible
```bash
# Check if Flask is running
sudo systemctl status excel-agent

# Check security group allows port 5000
# Check EC2 security group rules in AWS console
```

### Import errors
```bash
# Ensure venv is activated
source /opt/excel-ingestion-agent/venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Permission issues
```bash
# Fix ownership
sudo chown -R ec2-user:ec2-user /opt/excel-ingestion-agent
sudo chmod -R 755 /opt/excel-ingestion-agent
```

## Performance Tips

1. **Use t2.medium or larger** for better performance with large files
2. **Enable auto-scaling** if processing many files
3. **Use Elastic IP** to keep the same IP address
4. **Add CloudWatch monitoring** for logs and metrics
5. **Consider using Nginx as reverse proxy** for production

## Security Best Practices

1. **Restrict port 5000** to your IP range in Security Group
2. **Use HTTPS** with SSL certificate (use Nginx with Let's Encrypt)
3. **Set proper `CORS_ORIGINS`** instead of `*`
4. **Monitor CloudWatch logs** for suspicious activity
5. **Use IAM roles** for S3 access if needed

## Production Deployment

For production, consider:
1. Using Gunicorn or uWSGI instead of Flask development server
2. Setting up Nginx as reverse proxy
3. Using RDS for database if adding persistence
4. Enabling CloudWatch alarms
5. Using CodeDeploy for automated updates

## Stopping/Restarting the Service

```bash
# Stop
sudo systemctl stop excel-agent

# Restart
sudo systemctl restart excel-agent

# View logs
sudo journalctl -u excel-agent -n 50  # Last 50 lines
```
