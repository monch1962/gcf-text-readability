from flask import Flask, request, jsonify, abort, make_response
from werkzeug.exceptions import HTTPException
import json

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_bad_request(e):
    return jsonify({"error": "Bad request! You need to POST JSON with a single 'text' field containing the text to check to the /evaluate_text endpoint"}), 400

@app.route('/evaluate_text', methods=['POST'])
def evaluate_text(request):
    #print('request: %s' % request.data)
    try:
        text = request.get_json()['text']
        #text = str(request.get_data())
        print('text: %s' % text)
    except KeyError:
        abort(400)
    readability = evaluate_readability(text)
    print(readability)
    (errors_found, corrected_text) = check_for_errors(str(text), 'en-AU')
    if corrected_text != text:
        resp = make_response(jsonify({'corrected_text': corrected_text}))
    else:
        resp = make_response('')
    resp.headers['readability'] = str(readability)
    resp.headers['errors_found'] = str(errors_found)
    return(resp)
    #return jsonify({'original_text': text, 'readability': readability, 'errors_found': errors_found, 'corrected_text': corrected_text})

def evaluate_readability(text):
    import textstat
    return textstat.text_standard(str(text), float_output=True)

def check_for_errors(text, language='en-AU'):
    import language_tool_python
    text_check = language_tool_python.LanguageToolPublicAPI(language)
    corrected_text = text_check.correct(text)
    errs = text_check.check(text)
    errors_found = []
    for i in errs:
        errors_found.append(json.dumps(str(i)))
    return (errors_found, corrected_text)

if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)