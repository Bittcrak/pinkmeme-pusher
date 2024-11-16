Download a text file from webshare or anywhere, the format for each line should be
> 198.23.239.134:6540:fcuedvzr:xxxxxxxxx



1. Download these files in a directory
2. Put the proxy text file in the same directory
3. Now install [GeckoDriver](https://github.com/mozilla/geckodriver) put the driver in that repo as well
4. get firefox
5. run pip install -r requirements.txt(the one I uploaded is a bit cluttered but it will work)
6. Now open a terminal in the same directory and Do this
      ```
      run cli.py -p path/to/proxy -u {URL/of/your/token}
      ```
DONE!
