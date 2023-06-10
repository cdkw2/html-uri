#!/usr/bin/env python
# coding: utf-8

# In[1]:

import base64

with open('your-html-file-address-here', 'rb') as file:
    html_content = file.read()

encoded_content = base64.b64encode(html_content).decode('utf-8')
print(encoded_content)
