
# Adobe Hackathon Round 1A - PDF Outline Extractor

## 🧠 Approach
This is a simple simulated solution that reads PDF filenames and outputs a predefined outline structure as JSON.
In real-world usage, you'd replace the placeholder with a robust PDF parser like PyMuPDF or pdfplumber.

## 🐳 Docker Instructions

### Build the image:
```bash
docker build --platform linux/amd64 -t pdfoutline:123abc .
```

### Run the container:
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdfoutline:123abc
```

## 🗂 Output Format

```json
{
  "title": "Sample Document",
  "outline": [
    {"level": "H1", "text": "Introduction", "page": 1},
    {"level": "H2", "text": "Background", "page": 2},
    {"level": "H3", "text": "Early History", "page": 3},
    {"level": "H1", "text": "Conclusion", "page": 5}
  ]
}
```
