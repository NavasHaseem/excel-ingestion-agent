#!/bin/bash
# AWS EC2 Deployment Script for Excel Ingestion Agent

set -e

echo "=========================================="
echo "Excel Ingestion Agent - EC2 Setup"
echo "=========================================="

# Update system
echo "Updating system packages..."
sudo yum update -y

# Install Python and dependencies
echo "Installing Python 3.9+..."
sudo yum install -y python3 python3-pip python3-venv git

# Clone or setup repository
echo "Setting up application directory..."
AGENT_DIR="/opt/excel-ingestion-agent"
sudo mkdir -p $AGENT_DIR
cd $AGENT_DIR

# If deploying from git
# sudo git clone <your-repo-url> .

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
mkdir -p uploads output logs

# Set permissions
sudo chown -R ec2-user:ec2-user $AGENT_DIR

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Update config.py with your settings"
echo "2. Run: source /opt/excel-ingestion-agent/venv/bin/activate"
echo "3. Run: python app.py"
echo ""
echo "Or use systemd service:"
echo "4. sudo cp excel-agent.service /etc/systemd/system/"
echo "5. sudo systemctl daemon-reload"
echo "6. sudo systemctl start excel-agent"
echo "7. sudo systemctl enable excel-agent"
