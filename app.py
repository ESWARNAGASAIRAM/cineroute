from flask import Flask, render_template

app = Flask(__name__)

movies = {

    "Kalki 2898 AD": {
        "ott": "Prime Video",
        "image": "kalki.jpg",
        "link": "https://www.primevideo.com"
    },

    "Pushpa": {
        "ott": "Prime Video",
        "image": "pushpa.jpg",
        "link": "https://www.primevideo.com"
    },

    "Pushpa 2": {
        "ott": "Netflix",
        "image": "pushpa2.jpg",
        "link": "https://www.netflix.com"
    },

    "Salaar": {
        "ott": "Netflix",
        "image": "salaar.jpg",
        "link": "https://www.netflix.com"
    },

    "Dasara": {
        "ott": "Netflix",
        "image": "dasara.jpg",
        "link": "https://www.netflix.com"
    },

    "Lucky Baskhar": {
        "ott": "Netflix",
        "image": "luckybaskar.jpg",
        "link": "https://www.netflix.com"
    },

    "Guntur Kaaram": {
        "ott": "Netflix",
        "image": "gunturkaram.jpg",
        "link": "https://www.netflix.com"
    },

    "Hi Nanna": {
        "ott": "Netflix",
        "image": "hinanna.jpg",
        "link": "https://www.netflix.com"
    },

    "Major": {
        "ott": "Netflix",
        "image": "major.jpg",
        "link": "https://www.netflix.com"
    },

    "MAD": {
        "ott": "Netflix",
        "image": "mad.jpg",
        "link": "https://www.netflix.com"
    },

    "Virupaksha": {
        "ott": "Netflix",
        "image": "virupaksha.jpg",
        "link": "https://www.netflix.com"
    },

    "Sita Ramam": {
        "ott": "Prime Video",
        "image": "sitaramam.jpg",
        "link": "https://www.primevideo.com"
    },

    "Saripodhaa Sanivaaram": {
        "ott": "Netflix",
        "image": "saripodhaa.jpg",
        "link": "https://www.netflix.com"
    },

    "Tillu Square": {
        "ott": "Netflix",
        "image": "tillusquare.jpg",
        "link": "https://www.netflix.com"
    },

    "Khaleja": {
        "ott": "Prime Video",
        "image": "khaleja.jpg",
        "link": "https://www.primevideo.com"
    },

    "Eega": {
        "ott": "Prime Video",
        "image": "eega.jpg",
        "link": "https://www.primevideo.com"
    },

    "Devara": {
        "ott": "Netflix",
        "image": "devara.jpg",
        "link": "https://www.netflix.com"
    },

    "Arjun Reddy": {
        "ott": "Prime Video",
        "image": "arjunreddy.jpg",
        "link": "https://www.primevideo.com"
    },

    "Dear Comrade": {
        "ott": "Prime Video",
        "image": "dearcomrade.jpg",
        "link": "https://www.primevideo.com"
    },

    "Geetha Govindam": {
        "ott": "Prime Video",
        "image": "geethagovindham.jpg",
        "link": "https://www.primevideo.com"
    }
}


@app.route('/')
def home():
    return render_template('index.html', movies=movies)


if __name__ == '__main__':
    app.run(debug=True)