import requests
from lxml import html
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    return jsonify({
        'message': 'Welcome to CWPY!',
        'created_by': 'Juliano Mesquita',
        'created_at': '2018-03',
        'author': 'julianophp@gmail.com'
    })


@app.route('/cw', methods=['POST'])
def cw():

    output = ''
    path = request.json['path']
    session_requests = requests.session()

    for page_request in path:
        url = page_request['url']

        if page_request['method'] == 'GET':
            result = session_requests.get(url)

            if page_request['return'] == 'Y':
                output = result.content

            if len(page_request['get_inputs']) > 0:
                tree = html.fromstring(result.text.encode('utf-8', 'ignore'))

                for get_inputs in page_request['get_inputs']:
                    get_inputs['value'] = list(set(tree.xpath("//input[@name='" + get_inputs['name'] + "']/@value")))[0]

        elif page_request['method'] == 'POST':
            payload = page_request['inputs']

            for html_input in payload:
                if type(payload[html_input]) is dict:
                    filter_path  = [page for page in path if page['id'] == payload[html_input]['id_path']]
                    filter_input = [get_input for get_input in filter_path[0]['get_inputs'] if get_input['name'] == html_input]
                    payload[html_input] = filter_input[0]['value']

            result = session_requests.post(url, data = payload, headers = dict(referer = url))

            if page_request['return'] == 'Y':
                output = result.content

    return output


if __name__ == '__main__':
    app.run(debug=True, port=8081)