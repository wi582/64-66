# Claude Monet — restaurant website (Flask)

Local run:    pip install -r requirements.txt && python app.py   (http://localhost:5000)
Tests:        pytest
Docker:       docker build -t claude-monet . && docker run -p 5000:5000 claude-monet
Git / CI:     git init && git add . && git commit -m "Initial" && git branch -M main
              git remote add origin https://github.com/<user>/claude-monet.git && git push -u origin main
