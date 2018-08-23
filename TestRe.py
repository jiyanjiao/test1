import re

# s = '<span>808798人评价</span>'
html_text1 = '<div class="item">'\
                '<div class="pic">'\
                    '<em class="">1</em>'\
                    '<a href="https://movie.douban.com/subject/1292052/">'\
                        '<img width="100" alt="肖申克的救赎" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">'\
                    '</a>'\
                '</div>'\
                '<div class="info">'\
                    '<div class="hd">'\
                        '<a href="https://movie.douban.com/subject/1292052/" class="">'\
                            '<span class="title">肖申克的救赎</span>'\
                                    '<span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>'\
                                '<span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>'\
                        '</a>'\
                            '<span class="playable">[可播放]</span>'\
                    '</div>'\
                    '<div class="bd">'\
                        '<p class="">'\
                           ' 导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>'\
                            '1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情'\
                        '</p>'\
                        '<div class="star">'\
                                '<span class="rating5-t"></span>'\
                                '<span class="rating_num" property="v:average">9.6</span>'\
                                '<span property="v:best" content="10.0"></span>'\
                                '<span>1108123人评价</span>'\
                        '</div>'\
                   '</div>'\
                '</div>'\
            '</div>'
reObj1 = re.compile('<div.*?class="item">.*?'
                             + '<div.*?class="pic">.*?'
                             + '<em.*?class="">(.*?)</em>'
                             + '<div.*?class="info">.*?'
                             + '<span.*?class="title">(.*?)'
                             + '</span>.*?<span.*?class="title">(.*?)</span>.*?'
                             + '<span.*?class="other">(.*?)</span>.*?</a>.*?'
                             + '<div.*?class="bd">.*?<p.*?class="">.*?'
                             + '导演:(.*?)&nbsp;&nbsp;&nbsp;.*?</br>'
                             + '(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;'
                             + '(.*?)</p>.*?<div.*?class="star">.*?'
                             + '<span.*?'
                             + 'class="rating_num".*?property="v:average">'
                             + '(.*?)</sapn>.*?'
                             + '.*?<span>(.*?)人评价</span>.*?'
                             + '<p.*?class="quote">.*?'
                             + '<span.*?class="inq">(.*?)'
                             + '</span>.*?</p>',re.S)
print(reObj1.findall(html_text1))