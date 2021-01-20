{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "app.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPNO0exaKoC2gcXt4KDMZTZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Satyam1103/Spam-Email-Detection/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "97y9pZS8zab1"
      },
      "source": [
        "from flask import Flask,render_template,url_for,request\r\n",
        "import pandas as pd \r\n",
        "from sklearn.feature_extraction.text import CountVectorizer\r\n",
        "from sklearn.naive_bayes import MultinomialNB\r\n",
        "from nltk.tokenize import RegexpTokenizer, word_tokenize\r\n",
        "from nltk.stem import PorterStemmer"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9xqd7hQ45bI3",
        "outputId": "114581d8-3d9d-4b97-e541-4dff6426a60e"
      },
      "source": [
        "!pip install pickle5"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting pickle5\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/f7/4c/5c4dd0462c8d3a6bc4af500a6af240763c2ebd1efdc736fc2c946d44b70a/pickle5-0.0.11.tar.gz (132kB)\n",
            "\r\u001b[K     |██▌                             | 10kB 14.9MB/s eta 0:00:01\r\u001b[K     |█████                           | 20kB 10.8MB/s eta 0:00:01\r\u001b[K     |███████▍                        | 30kB 9.1MB/s eta 0:00:01\r\u001b[K     |██████████                      | 40kB 7.2MB/s eta 0:00:01\r\u001b[K     |████████████▍                   | 51kB 3.9MB/s eta 0:00:01\r\u001b[K     |██████████████▉                 | 61kB 4.4MB/s eta 0:00:01\r\u001b[K     |█████████████████▍              | 71kB 4.7MB/s eta 0:00:01\r\u001b[K     |███████████████████▉            | 81kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████████████████▎         | 92kB 5.2MB/s eta 0:00:01\r\u001b[K     |████████████████████████▉       | 102kB 5.5MB/s eta 0:00:01\r\u001b[K     |███████████████████████████▎    | 112kB 5.5MB/s eta 0:00:01\r\u001b[K     |█████████████████████████████▊  | 122kB 5.5MB/s eta 0:00:01\r\u001b[K     |████████████████████████████████| 133kB 5.5MB/s \n",
            "\u001b[?25hBuilding wheels for collected packages: pickle5\n",
            "  Building wheel for pickle5 (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pickle5: filename=pickle5-0.0.11-cp36-cp36m-linux_x86_64.whl size=218617 sha256=c791fac7c12f024bddecab4f7771cca197babc211e49dba8b150eac849e86d8d\n",
            "  Stored in directory: /root/.cache/pip/wheels/a6/90/95/f889ca4aa8b0e0c7f21c8470b6f5d6032f0390a3a141a9a3bd\n",
            "Successfully built pickle5\n",
            "Installing collected packages: pickle5\n",
            "Successfully installed pickle5-0.0.11\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "31mpcz1T5l9F"
      },
      "source": [
        "import pickle5 as pickle"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "txDG6Jc20ONY",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 459
        },
        "outputId": "76226686-fdaf-40ff-bff2-2b6759a9b9bf"
      },
      "source": [
        "# load the model from disk\r\n",
        "filename = 'nlp_model.pkl'\r\n",
        "clf = pickle.load(open(filename, 'rb'))\r\n",
        "cv=pickle.load(open('tranform.pkl','rb'))\r\n",
        "app = Flask(__name__)\r\n",
        "\r\n",
        "@app.route('/')\r\n",
        "def home():\r\n",
        "\treturn render_template('home.html')\r\n",
        "\r\n",
        "@app.route('/predict',methods=['POST'])\r\n",
        "def predict():\r\n",
        "      \r\n",
        "\tif request.method == 'POST':\r\n",
        "\t\tmessage = request.form['message']\r\n",
        "\t\tdata = [message]\r\n",
        "\t\tvect = cv.transform(data).toarray()\r\n",
        "\t\tmy_prediction = clf.predict(vect)\r\n",
        "\treturn render_template('result.html',prediction = my_prediction)\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "if __name__ == '__main__':\r\n",
        "\tapp.run(debug=True)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " * Serving Flask app \"__main__\" (lazy loading)\n",
            " * Environment: production\n",
            "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
            "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
            " * Debug mode: on\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "OSError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mOSError\u001b[0m                                   Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-9-8be555a2b37c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     23\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'__main__'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 24\u001b[0;31m         \u001b[0mapp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/flask/app.py\u001b[0m in \u001b[0;36mrun\u001b[0;34m(self, host, port, debug, load_dotenv, **options)\u001b[0m\n\u001b[1;32m    988\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    989\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 990\u001b[0;31m             \u001b[0mrun_simple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhost\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mport\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    991\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    992\u001b[0m             \u001b[0;31m# reset the first request information if the development server\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/werkzeug/serving.py\u001b[0m in \u001b[0;36mrun_simple\u001b[0;34m(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)\u001b[0m\n\u001b[1;32m   1028\u001b[0m             \u001b[0ms\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maddress_family\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSOCK_STREAM\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1029\u001b[0m             \u001b[0ms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msetsockopt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSOL_SOCKET\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mSO_REUSEADDR\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1030\u001b[0;31m             \u001b[0ms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mserver_address\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1031\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"set_inheritable\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1032\u001b[0m                 \u001b[0ms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_inheritable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mOSError\u001b[0m: [Errno 98] Address already in use"
          ]
        }
      ]
    }
  ]
}