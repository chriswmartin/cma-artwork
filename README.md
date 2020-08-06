# CMA Artwork

![screenshot](screenshot.png)

This project extracts information associated with works of art from a 5-table SQLite database into JSON and then uses this data to populate a web page. Each artwork on the web page can be clicked on to view additional information. 

# Running

This project requires [python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/). Once those are installed you can run the project with the following.

```bash
> git clone https://github.com/chriswmartin/cma-artwork.git

> cd cma-artwork

> pip3 install -r requirements.txt

> python3 main.py
```

This will start a local web server with the web page running at [http://127.0.0.1:5000](http://127.0.0.1:5000).
