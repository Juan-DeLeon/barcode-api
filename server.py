from io import BytesIO
from barcode import Code128, Code39
from barcode.writer import ImageWriter
import base64
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def generate_barcode():
    event = request.json
    # provider can be defined for barcode
    # if not defined will default to code128
    provider = event.get('provider', 'code128')

    # render options (for sizes, see python barcode docs)
    # https://python-barcode.readthedocs.io/en/stable/writers.html
    # defaults to None
    options = event.get('options', None)

    try:
        code = event['code']
    except:
        return {
            'statusCode': 400,
            'body': 'event.code no puede estar vacio'
        }, 400

    rv = BytesIO()

    if provider == 'code128':
        codex = Code128(code, writer=ImageWriter())
    elif provider == 'code39':
        codex = Code39(code, writer=ImageWriter())

    codex.write(rv, options)

    b64 = base64.b64encode(rv.getvalue()).decode('utf-8')

    return {
        'statusCode': 200,
        'body': b64
    }, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
