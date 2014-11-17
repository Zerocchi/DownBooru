GelDown
=======

Simple Gelbooru CLI Downloader. Specifically designed for Windows.

Default directory is `C:\Gelbooru`, but you can change the directory to anywhere you want by editing

```python
newpath = r'C:Gelbooru\{}'.format(tags).split("+")[0]
```

into

```python
newpath = r'<your directory here>\{}'.format(tags).split("+")[0]
```

Dependency: 
-BeautifulSoup4

