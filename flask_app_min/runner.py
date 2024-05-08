from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    currency = request.args.get('currency', '', type=str)
    flt = request.args.get('flt', '', type=str)
    pages = request.args.get('pages', 1, type=str)

    data = requests.get(
        f'https://brains.tradingeconomics.com/v2/search/wb?q={flt}{("&currency=" + currency) if currency else ""}'
        f'&pp={pages}&stance=1').json() if flt else None

    hits = 0
    head_list1, values_list1 = [], []
    head_list2, values_list2 = [], [[]]
    from_pages = (1, 5, 20, 100, 500)
    if data is not None:
        hits = data["info"]["hits"]["value"]
        head_list1 = ["type_info", "key", "doc_count"]
        for key in data["info"]["facets"].keys():
            for val in data["info"]["facets"][key]:
                values_list1.append([key, val["key"], val["doc_count"]]) if val else None

        head_list2 = data["hits"][0].keys() if data["hits"] else None
        values_list2 = [[d[k] for k in head_list2] for d in data["hits"]]

    return render_template('index.html',
                           head_list1=head_list1, values_list1=values_list1,
                           head_list2=head_list2, values_list2=values_list2,
                           currency=currency,
                           hits=hits,
                           pages=pages,
                           from_pages=from_pages,
                           flt=flt, view='index')


if __name__ == '__main__':
    # app.run(host='localhost', port=8000, debug=True)
    app.run(host='localhost', port=8000, debug=True)
