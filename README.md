# Flask local server

This is a Flask-based local server for serving builds generated from Unity models.

Add the model files inside the models folder:

```
-models:
    -model-name:
        -Build:
            build files from the Unity model
```

To run the server use: `python3 app.py`