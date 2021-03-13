# Overview

Measurement of lxml (python XML parser) behavior

The xml file (109 MB) is here.
http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/www/repository.html#SwissProt

Compare memory usage and elapsed time by counting the number of elements named "Entry" in this file.

1. use 'parse' (deserialize whole data at once)
2. use 'iterparse'
3. use 'iterparse' with memory optimization (see following blog post!)

# Reference

Awesome blog post
https://www.ibm.com/developerworks/xml/library/x-hiperfparse/

Sample XML data is also available here.
http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/
