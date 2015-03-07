# DownBooru ![](https://img.shields.io/badge/Python-3.4-blue.svg?style=flat-square)
###### Formerly known as GelDown

Simple Imageboard CLI Downloader.

**Supported imageboards**:
* Danbooru
* Gelbooru
* Safebooru
* Rule34
* Yande.re
* Konachan

**Usage**

Tags: Tags can be as simple as character name (e.g. misaka_mikoto, uzumaki_naruto) or by adding extra tag (e.g. shana short_hair)

```python
Enter tags: misaka_mikoto short_hair
```

Limit: Enter how much limit of images to download

```python
Enter limit: 5
```

Booru: Enter imageboard you prefer to use (default is Danbooru)

```python
Enter booru: Konachan
```

For now the default save location is at `~/Images`, will add support to choose other directory easily.

Or you can manually edit the location path by opening `main.py` and edit

```python
makefile("/home/%s/Images" % getpass.getuser())
```
to your desired path.

**Dependencies**:
* BeautifulSoup4
