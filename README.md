# Digit Recognition Web App

This is a simple **handwritten digit recognition web application** built using **Flask**, **TensorFlow**, and **JavaScript**. The application allows users to draw a digit on a canvas, then predicts which number it is using a pre-trained model.

## Features

- Draw digits on a canvas
- Predict digits using a pre-trained TensorFlow model
- Interactive web interface using HTML, CSS, and JavaScript
- Lightweight and easy to deploy

## Project Structure

```
digit-recognition-app/          <- GitHub repo root
│
├── app.py                     <- Flask backend application
├── model.keras                <- Trained TensorFlow model
├── requirements.txt           <- Python dependencies
├── Procfile                   <- Command to run the app on Render/Heroku
├── .gitignore                 <- Files to ignore in Git
│
├── templates/                 <- HTML templates
│    └── index.html            <- Main frontend page
│
└── static/                    <- Static files (JS, CSS)
     ├── script.js             <- Handles canvas drawing and API calls
     └── style.css             <- Styling for the frontend
```

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/prayagadage/digit-recognition-app.git
   cd digit-recognition-app
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app locally:**

   ```bash
   python app.py
   ```

5. **Open your browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```

## Deployment

### Using Render:

1. Go to [Render](https://render.com) and create a new Web Service.
2. Connect your GitHub repo (`digit-recognition-app`).
3. If your project is inside a subfolder (like `Handwriting_Recognition`), set the **Root Directory** accordingly. Otherwise, keep it blank.
4. Set the **Build Command**:

   ```
   pip install -r requirements.txt
   ```

5. Set the **Start Command**:

   ```
   gunicorn app:app
   ```

6. Deploy and get the public URL.
7. Update `script.js` in your frontend to call the deployed backend API:

   ```javascript
   fetch("https://your-deployed-backend-url/predict", {
       method: "POST",
       headers: { "Content-Type": "application/json" },
       body: JSON.stringify({ image: image })
   })
   ```

### Using GitHub Pages for frontend (optional):

- You can host `index.html` and static files on GitHub Pages and connect it to the Render backend.

## Notes

- Keep your `model.keras` in the project folder for Render to access it.
- Make sure `.gitignore` does not exclude essential files like `requirements.txt`, `Procfile`, or the model.
- The app is built for simplicity and learning purposes.

## License

MIT License
