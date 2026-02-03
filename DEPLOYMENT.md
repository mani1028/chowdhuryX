# ChowdhuryX - Production Deployment Guide

## Prerequisites
- Python 3.8+
- Gunicorn WSGI server
- Nginx (reverse proxy)
- SSL certificate

## Installation & Setup

### 1. Clone & Install Dependencies
```bash
git clone <repo-url>
cd chowdhuryx
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment
Edit `.env` with production values:
```
FLASK_ENV=production
SECRET_KEY=<generate-with-python-secrets>
DATABASE_URL=sqlite:///instance/chowdhuryX.db
MAIL_SERVER=<your-smtp-server>
MAIL_USERNAME=<your-email>
MAIL_PASSWORD=<your-app-password>
```

### 3. Initialize Database
```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### 4. Create Admin User
```bash
python create_admin.py
# Follow prompts to create admin account
```

## Deployment with Gunicorn

### Install Gunicorn
```bash
pip install gunicorn
```

### Start Application
```bash
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

### Systemd Service (Linux)
Create `/etc/systemd/system/chowdhuryx.service`:
```ini
[Unit]
Description=ChowdhuryX Flask Application
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/chowdhuryx
Environment="PATH=/path/to/chowdhuryx/venv/bin"
Environment="FLASK_ENV=production"
ExecStart=/path/to/chowdhuryx/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 wsgi:app

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable chowdhuryx
sudo systemctl start chowdhuryx
```

## Nginx Configuration

Create `/etc/nginx/sites-available/chowdhuryx`:
```nginx
upstream chowdhuryx {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    client_max_body_size 16M;

    location / {
        proxy_pass http://chowdhuryx;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/chowdhuryx/static/;
        expires 30d;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/chowdhuryx /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## SSL Certificate (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d yourdomain.com -d www.yourdomain.com
```

## Maintenance

### Backup Database
```bash
cp instance/chowdhuryX.db instance/chowdhuryX.db.backup
```

### View Logs
```bash
journalctl -u chowdhuryx -f
```

### Database Cleanup (Monthly)
```bash
python
>>> from app import create_app, db
>>> from models import Analytics
>>> app = create_app()
>>> with app.app_context():
...     old_analytics = Analytics.query.filter(Analytics.created_at < '2024-01-01').delete()
...     db.session.commit()
```

## Security Checklist

- [ ] Change SECRET_KEY to random string (256+ bits)
- [ ] Set strong database credentials
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall rules
- [ ] Set up fail2ban for brute-force protection
- [ ] Enable CSRF protection (enabled by default)
- [ ] Set secure session cookies
- [ ] Regular database backups
- [ ] Monitor error logs
- [ ] Keep dependencies updated

## Performance Optimization

1. Enable gzip compression in Nginx
2. Set cache headers for static files
3. Use CDN for static assets
4. Implement database query optimization
5. Monitor application performance

## Troubleshooting

**Port already in use:**
```bash
lsof -i :8000  # Find process
kill -9 <PID>  # Kill process
```

**Database locked:**
```bash
rm instance/chowdhuryX.db-journal
```

**Memory issues:**
```bash
gunicorn -w 2 -b 127.0.0.1:8000 wsgi:app  # Reduce workers
```

## Support
For issues, check logs and error messages. Contact support@chowdhuryx.com
