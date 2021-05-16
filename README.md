# Analysis-on-Stop-Asian-Hate-trend-from-Twitter
> CIS600 SocialMedia&DataMining Team Project

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Features](#features)
* [Screenshots](#screenshots)
* [Room for Improvement](#room-for-improvement)
* [Sources](#sources)
* [Contact](#contact)
* [License](#license)


## General Information
- Our goal is using machine learning method classify the attitude of a tweet.  
- Collecting data using Twitter API (search and streaming) on the trend of Asian Hate.  
- Analyzing search data state by state to compare the difference between states.  
- Loading streaming data and label tweets in positive, objective and negative  
  (Another version in positive and negative).  
- Creating word clouds on positive, negative and objective tweets.  
- Constructing training and testing sets, using SVM, Naive Bayes, Single-layer CNN  
  and TextCNN to train the data.  
- Make attempt using BERT to train the data.  
  
- We also try to do the same process above in a two-sentiment classification (Negative + Positive)


## Technologies Used  
Programming Language  
- Python 3  
- Jupyter Notebook  
  
API   
- Twitter API (Standard v1.1)  
  
Libraries  
- numpy  
- os  
- pandas  
- seaborn  
- matplotlib  
- nltk  
- sklearn  
- jieba  
- keras  
- torch  
- re  
- functools  
- wordcloud  

## Setup
1. Install anaconda on your computer  
   - Windows: Follow <https://docs.anaconda.com/anaconda/install/windows/>  
   - Mac: Follow <https://docs.anaconda.com/anaconda/install/mac-os/>  
   - Linux: Follow <https://docs.anaconda.com/anaconda/install/linux/>  
2. Make sure you have installed python on your computer, here is the link:  
  <https://www.python.org/>, then open anaconda and select jupyter notebook. 
    
3. Download the data files in DataFiles/ on your computer  
  
4. Download the .ipynb or .py files in Code/ and open in jupyter notebook, 
  make sure that the directory is correct.  
  
5. Additionally, you can also only download the .html files in Code/ and open them.  
  



## Features
List the ready features here:
- Analysis on search data state by state  
- WordClouds on streaming data  
- SVM and Naive-Bayes models  
- Single-layer CNN and TextCNN  
- Two classifications (three-sentiments and two sentiments)  




## Sources
This project was inspired by...



## Contact
Created by the following members, feel free to contact us!  
-<yzhou01@syr.edu>  
-<hgao12@g.syr.edu>   
-<rli127@g.syr.edu>  
-<XKZMX1@gmail.com>  
-<xchen210@g.syr.edu>  
-<yli960918@gmail.com>  




## License
Copyright (c) [2021] [Yixin Zhou]
  
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  
  
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
