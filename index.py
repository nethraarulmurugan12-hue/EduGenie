<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduGenie - AI Learning Assistant</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f7f6;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            width: 100%;
            max-width: 600px;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 20px;
        }
        textarea {
            width: 100%;
            height: 120px;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
            resize: vertical;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
        .result-box {
            margin-top: 25px;
            padding: 20px;
            background-color: #e8f8f5;
            border-left: 5px solid #1abc9c;
            border-radius: 5px;
        }
        .result-box h3 {
            margin-top: 0;
            color: #16a085;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>EduGenie AI Assistant</h1>
        
        <!-- Form submission sends POST request to FastAPI backend -->
        <form action="/" method="POST">
            <label for="user_input">Enter your question or topic:</label>
            <textarea name="user_input" id="user_input" placeholder="Type something here...">{{ user_input if user_input else '' }}</textarea>
            <button type="submit">Ask Gemini</button>
        </form>

        <!-- Result appears below input box in real-time -->
        {% if result %}
            <div class="result-box">
                <h3>Gemini Response:</h3>
                <p>{{ result }}</p>
            </div>
        {% endif %}
    </div>

</body>
</html>
