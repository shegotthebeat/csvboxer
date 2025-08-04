
import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        script = request.form.get('script')

        if script == 'sanitize_headers':
            from processors.csv_sanitizer import CSVSanitizer
            sanitizer = CSVSanitizer()
            processed_filepath = sanitizer.process(filepath)
            return send_file(processed_filepath, as_attachment=True)

        elif script == 'calculate_stats':
            from processors.csv_stats_calculator import CSVStatsCalculator
            calculator = CSVStatsCalculator()
            stats = calculator.process(filepath)
            return render_template('results.html', stats=stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
