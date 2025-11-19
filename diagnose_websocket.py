#!/usr/bin/env python3
"""
WebSocket Connection Diagnostic Tool
Run this to identify why WebSocket connections are failing
"""

import sys
import asyncio
import json

def check_imports():
    """Check if required packages are installed"""
    print("=" * 60)
    print("1. CHECKING PYTHON PACKAGES")
    print("=" * 60)

    packages = {
        'fastapi': 'FastAPI',
        'uvicorn': 'Uvicorn',
        'websockets': 'WebSockets client',
        'anthropic': 'Anthropic API'
    }

    missing = []
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✅ {name} installed")
        except ImportError:
            print(f"❌ {name} NOT installed")
            missing.append(package)

    if missing:
        print(f"\n⚠️  Install missing packages:")
        print(f"   pip install {' '.join(missing)}")
        return False
    return True


def check_backend_code():
    """Check if backend has WebSocket endpoint"""
    print("\n" + "=" * 60)
    print("2. CHECKING BACKEND CODE")
    print("=" * 60)

    try:
        with open('main.py', 'r') as f:
            content = f.read()

        # Check for WebSocket endpoint
        if '@app.websocket("/ws")' in content or '@app.websocket(\'/ws\')' in content:
            print("✅ WebSocket endpoint found in main.py")
        else:
            print("❌ WebSocket endpoint NOT found in main.py")
            print("   Missing: @app.websocket('/ws')")
            return False

        # Check for CORS
        if 'CORSMiddleware' in content:
            print("✅ CORS middleware configured")
        else:
            print("⚠️  CORS middleware not found")

        # Check ports in CORS
        if 'localhost:3000' in content:
            print("✅ Port 3000 allowed in CORS")
        else:
            print("⚠️  Port 3000 not in CORS allow_origins")

        if 'localhost:5173' in content:
            print("✅ Port 5173 allowed in CORS")
        else:
            print("⚠️  Port 5173 not in CORS allow_origins")

        return True

    except FileNotFoundError:
        print("❌ main.py not found in current directory")
        print(f"   Current directory: {os.getcwd()}")
        return False


def check_port_availability():
    """Check if port 8000 is in use"""
    print("\n" + "=" * 60)
    print("3. CHECKING PORT AVAILABILITY")
    print("=" * 60)

    import socket

    def is_port_in_use(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0

    if is_port_in_use(8000):
        print("✅ Port 8000 is IN USE (backend likely running)")
    else:
        print("❌ Port 8000 is FREE (backend NOT running)")
        return False

    if is_port_in_use(3000):
        print("✅ Port 3000 is IN USE (frontend likely running)")
    elif is_port_in_use(5173):
        print("✅ Port 5173 is IN USE (frontend likely running on Vite default)")
    else:
        print("⚠️  Neither port 3000 nor 5173 in use (frontend might not be running)")

    return True


async def test_websocket_connection():
    """Test actual WebSocket connection"""
    print("\n" + "=" * 60)
    print("4. TESTING WEBSOCKET CONNECTION")
    print("=" * 60)

    try:
        import websockets

        print("Attempting connection to ws://localhost:8000/ws...")

        async with websockets.connect('ws://localhost:8000/ws', timeout=5) as ws:
            print("✅ WebSocket connection SUCCESSFUL!")

            # Try sending a test message
            test_msg = json.dumps({"type": "ping"})
            await ws.send(test_msg)
            print("✅ Sent test message")

            # Try receiving (with timeout)
            try:
                response = await asyncio.wait_for(ws.recv(), timeout=2)
                print(f"✅ Received response: {response[:100]}...")
            except asyncio.TimeoutError:
                print("⚠️  No response (this is OK if backend doesn't respond to ping)")

            return True

    except Exception as e:
        print(f"❌ WebSocket connection FAILED!")
        print(f"   Error: {type(e).__name__}: {str(e)}")

        if "Connection refused" in str(e):
            print("\n   ROOT CAUSE: Backend is not running on port 8000")
            print("   Fix: Start backend with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload")

        elif "Invalid status code" in str(e):
            print("\n   ROOT CAUSE: Server returned non-101 status (not upgrading to WebSocket)")
            print("   Fix: Check that @app.websocket('/ws') endpoint exists in main.py")

        elif "timeout" in str(e).lower():
            print("\n   ROOT CAUSE: Connection timeout")
            print("   Fix: Check firewall or if backend is listening on 0.0.0.0 (not just 127.0.0.1)")

        return False


def check_http_endpoint():
    """Test HTTP endpoints"""
    print("\n" + "=" * 60)
    print("5. TESTING HTTP ENDPOINTS")
    print("=" * 60)

    import urllib.request
    import urllib.error

    endpoints = [
        ('/', 'Root'),
        ('/health', 'Health check'),
    ]

    for path, name in endpoints:
        try:
            with urllib.request.urlopen(f'http://localhost:8000{path}', timeout=5) as response:
                data = response.read().decode()
                print(f"✅ {name}: {data[:100]}")
        except urllib.error.URLError as e:
            print(f"❌ {name}: {e}")
        except Exception as e:
            print(f"❌ {name}: {e}")


def main():
    """Run all diagnostics"""
    import os

    print("\n")
    print("🔍" * 30)
    print("WEBSOCKET CONNECTION DIAGNOSTIC TOOL")
    print("🔍" * 30)
    print()

    # Change to backend directory if needed
    if os.path.exists('backend/main.py'):
        print(f"📁 Changing to backend directory...")
        os.chdir('backend')

    print(f"📁 Working directory: {os.getcwd()}")
    print()

    # Run checks
    results = []

    results.append(("Packages", check_imports()))
    results.append(("Backend Code", check_backend_code()))
    results.append(("Port Availability", check_port_availability()))

    # HTTP endpoints check
    check_http_endpoint()

    # WebSocket test (async)
    try:
        ws_result = asyncio.run(test_websocket_connection())
        results.append(("WebSocket Connection", ws_result))
    except Exception as e:
        print(f"❌ WebSocket test failed: {e}")
        results.append(("WebSocket Connection", False))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for check, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {check}")

    all_passed = all(result for _, result in results)

    if all_passed:
        print("\n🎉 All checks passed! WebSocket should work.")
    else:
        print("\n⚠️  Some checks failed. See errors above for fixes.")
        print("\nQUICK FIX:")
        print("1. Make sure you're in the backend directory")
        print("2. Run: uvicorn main:app --host 0.0.0.0 --port 8000 --reload")
        print("3. Run this diagnostic again")

    return 0 if all_passed else 1


if __name__ == '__main__':
    sys.exit(main())
