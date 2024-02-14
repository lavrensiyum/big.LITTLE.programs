from flask import Flask

import hu_yemek

app = Flask(__name__)

@app.route('/v2/hacettepe_yemek/get_data/', methods=['GET'])
def yemek():

    yemek = hu_yemek.bugunun_yemekleri()
    return yemek

if __name__ == '__main__':
    app.run(host='79.110.234.6', port=7000)