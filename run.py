#!/usr/bin/env python3

from app import create_app, socketio

def run_app():
    """Run the Flask application - simplified version"""
    try:
        app = create_app()
        
        print("=" * 50)
        print("🚀 EXAM SYSTEM STARTING")
        print("🔧 DEBUGGING MODE: ENABLED")
        print("🔧 F12 ACCESS: ALLOWED")
        print("=" * 50)
        
        # Simple HTTP server without SSL complications
        ports_to_try = [5001, 5002, 5003, 5000]
        
        for port in ports_to_try:
            try:
                print(f"🌐 Starting on http://127.0.0.1:{port}")
                socketio.run(app,
                           host='127.0.0.1',
                           port=port,
                           debug=True,
                           use_reloader=False)  # Simple HTTP, no SSL
                break
            except OSError as e:
                if "Only one usage of each socket address" in str(e):
                    print(f"❌ Port {port} is busy, trying next port...")
                    continue
                else:
                    raise
        else:
            print("❌ All ports are busy!")
            
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    run_app() 