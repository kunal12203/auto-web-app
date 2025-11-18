"""
Test script to deploy a sample project and verify the deployment system works
"""

import asyncio
import sys
sys.path.append('/home/user/auto-web-app/backend')

from project_runner import project_runner

# Sample HTML project files
test_files = {
    'index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>🎉 Live Deployment Test</h1>
        <p>This is a real website running on a live server!</p>
        <div class="features">
            <div class="feature">
                <span class="icon">✅</span>
                <h3>Real Server</h3>
                <p>Running on Python HTTP server</p>
            </div>
            <div class="feature">
                <span class="icon">🚀</span>
                <h3>Auto Deployment</h3>
                <p>Files saved and served automatically</p>
            </div>
            <div class="feature">
                <span class="icon">🌐</span>
                <h3>Live URL</h3>
                <p>Access from your browser</p>
            </div>
        </div>
        <button onclick="testInteraction()">Click Me!</button>
        <div id="result"></div>
    </div>
    <script src="script.js"></script>
</body>
</html>''',

    'styles.css': '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.container {
    background: white;
    border-radius: 20px;
    padding: 60px;
    max-width: 800px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    text-align: center;
}

h1 {
    font-size: 48px;
    margin-bottom: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

p {
    font-size: 20px;
    color: #6b7280;
    margin-bottom: 40px;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 30px;
    margin: 40px 0;
}

.feature {
    padding: 30px;
    background: #f9fafb;
    border-radius: 15px;
    transition: transform 0.3s;
}

.feature:hover {
    transform: translateY(-5px);
}

.icon {
    font-size: 48px;
    display: block;
    margin-bottom: 15px;
}

.feature h3 {
    font-size: 20px;
    color: #1f2937;
    margin-bottom: 10px;
}

.feature p {
    font-size: 14px;
    color: #6b7280;
    margin: 0;
}

button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 15px 40px;
    font-size: 18px;
    border-radius: 10px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    margin-top: 20px;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}

#result {
    margin-top: 20px;
    font-size: 18px;
    color: #10b981;
    font-weight: bold;
    min-height: 30px;
}''',

    'script.js': '''function testInteraction() {
    const result = document.getElementById('result');
    const messages = [
        '✅ JavaScript is working!',
        '🎊 The website is fully functional!',
        '🚀 All assets loaded correctly!',
        '💯 Deployment successful!'
    ];
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    result.textContent = randomMessage;
    result.style.animation = 'fadeIn 0.5s';
}

// Add animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);

console.log('🎉 Test website loaded successfully!');
console.log('✅ All JavaScript is executing correctly!');'''
}

async def test_deployment():
    print("=" * 60)
    print("🧪 Testing Project Deployment System")
    print("=" * 60)

    try:
        # Deploy the test project
        print("\n📦 Deploying test project...")
        result = await project_runner.deploy_project(
            project_id="test-deployment-123",
            files=test_files,
            project_name="test-website"
        )

        if result['success']:
            print(f"\n✅ Deployment successful!")
            print(f"🌐 Live URL: {result['url']}")
            print(f"📂 Project Type: {result['type']}")
            print(f"🔌 Port: {result['port']}")
            print("\n" + "=" * 60)
            print("🎉 You can now access your website at:")
            print(f"   {result['url']}")
            print("=" * 60)
            print("\n💡 The server will keep running until you stop it")
            print("   Press Ctrl+C to stop the server")

            # Keep running
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                print("\n\n🛑 Stopping server...")
                await project_runner.stop_project("test-deployment-123")
                print("✅ Server stopped")
        else:
            print(f"\n❌ Deployment failed: {result.get('error')}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    asyncio.run(test_deployment())
