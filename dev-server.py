#!/usr/bin/env python3
"""
Night Watch: Outpost Zero - Local Development Server with Cloud Save Support.
Run: python dev-server.py 8080
"""
import http.server
import json
import os
import re
import sys
import random
from datetime import datetime

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
SAVE_DIR = os.path.join(os.path.dirname(__file__), 'saves')
os.makedirs(SAVE_DIR, exist_ok=True)

class OutpostHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/save.php'):
            self.handle_save_get()
            return
        super().do_GET()

    def do_POST(self):
        if self.path.startswith('/save.php'):
            self.handle_save_post()
            return
        self.send_response(404)
        self.end_headers()

    def handle_save_get(self):
        query = self.path.split('?', 1)[1] if '?' in self.path else ''
        params = dict(qc.split('=', 1) for qc in query.split('&') if '=' in qc)
        
        if 'new' in params:
            prefixes = ['ARTEMIS', 'ORION', 'APOLLO', 'EAGLE', 'VOYAGER', 'GATEWAY', 'POLARIS', 'TITAN', 'NOVA']
            cs = f"{random.choice(prefixes)}-{random.randint(100, 999)}"
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'callsign': cs}).encode('utf-8'))
            return

        callsign = params.get('id', '')
        callsign = re.sub(r'[^A-Za-z0-9_-]', '', callsign).upper()
        if not callsign:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': 'Invalid callsign'}).encode('utf-8'))
            return

        file_path = os.path.join(SAVE_DIR, f"{callsign}.json")
        if not os.path.exists(file_path):
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': 'Mission not found on server'}).encode('utf-8'))
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'ok': True, 'callsign': callsign, 'save': data}).encode('utf-8'))

    def handle_save_post(self):
        content_len = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(content_len).decode('utf-8')
        try:
            payload = json.loads(raw)
            callsign = re.sub(r'[^A-Za-z0-9_-]', '', payload.get('callsign', '')).upper()
            if not callsign:
                raise ValueError("Missing callsign")
            data = payload.get('data')
            if not data:
                raise ValueError("Missing data")
            
            file_path = os.path.join(SAVE_DIR, f"{callsign}.json")
            save_obj = {
                'v': 2,
                'callsign': callsign,
                'updated_at': datetime.utcnow().isoformat() + 'Z',
                'S': data
            }
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(save_obj, f, indent=2)

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'callsign': callsign, 'saved_at': save_obj['updated_at']}).encode('utf-8'))
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': str(e)}).encode('utf-8'))

if __name__ == '__main__':
    print(f"Starting Outpost Zero Dev Server at http://localhost:{PORT}")
    print(f"Cloud Save directory: {SAVE_DIR}")
    server = http.server.HTTPServer(('0.0.0.0', PORT), OutpostHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
