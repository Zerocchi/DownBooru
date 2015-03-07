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

```python
python main.py <tags> <limit> <booru>
```

Argument  | Description
------------- | -------------
| Tags  | Tags can be as simple as character name (e.g. misaka_mikoto, uzumaki_naruto) or by adding extra tag wrapped in quotation mark (e.g. "shana short_hair"). |
| Limit | Enter how much limit of images to download. |
| Booru | Enter imageboard you prefer to use. Refer to [list of supported keywords](https://github.com/Zerocchi/DownBooru/blob/master/docs/supported.md) |


For now the default save location is at `~/Images`, will add support to choose other directory easily.

Or you can manually edit the location path by opening `main.py` and edit

```python
makefile("/home/%s/Images" % getpass.getuser())
```
to your desired path.

**Dependencies**:
* BeautifulSoup4
